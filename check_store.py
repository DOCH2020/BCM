"""Validate the store foundation without claiming app runtime verification."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parent
store = (root / 'umbrel-app-store.yml').read_text(encoding='utf-8')
assert re.fullmatch(r'id: "bcm"\s+name: "BCM"\s*', store), 'Invalid store identity'
draft = json.loads((root / 'ecx-draft.json').read_text())
assert draft['id'].startswith('bcm-')
assert (root / draft['icon_asset']).is_file(), 'Missing app icon'
assert draft['status'] == 'draft-not-installable'
assert draft['runtime_images'] is None
assert not draft['fresh_umbrel_install_verified']
build = json.loads((root / draft['build_status_file']).read_text())
assert build['app_id'] == draft['id']
assert build['status'] == 'private-build-tested-not-installable'
assert build['architecture'] == 'linux/amd64'
assert not build['published'] and build['public_image_reference'] is None
assert not build['tests']['real_umbrel_lifecycle_verified']
assert not build['tests']['arm64_verified']
assert re.fullmatch(r'sha256:[a-f0-9]{64}', build['oci_manifest_digest'])
assert re.fullmatch(r'[a-f0-9]{64}', build['archive_sha256'])
catalog = list(root.glob('*/umbrel-app.yml'))
assert not catalog, 'Installable apps need a separate release validation gate'
patterns = [
    rb'umbrelmcp_[A-Za-z0-9_]+',
    rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    rb'gh[pousr]_[A-Za-z0-9]{20,}',
    rb'\bbc1[a-z0-9]{25,}\b',
    rb'\b192\.168\.[0-9]{1,3}\.[0-9]{1,3}\b',
]
checked = 0
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.relative_to(root).parts:
        continue
    assert path.suffix not in {'.db', '.sqlite', '.sqlite3', '.key', '.pem'}, 'Unexpected private/runtime file'
    if path.suffix in {'.md', '.json', '.yml', '.py'}:
        data = path.read_bytes()
        assert not any(re.search(pattern, data) for pattern in patterns), 'Potential personal data: ' + str(path.relative_to(root))
    checked += 1
print(json.dumps({'store': 'BCM', 'id': 'bcm', 'checks_passed': True,
                  'files_checked': checked, 'installable_apps': len(catalog),
                  'draft_apps': 1, 'publication_checked': False}))
