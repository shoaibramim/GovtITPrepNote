with open("latex/ch10_electronics_hardware.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i in range(2380, 2405):
    print(f"{i+1}: {lines[i]}", end="")
