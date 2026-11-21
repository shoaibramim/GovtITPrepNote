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

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find \begin{tabularx}{\textwidth}{...} where no column is 'X'
    matches = list(re.finditer(r'\\begin\{tabularx\}\{[^\}]+\}\{([^\}]+)\}', content))
    for m in matches:
        spec = m.group(1).strip()
        if 'X' not in spec:
            lineno = content[:m.start()].count('\n') + 1
            # let's see full table tag
            print(f"{fpath}:L{lineno} -> spec='{spec}'")
