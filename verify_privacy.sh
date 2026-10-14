#!/bin/bash
# Verify only privacy-related changes, not breaking functionality
echo "=== Privacy verification ==="
grep -rn 'remember-recent-files.*false\|recent-files-max-age.*0' /home/tinkerspace/bikou-workspace/src/deepin-desktop-schemas 2>&1 | wc -l
