with open("latex/ch08_cloud_ml.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(80, 115):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
