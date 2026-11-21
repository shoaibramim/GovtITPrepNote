with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find tabularx around L1337
pos = 0
for i in range(1336):
    pos = text.find('\n', pos) + 1

print(text[pos:pos+500])
