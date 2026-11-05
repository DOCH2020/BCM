"""Validate the published beta's static catalog; no installation claim."""
import hashlib,json,re,runpy
from pathlib import Path
root=Path(__file__).resolve().parent
assert re.fullmatch(r'id: "bcm"\s+name: "BCM"\s*',(root/'umbrel-app-store.yml').read_text())
runpy.run_path(str(root/'check_beta_package.py'),run_name='__main__')
status=json.loads((root/'ecx-build-status.json').read_text())
assert status['published'] and status['status']=='published-amd64-beta-untested-on-umbrel'
assert not status['tests']['real_umbrel_lifecycle_verified']
assert not status['tests']['arm64_verified']
compose=json.loads((root/'bcm-ecx/docker-compose.yml').read_text())
assert all(s['image']==status['public_image_reference'] for n,s in compose['services'].items() if n!='app_proxy')
icon=(root/'ecx-icon.png').read_bytes()
assert hashlib.sha1(('blob '+str(len(icon))+'\0').encode()+icon).hexdigest()=='2ca2b0f267593290c419966f1981e2c3cd385a05'
for p in (root/'bcm-ecx').rglob('*'):
    if not p.is_file():continue
    assert p.suffix not in {'.db','.sqlite','.sqlite3','.key','.pem'}
    if p.suffix in {'.md','.yml','.json','.py'}:
        assert not re.search(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|umbrelmcp_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]{20,}|\b192\.168\.\d+\.\d+\b',p.read_bytes())
print(json.dumps({'checks_passed':True,'catalog_apps':1,'uses_verified_3d_icon':True,'umbrel_lifecycle_verified':False}))
