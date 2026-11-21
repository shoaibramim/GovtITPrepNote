with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()
# let's see line 56
print("Line 56:")
print(repr(lines[55]))
print(repr(lines[56]))
