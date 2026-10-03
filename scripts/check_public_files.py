#!/usr/bin/env python
"""Inspect the Git index without opening ignored private runtime files."""
import re
import subprocess
import sys
from pathlib import PurePosixPath

entries = subprocess.check_output(['git', 'ls-files', '--stage', '-z']).decode().split('\0')
errors = []
for entry in filter(None, entries):
    metadata, name = entry.split('\t', 1)
    mode, object_id, _ = metadata.split()
    if mode == '160000':
        continue  # separately audited source repositories, never runtime copies
    path = PurePosixPath(name)
    blocked = (path.name in {'.env', 'cookies.json', 'credentials.json', 'account.json', 'providers.env'}
               or (path.name.startswith('.env.') and not path.name.endswith('.example'))
               or path.suffix.lower() in {'.sqlite', '.sqlite3', '.db', '.pem', '.key', '.mp4', '.mov', '.zip'}
               or any(part in {'private', 'runtime', 'profiles', 'node_modules', 'DATA'} for part in path.parts))
    if blocked:
        errors.append(f'private/generated path staged: {name}')
        continue
    data = subprocess.check_output(['git', 'cat-file', 'blob', object_id])
    patterns = [rb'-----BEGIN (?:OPENSSH|RSA|EC|DSA|PRIVATE) (?:PRIVATE )?KEY-----',
                rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|npm_[A-Za-z0-9]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{25,})\b']
    if any(re.search(pattern, data) for pattern in patterns):
        errors.append(f'credential pattern staged: {name}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('Public-file check passed; private runtime state must remain outside Git.')
