#!/bin/bash
# usage: tools/batch_snap.sh width page...
w=$1; shift
printf "%s\n" "$@" | xargs -P 5 -I{} sh -c "python3 /home/claude/v4/tools/snap.py {} $w full > /dev/null 2>&1 || echo FAIL {}"
