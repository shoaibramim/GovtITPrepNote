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

print("=== CHECKING TABLE WIDTHS & PACKAGES IN TABLES ===")

# Look for tabulars with many columns or long text in columns without p{} or X
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find \begin{tabular}... \end{tabular}
    matches = list(re.finditer(r'\\begin\{(tabular|tabularx)\}(\[[^\]]*\])?\{([^\}]+)\}(.*?)\\end\{\1\}', content, re.DOTALL))
    for idx, m in enumerate(matches):
        env = m.group(1)
        spec = m.group(3)
        body = m.group(4)
        
        # Check if table has text that might be wide
        # Count max columns across rows
        rows = [r for r in body.split(r'\\') if r.strip() and not r.strip().startswith(r'\hline') and not r.strip().startswith(r'\midrule') and not r.strip().startswith(r'\toprule') and not r.strip().startswith(r'\bottomrule')]
        max_cols = 0
        max_row_len = 0
        longest_row = ""
        for r in rows:
            cells = r.split('&')
            if len(cells) > max_cols:
                max_cols = len(cells)
            row_len = sum(len(c.strip()) for c in cells)
            if row_len > max_row_len:
                max_row_len = row_len
                longest_row = r.strip()
        
        # If env is tabular (not tabularx) and max_row_len is large (e.g. > 100 chars or > 4 columns with text)
        if env == "tabular" and (max_row_len > 120 or (max_cols >= 5 and max_row_len > 80)):
            # check line number
            lineno = content[:m.start()].count('\n') + 1
            print(f"{fpath}:L{lineno} -> {env}{{{spec}}}, cols={max_cols}, max_len={max_row_len}")
            print(f"   Sample row: {longest_row[:100]}...\n")
        elif env == "tabularx":
            # Check if tabularx has very wide content or is inside something
            if max_row_len > 250:
                lineno = content[:m.start()].count('\n') + 1
                # print(f"tabularx {fpath}:L{lineno} -> cols={max_cols}, max_len={max_row_len}")
