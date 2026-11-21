# -*- coding: utf-8 -*-
"""
Master Build Script for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Imports content from all 10 generator modules, verifies environment balances,
and outputs latex/ch17_electronics_hardware.tex
"""

import os
import sys
import re
from collections import Counter

# Add scratch to sys.path
scratch_dir = os.path.dirname(os.path.abspath(__file__))
if scratch_dir not in sys.path:
    sys.path.insert(0, scratch_dir)

print("Importing all 10 module contents...")
assembled_text = []

for i in range(1, 11):
    mod_name = f'gen_ch17_mod{i}'
    mod = __import__(mod_name)
    fn_name = f'get_mod{i}_tex'
    if hasattr(mod, fn_name):
        text = getattr(mod, fn_name)().strip()
    elif hasattr(mod, 'content'):
        text = getattr(mod, 'content').strip()
    else:
        raise AttributeError(f"Could not find content in {mod_name}")
    assembled_text.append(text)
    print(f"  [OK] Loaded {mod_name} (length: {len(text)} chars)")

master_content = "\n\n".join(assembled_text) + "\n"

# Verify environment balance
print("\nVerifying environment balances...")
begins = re.findall(r'\\begin\{([a-zA-Z0-9*]+)\}', master_content)
ends = re.findall(r'\\end\{([a-zA-Z0-9*]+)\}', master_content)

c_begins = Counter(begins)
c_ends = Counter(ends)

all_envs = sorted(list(set(begins) | set(ends)))
balance_ok = True
for env in all_envs:
    b_count = c_begins.get(env, 0)
    e_count = c_ends.get(env, 0)
    if b_count != e_count:
        print(f"  [ERROR] Mismatch for environment '{env}': \\begin={b_count}, \\end={e_count}")
        balance_ok = False
    else:
        print(f"  [BALANCED] {env}: {b_count}")

if not balance_ok:
    print("\nAborting: environment imbalance detected!")
    sys.exit(1)

# Write to target latex file
workspace_dir = os.path.abspath(os.path.join(scratch_dir, '..'))
output_path = os.path.join(workspace_dir, 'latex', 'ch17_electronics_hardware.tex')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(master_content)

print(f"\nSuccessfully wrote {output_path}")
print(f"Total lines: {len(master_content.splitlines())}")
print(f"Total characters: {len(master_content)}")
