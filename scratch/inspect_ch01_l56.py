with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i in range(50, 65):
    print(f"{i+1}: {lines[i]}", end="")
