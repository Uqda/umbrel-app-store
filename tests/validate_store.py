"""Validate installable pins against public GHCR metadata, without Docker/secrets."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
manifest = (ROOT / 'uqda-network/umbrel-app.yml').read_text()
compose = (ROOT / 'uqda-network/docker-compose.yml').read_text()
version = re.search(r'^version: "([^"]+)"$', manifest, re.M)[1]
assert re.fullmatch(r'26\.0\.4-umbrel\.\d+', version)
assert 'id: uqda-network\n' in manifest
refs = re.findall(r'^\s+image: (\S+)$', compose, re.M)
assert len(refs) == 2 and refs[0] == refs[1]
assert re.fullmatch(r'ghcr\.io/uqda/core:' + re.escape(version) + r'@sha256:[a-f0-9]{64}', refs[0])
digest = refs[0].split('@')[1]
assert '${APP_PASSWORD}' in compose and 'APP_PORT: 8080' in compose
assert 'network_mode: host' in compose and '/dev/net/tun:/dev/net/tun' in compose
assert 'privileged:' not in compose and 'docker.sock' not in compose and 'ports:' not in compose
allowed = {'config/.gitkeep', 'control/.gitkeep'}
for file in (ROOT / 'uqda-network/data').rglob('*'):
    if file.is_file():
        assert file.relative_to(ROOT / 'uqda-network/data').as_posix() in allowed
        assert file.read_bytes() == b''

# Anonymous pull token is kept only in memory and never printed or cached.
query = urlencode({'service': 'ghcr.io', 'scope': 'repository:uqda/core:pull'})
with urlopen('https://ghcr.io/token?' + query, timeout=30) as response:
    token = json.load(response)['token']
accept = ','.join(['application/vnd.oci.image.index.v1+json',
                   'application/vnd.docker.distribution.manifest.list.v2+json',
                   'application/vnd.oci.image.manifest.v1+json',
                   'application/vnd.docker.distribution.manifest.v2+json'])

def read(resource, expected=None):
    request = Request('https://ghcr.io/v2/uqda/core/' + resource,
                      headers={'Authorization': 'Bearer ' + token, 'Accept': accept})
    with urlopen(request, timeout=30) as response:
        raw = response.read()
    if expected:
        assert 'sha256:' + hashlib.sha256(raw).hexdigest() == expected
    return json.loads(raw)

index = read('manifests/' + digest, digest)
assert read('manifests/' + version, digest) == index
platforms = {entry['platform']['architecture']: entry for entry in index['manifests']
             if entry.get('platform', {}).get('os') == 'linux'}
assert {'amd64', 'arm64'} <= platforms.keys()
for arch in ['amd64', 'arm64']:
    entry = platforms[arch]
    image = read('manifests/' + entry['digest'], entry['digest'])
    config = read('blobs/' + image['config']['digest'], image['config']['digest'])
    labels = config['config']['Labels']
    assert labels['org.opencontainers.image.version'] == version
    assert labels['org.opencontainers.image.source'] == 'https://github.com/Uqda/Core'
    assert re.fullmatch(r'[a-f0-9]{40}', labels['org.opencontainers.image.revision'])
gallery = re.findall(r'^  - (https://github.com/Uqda/Core/releases/download/umbrel-26\.0\.4-2/dashboard-(?:en|ar|mobile)\.png)$', manifest, re.M)
assert len(gallery) == 3
for url in gallery:
    with urlopen(url, timeout=30) as response:
        assert response.read(8) == b'\x89PNG\r\n\x1a\n'
icon = re.search(r'^icon: (https://raw\.githubusercontent\.com/Uqda/Core/[a-f0-9]{40}/contrib/umbrel/web/icon\.svg)$', manifest, re.M)[1]
with urlopen(icon, timeout=30) as response:
    assert b'<svg' in response.read(1024)
print('PASS: matching immutable pins, safe package boundaries, amd64/arm64 image digests and source labels')
print('PASS: released screenshots and source-pinned icon are publicly reachable')
