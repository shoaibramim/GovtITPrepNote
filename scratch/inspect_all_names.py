import re

with open("latex/ch02_algorithms.tex", "r", encoding="utf-8") as f: ch02 = f.read()
with open("latex/ch04_cybersecurity.tex", "r", encoding="utf-8") as f: ch04 = f.read()
with open("latex/ch05_dbms_sql.tex", "r", encoding="utf-8") as f: ch05 = f.read()
with open("latex/ch06_operating_system.tex", "r", encoding="utf-8") as f: ch06 = f.read()

# Let's inspect all places in ch05 with Rahim, Karim, Hasan
print("=== CH05 OCCURRENCES ===")
for i, line in enumerate(ch05.splitlines()):
    if any(n in line for n in ["Rahim", "Karim", "Hasan"]):
        print(f"L{i+1}: {line}")

print("\n=== CH02 OCCURRENCES ===")
for i, line in enumerate(ch02.splitlines()):
    if any(n in line for n in ["Rahim", "Karim"]):
        print(f"L{i+1}: {line}")

print("\n=== CH04 OCCURRENCES ===")
for i, line in enumerate(ch04.splitlines()):
    if any(n in line for n in ["Alice", "Bob"]):
        print(f"L{i+1}: {line}")
