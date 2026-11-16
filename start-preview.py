"""Verify the complete backup and preview it using only Python's standard library."""
from pathlib import Path
import hashlib
import http.server
import functools
import sys

root = Path(__file__).resolve().parent
manifest = root / 'ASSET_MANIFEST.sha256'
failures = []
for line in manifest.read_text().splitlines():
    expected, name = line.split('  ', 1)
    path = root / name
    if not path.is_file():
        failures.append('MISSING: ' + name)
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        failures.append('CHANGED: ' + name)
if failures:
    print('\n'.join(failures))
    print('Please extract the complete ZIP again into a NEW folder.')
    sys.exit(1)
print('All website files verified. Open http://localhost:8000/')
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root / 'dist'))
http.server.ThreadingHTTPServer(('127.0.0.1', 8000), handler).serve_forever()
