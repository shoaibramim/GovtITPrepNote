with open("latex/ch07_software_engineering.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i in [134, 199, 236, 823, 848, 870]:
    print(f"L{i}:")
    print("".join(lines[i-1:i+6]))
    print("="*40)
