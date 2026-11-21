# Inspect all 27 tabularx without X
with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f: ch01 = f.read()
with open("latex/ch02_algorithms.tex", "r", encoding="utf-8") as f: ch02 = f.read()
with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f: ch03 = f.read()
with open("latex/ch04_cybersecurity.tex", "r", encoding="utf-8") as f: ch04 = f.read()
with open("latex/ch05_dbms_sql.tex", "r", encoding="utf-8") as f: ch05 = f.read()
with open("latex/ch07_software_engineering.tex", "r", encoding="utf-8") as f: ch07 = f.read()
with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f: ch09 = f.read()
with open("latex/ch10_electronics_hardware.tex", "r", encoding="utf-8") as f: ch10 = f.read()
with open("latex/ch11_programming.tex", "r", encoding="utf-8") as f: ch11 = f.read()

def get_snippet(content, lineno):
    lines = content.splitlines()
    start = max(0, lineno - 2)
    end = min(len(lines), lineno + 8)
    return "\n".join(lines[start:end])

checks = [
    ("ch01", ch01, 1337),
    ("ch02", ch02, 734),
    ("ch02", ch02, 4116),
    ("ch03", ch03, 1929),
    ("ch03", ch03, 2423),
    ("ch04", ch04, 4163),
    ("ch05", ch05, 152),
    ("ch05", ch05, 609),
    ("ch05", ch05, 684),
    ("ch05", ch05, 2863),
    ("ch05", ch05, 3207),
    ("ch05", ch05, 3224),
    ("ch07", ch07, 199),
    ("ch07", ch07, 1277),
    ("ch09", ch09, 308),
    ("ch09", ch09, 464),
    ("ch09", ch09, 533),
    ("ch09", ch09, 621),
    ("ch09", ch09, 687),
    ("ch09", ch09, 723),
    ("ch09", ch09, 869),
    ("ch09", ch09, 1269),
    ("ch09", ch09, 1563),
    ("ch09", ch09, 2522),
    ("ch10", ch10, 1826),
    ("ch10", ch10, 2388),
    ("ch11", ch11, 1227)
]

for name, text, l in checks:
    print(f"=== {name} L{l} ===")
    print(get_snippet(text, l))
    print("="*40)
