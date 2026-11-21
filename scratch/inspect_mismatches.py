with open("latex/ch06_operating_system.tex", "r", encoding="utf-8") as f:
    ch06_lines = f.readlines()

print("--- ch06 around line 1184 ---")
for i in range(1180, 1205):
    if i < len(ch06_lines):
        print(f"{i+1}: {ch06_lines[i]}", end="")

with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    ch09_lines = f.readlines()

print("\n--- ch09 around line 464 ---")
for i in range(460, 480):
    if i < len(ch09_lines):
        print(f"{i+1}: {ch09_lines[i]}", end="")
