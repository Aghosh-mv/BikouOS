#!/usr/bin/env python3
import os
import sys

src = '/home/tinkerspace/bikou-workspace/src'
# Files to process (text)
exts = ('.h', '.hpp', '.cpp', '.c', '.cc', '.qml', '.js', '.ts', '.py', '.go', '.sh', '.desktop', '.xml', '.json', '.conf', '.in', '.txt', '.md', '.service', '.policy', '.gschema.xml', '.theme', '.info', '.mirrors', '.ini', '.cfg')
count = 0

for root, dirs, files in os.walk(src):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith(exts) or '.' not in f:
            path = os.path.join(root, f)
            try:
                with open(path, 'rb') as fh:
                    data = fh.read()
                if b'\x00' in data:
                    continue
                s = data.decode('utf-8', errors='ignore')
                if 'Deepin' in s or 'deepin' in s:
                    # Be selective - avoid changing URLs in git history references? 
                    # Replace Deepin (brand) but keep vendor X-Deepin keys? 
                    # Keep "deepin" in paths if they refer to upstream; but for our fork, we want branding
                    # For user-facing strings, replace
                    news = s.replace('Deepin', 'Bikou')
                    if news != s:
                        with open(path, 'w', encoding='utf-8') as fh:
                            fh.write(news)
                        count += 1
                        print('mod:', path)
            except Exception as e:
                pass
print('total:', count)
