#!/usr/bin/env python3
import os
import sys

# Walk through src and replace branding strings
replacements = [
    ('Deepin', 'Bikou'),
    ('deepin', 'bikou'),
    ('DEEPIN', 'BIKOU'),
    ('uniontech', 'bikou'),  # company references - be careful
    ('UnionTech', 'Bikou'),
]
