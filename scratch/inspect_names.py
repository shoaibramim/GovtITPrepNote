import re

# Given target names:
# "Shoaib, Ramim, Tonmoy, Tareq, Zunaeed, Likhon, Sifat, Hridoy, Bappi, Aurnob, Avinash, Talukder, Shojib"

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

# Let's inspect occurrences of Rahim, Karim, Hasan, Alice, Bob, etc. in ch02, ch04, ch05, ch06, ch07, etc.
names_to_check = ["Rahim", "Karim", "Hasan", "Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Mallory", "Trent", "John", "Jane", "Smith", "Ahmed"]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    found_in_file = []
    for idx, line in enumerate(lines):
        for name in names_to_check:
            if re.search(r'\b' + name + r'\b', line, re.IGNORECASE):
                found_in_file.append((idx + 1, name, line.strip()))
    
    if found_in_file:
        print(f"=== {fpath} ({len(found_in_file)} occurrences) ===")
        for line_no, name, line_str in found_in_file[:20]: # show first 20
            print(f"  L{line_no} [{name}]: {line_str[:120]}")
        if len(found_in_file) > 20:
            print(f"  ... and {len(found_in_file) - 20} more.")
