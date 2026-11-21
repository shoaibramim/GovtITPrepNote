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

print("=== CHECKING ALL TABULARX WITHOUT ANY 'X' COLUMN ===")
pure_no_x = []
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    for m in re.finditer(r'\\begin\{tabularx\}\s*\{([^\}]+)\}\s*\{([^\}]+)\}', content):
        width = m.group(1).strip()
        spec = m.group(2).strip()
        # count X in the entire spec
        if 'X' not in spec:
            lineno = content[:m.start()].count('\n') + 1
            pure_no_x.append((fpath, lineno, width, spec))

print(f"Total tabularx without X: {len(pure_no_x)}")
for item in pure_no_x:
    print(f"{item[0]}:L{item[1]} -> width='{item[2]}', spec='{item[3]}'")
