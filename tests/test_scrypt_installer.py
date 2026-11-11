"""Reproduce root-owned PEP/BEL mounts without touching any real app data."""
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'bcm-ltc-merged'
HOOK = APP / 'hooks/pre-start'
NAMES = ('ltc', 'doge', 'soq', 'pep', 'bel', 'settings', 'pool', 'telemetry')


@unittest.skipUnless(os.name == 'posix' and os.geteuid() == 0,
                     'Linux root needed to reproduce Docker-created owners')
class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='bcm-installer-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.base.chmod(0o755)
        self.app = self.base / 'bcm-ltc-merged'
        self.app.mkdir(mode=0o755)
        self.env = dict(os.environ, APP_ID='bcm-ltc-merged', APP_DATA_DIR=str(self.app))
        self.env.pop('APP_DATA_ROOT', None)
        self.data = self.app / 'data'

    def run_hook(self, okay=True, install=False):
        path = APP / 'hooks/pre-install' if install else HOOK
        result = subprocess.run(['bash', str(path)], env=self.env, capture_output=True, text=True)
        self.assertEqual(result.returncode == 0, okay, result.stderr)
        return result

    def test_fresh_install_creates_all_mounts_and_allows_node_user_writes(self):
        self.run_hook(install=True)
        for name in NAMES:
            p = self.data / name
            self.assertEqual((p.stat().st_uid, p.stat().st_gid), (1000, 1000))
        # Prove the actual daemon UID can create its lock, not merely inspect modes.
        child = os.fork()
        if child == 0:
            try:
                os.setgroups([])
                os.setgid(1000)
                os.setuid(1000)
                for name in ('pep', 'bel'):
                    (self.data / name / '.lock').write_bytes(b'lock probe')
                os._exit(0)
            except Exception:
                os._exit(1)
        self.assertEqual(os.waitpid(child, 0)[1], 0)

    def test_upgrade_repairs_root_folders_preserving_chain_and_settings(self):
        self.data.mkdir()
        for name in NAMES:
            (self.data / name).mkdir()
        chain = self.data / 'ltc/blocks'
        chain.mkdir(mode=0o750)
        payload = chain / 'blk00000.dat'
        payload.write_bytes(b'existing blockchain bytes')
        settings = self.data / 'settings/installation.json'
        settings.write_text('{"addresses":{"ltc":"unchanged"}}')
        paths = (chain, payload, settings)
        before = {p: (p.stat().st_ino, p.stat().st_uid, p.stat().st_gid,
                      stat.S_IMODE(p.stat().st_mode), p.stat().st_mtime_ns) for p in paths}
        self.run_hook()
        self.run_hook()
        for p in paths:
            self.assertEqual(before[p], (p.stat().st_ino, p.stat().st_uid, p.stat().st_gid,
                                        stat.S_IMODE(p.stat().st_mode), p.stat().st_mtime_ns))
        self.assertEqual(payload.read_bytes(), b'existing blockchain bytes')
        self.assertIn('unchanged', settings.read_text())
        self.assertEqual((self.data / 'pep').stat().st_uid, 1000)

    def test_relocated_root_takes_precedence(self):
        moved = self.base / 'external-app-data'
        moved.mkdir()
        self.env['APP_DATA_ROOT'] = str(moved)
        self.run_hook()
        self.assertTrue((moved / 'pep').is_dir())
        self.assertFalse(self.data.exists())

    def test_unavailable_external_root_does_not_initialize_internal_storage(self):
        self.env['APP_DATA_ROOT'] = str(self.base / 'missing-external-root')
        self.run_hook(okay=False)
        self.assertFalse(self.data.exists())
        self.assertFalse(Path(self.env['APP_DATA_ROOT']).exists())

    def test_symlink_child_cannot_change_outside_ownership(self):
        self.data.mkdir()
        outside = self.base / 'outside'
        outside.mkdir()
        (self.data / 'pep').symlink_to(outside, target_is_directory=True)
        self.run_hook(okay=False)
        self.assertEqual(outside.stat().st_uid, 0)
        self.assertFalse((self.data / 'ltc').exists())

    def test_symlink_root_is_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        self.data.symlink_to(outside, target_is_directory=True)
        self.run_hook(okay=False)
        self.assertEqual(list(outside.iterdir()), [])

    def test_missing_app_path_does_not_use_working_directory(self):
        del self.env['APP_DATA_DIR']
        self.run_hook(okay=False)
        self.assertFalse(self.data.exists())

    def test_wrong_app_id_is_rejected(self):
        self.env['APP_ID'] = 'other-app'
        self.run_hook(okay=False)
        self.assertFalse(self.data.exists())


class PackageTests(unittest.TestCase):
    def test_installer_only_release_preserves_verified_runtime(self):
        manifest = json.loads((APP / 'umbrel-app.yml').read_text())
        compose = json.loads((APP / 'docker-compose.yml').read_text())
        self.assertEqual(manifest['version'], '0.1.0-beta.4')
        self.assertEqual(manifest['id'], 'bcm-ltc-merged')
        self.assertEqual(manifest['port'], 8093)
        for name, service in compose['services'].items():
            if name == 'app_proxy':
                continue
            self.assertEqual(service['user'], '1000:1000')
            self.assertTrue(service['read_only'])
            self.assertEqual(service['cap_drop'], ['ALL'])
            self.assertEqual(service['image'], 'ghcr.io/doch2020/bcm-ltc-merged:0.1.0-beta.3@sha256:4ea8e36f87c53dd6d2bca245e657816606a780799f9f5226c3172a56f349a208')


if __name__ == '__main__':
    unittest.main()
