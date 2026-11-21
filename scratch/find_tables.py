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

print("=== CHECKING TABLES IN FILES ===")
# Find table environments: tabular, tabularx, longtable
table_pattern = re.compile(r'\\begin\{(tabular|tabularx|longtable)\}(\[.*?\])?\{([^\}]+)\}', re.DOTALL)

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = list(table_pattern.finditer(content))
    if matches:
        print(f"\n--- {fpath} ({len(matches)} tables) ---")
        for i, m in enumerate(matches):
            env_type = m.group(1)
            col_spec = m.group(3).strip()
            # check if col_spec has many columns or long fixed widths
            # count columns: c, l, r, p{...}, X, etc.
            cols = len(re.findall(r'[clrpXm]', col_spec))
            # check if tabular with many cols without tabularx or resizebox or adjustbox
            # look at surrounding context (100 chars before)
            start_pos = m.start()
            preceding = content[max(0, start_pos-200):start_pos]
            is_wrapped = any(w in preceding for w in ["resizebox", "adjustbox", "table*"])
            # check table length
            if cols >= 5 or "p{" in col_spec or env_type == "tabular":
                # Let's inspect if it might overflow
                print(f"  Table #{i+1}: env={env_type}, cols={cols}, spec='{col_spec[:40]}', wrapped={is_wrapped}")

