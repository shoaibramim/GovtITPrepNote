with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(2820, 2845):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
