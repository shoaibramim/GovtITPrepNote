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
    
    # Check for tabular without width control
    # Matches \begin{tabular}...
    for m in re.finditer(r'(\\begin\{tabular\}(\[[^\]]*\])?\{([^\}]+)\}.*?\\end\{tabular\})', content, re.DOTALL):
        tbl_full = m.group(1)
        spec = m.group(3)
        # count columns
        cols = spec.count('c') + spec.count('l') + spec.count('r')
        # check if it uses p{...}
        has_p = 'p{' in spec
        # length of rows
        lines = [l.strip() for l in tbl_full.split('\n') if '&' in l]
        max_line_len = max(len(l) for l in lines) if lines else 0
        if (cols >= 4 and not has_p and max_line_len > 90) or (cols >= 6) or max_line_len > 140:
            lineno = content[:m.start()].count('\n') + 1
            print(f"{fpath}:L{lineno} -> cols={cols}, max_len={max_line_len}, spec='{spec}'")
            # print sample
            if lines:
                print(f"   Row 1: {lines[0][:100]}")
