"""Static validation only; does not certify public image availability."""
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
app=root/'bcm-ecx'
m=json.loads((app/'umbrel-app.yml').read_text())
c=json.loads((app/'docker-compose.yml').read_text())
assert m['id']=='bcm-ecx' and m['version']=='0.1.0-beta.1'
assert m['icon']=='https://raw.githubusercontent.com/DOCH2020/BCM/main/ecx-icon.png'
assert 'beta' in m['releaseNotes'].lower()
services=c['services']
assert set(services)=={'app_proxy','node','enforcer','pool','dashboard'}
assert services['app_proxy']['environment']['APP_HOST']=='bcm-ecx_node_1'
for name in ['node','enforcer','pool','dashboard']:
    service=services[name]
    assert re.fullmatch(r'ghcr.io/doch2020/bcm-ecx:0\.1\.0-beta\.1@sha256:[a-f0-9]{64}',service['image'])
    assert service['user']=='1000:1000' and service['read_only']
    assert service['cap_drop']==['ALL'] and not service.get('privileged')
    assert not any('docker.sock' in v for v in service['volumes'])
assert services['node']['ports']==['3334:3334/tcp','3335:3335/tcp']
for name in ['enforcer','pool','dashboard']:
    assert services[name]['network_mode']=='service:node'
    assert not services[name].get('ports')
for name in ['chain','enforcer','pool','settings']:
    assert (app/'data'/name/'.gitkeep').exists()
assert 'BCM_SETUP_PASSWORD' in services['dashboard']['environment']
print(json.dumps({'static_checks_passed':True,'uses_3d_ecx_icon':True,'public_image_verified':False,'umbrel_install_verified':False}))
