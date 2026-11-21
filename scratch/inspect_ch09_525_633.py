with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- ch09 lines 520 to 545 ---")
for i in range(519, 545):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- ch09 lines 620 to 645 ---")
for i in range(619, 645):
    print(f"{i+1}: {lines[i]}", end="")
