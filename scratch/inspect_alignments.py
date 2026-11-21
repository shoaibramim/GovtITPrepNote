# Let's inspect each line in the corresponding files
# We can find which file contains lines around those numbers
with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    ch01 = f.readlines()
with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f:
    ch03 = f.readlines()
with open("latex/ch04_cybersecurity.tex", "r", encoding="utf-8") as f:
    ch04 = f.readlines()
with open("latex/ch07_software_engineering.tex", "r", encoding="utf-8") as f:
    ch07 = f.readlines()
with open("latex/ch08_cloud_ml.tex", "r", encoding="utf-8") as f:
    ch08 = f.readlines()
with open("latex/ch10_electronics_hardware.tex", "r", encoding="utf-8") as f:
    ch10 = f.readlines()

def print_around(lines, lineno, name, window=10):
    start = max(0, lineno - window)
    end = min(len(lines), lineno + window)
    print(f"=== {name} around L{lineno} ===")
    for i in range(start, end):
        print(f"{i+1}: {lines[i]}", end="")
    print("\n" + "="*40)

# ch01 L5249
print_around(ch01, 5249, "ch01", 10)
# ch04 L4171
print_around(ch04, 4171, "ch04", 10)
# ch10 L2399
print_around(ch10, 2399, "ch10", 10)
