with open("latex/ch07_software_engineering.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(2335, 2370):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
