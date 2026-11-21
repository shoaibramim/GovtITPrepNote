with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(500, 526):
    print(f"{i+1}: {lines[i]}", end="")
