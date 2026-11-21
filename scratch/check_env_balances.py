import re

files = [
    "latex/ch01_data_structures.tex",
    "latex/ch02_algorithms.tex",
    "latex/ch03_networking_subnetting.tex",
    "latex/ch04_cybersecurity.tex",
    "latex/ch05_dbms_sql.tex",
    "latex/ch06_operating_system.tex",
    "latex/ch07_software_engineering.tex",
    "latex/ch08_cloud_ml.tex",
    "latex/ch09_computer_architecture.tex",
    "latex/ch10_electronics_hardware.tex",
    "latex/ch11_programming.tex",
    "latex/chapter1_location.tex",
    "latex/chapter2_technical.tex",
    "latex/chapter3_banking.tex"
]

print("=== CHECKING ENVIRONMENT PAIR MATCHES ===")
envs_to_check = ['tabular', 'tabularx', 'table', 'figure', 'tcolorbox', 'longtable']

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check open and close counts
    for env in envs_to_check:
        opens = len(re.findall(r'\\begin\{' + env + r'\}', content))
        closes = len(re.findall(r'\\end\{' + env + r'\}', content))
        if opens != closes:
            print(f"MISMATCH in {fpath}: \\begin{{{env}}}={opens} vs \\end{{{env}}}={closes}")

# Also check sequential pairings of tabular vs tabularx
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    stack = []
    for line_no, line in enumerate(lines):
        m_begin = re.findall(r'\\begin\{(tabular|tabularx)\}', line)
        m_end = re.findall(r'\\end\{(tabular|tabularx)\}', line)
        for b in m_begin:
            stack.append((b, line_no + 1))
        for e in m_end:
            if not stack:
                print(f"Unexpected \\end{{{e}}} in {fpath}:L{line_no+1}")
            else:
                top, top_line = stack.pop()
                if top != e:
                    print(f"MISMATCHED PAIR in {fpath}: \\begin{{{top}}} at L{top_line} closed by \\end{{{e}}} at L{line_no+1}")
