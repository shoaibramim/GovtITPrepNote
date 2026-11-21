# -*- coding: utf-8 -*-
"""
Master Build Script for Chapter 18: Programming — Problem Solving, Code Tracing, OOP and Practical IT Skills
Imports content from all 8 generator modules, verifies environment balances,
and outputs latex/ch18_programming.tex
"""

import os
import sys
import re
from collections import Counter

scratch_dir = os.path.dirname(os.path.abspath(__file__))
if scratch_dir not in sys.path:
    sys.path.insert(0, scratch_dir)

print("Importing all 8 Chapter 18 module contents...")
assembled_text = []

for i in range(1, 9):
    mod_name = f'gen_ch18_mod{i}'
    mod = __import__(mod_name)
    text = getattr(mod, 'content', '').strip()
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

# Check unescaped dollars
clean_text = master_content.replace(r'\$', '')
# Also remove lstlisting blocks from dollar checks because code comments or strings might have characters
no_code = re.sub(r'\\begin\{lstlisting\}(?:\[[^\]]*\])?.*?\\end\{lstlisting\}', '', clean_text, flags=re.DOTALL)
dollars = re.findall(r'(?<!\\)\$', no_code)
print(f"\nUnescaped dollars outside lstlisting: {len(dollars)} (Even: {len(dollars) % 2 == 0})")
if len(dollars) % 2 != 0:
    print("  [WARNING] Odd number of unescaped dollar signs detected!")
    balance_ok = False

if not balance_ok:
    print("\nAborting: balance check failed!")
    sys.exit(1)

# Write to target latex file
workspace_dir = os.path.abspath(os.path.join(scratch_dir, '..'))
output_path = os.path.join(workspace_dir, 'latex', 'ch18_programming.tex')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(master_content)

print(f"\nSuccessfully wrote {output_path}")
print(f"Total lines: {len(master_content.splitlines())}")
print(f"Total characters: {len(master_content)}")
