#!/usr/bin/env python3
import os

src = '/home/tinkerspace/bikou-workspace/src'
for root, dirs, files in os.walk(src):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.desktop'):
            path = os.path.join(root, f)
            try:
                with open(path) as fh:
                    s = fh.read()
                changed = False
                if 'Deepin' in s:
                    s = s.replace('Deepin', 'Bikou')
                    changed = True
                if 'deepin' in s and 'X-Deepin' not in s:  # avoid overreplacing vendor keys? X-Deepin keep as is for compat or change?
                    pass  # be conservative
                if changed:
                    with open(path, 'w') as fh:
                        fh.write(s)
                    print('updated', path)
            except:
                pass
