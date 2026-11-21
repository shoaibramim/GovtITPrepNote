import re

with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    text = f.read()

# L5249 longtable
m = re.search(r'\\begin\{longtable\}\{r\s+p\{9\.8cm\}\s+p\{6\.8cm\}\}', text)
if m:
    print("Found longtable in ch01!")
else:
    print("Not found by regex, checking lines around 5249...")
    lines = text.splitlines()
    for i in range(5245, 5255):
        print(lines[i])
