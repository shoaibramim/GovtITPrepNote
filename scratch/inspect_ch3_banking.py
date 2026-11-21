with open("latex/chapter3_banking.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(470, 505):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
