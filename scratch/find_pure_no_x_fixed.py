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

print("=== CHECKING FOR TABULARX WHERE NO COLUMN HAS 'X' (FIXED REGEX) ===")
pure_no_x = []
# Match \begin{tabularx}{arg1}{arg2} allowing nested braces in arg2
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find \begin{tabularx}
    idx = 0
    while True:
        pos = content.find(r'\begin{tabularx}', idx)
        if pos == -1:
            break
        # find first brace
        b1_start = content.find('{', pos + len(r'\begin{tabularx}'))
        b1_end = content.find('}', b1_start)
        width = content[b1_start+1:b1_end].strip()
        # find second brace block (may contain nested braces like p{7.5cm})
        b2_start = content.find('{', b1_end)
        # find matching closing brace
        depth = 0
        b2_end = b2_start
        while b2_end < len(content):
            if content[b2_end] == '{':
                depth += 1
            elif content[b2_end] == '}':
                depth -= 1
                if depth == 0:
                    break
            b2_end += 1
        spec = content[b2_start+1:b2_end].strip()
        if 'X' not in spec:
            lineno = content[:pos].count('\n') + 1
            pure_no_x.append((fpath, lineno, width, spec))
        idx = b2_end

print(f"Total tabularx without X: {len(pure_no_x)}")
for item in pure_no_x:
    print(f"{item[0]}:L{item[1]} -> width='{item[2]}', spec='{item[3]}'")
