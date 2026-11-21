# Let's inspect ch01 around L5249 and lines 525, 633 in main.log
with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    ch01 = f.read()

idx = ch01.find(r"\begin{longtable}")
if idx != -1:
    print(ch01[idx:idx+200])

# Let's check lines 525 and 633 in main.log
with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    log_text = f.read()

import re
m1 = re.search(r'Overfull \\hbox [^\n]+ in alignment at lines 525--525.*?(?=\n\n)', log_text, re.DOTALL)
if m1:
    print("Alignment 525:")
    print(m1.group(0))

m2 = re.search(r'Overfull \\hbox [^\n]+ in alignment at lines 633--633.*?(?=\n\n)', log_text, re.DOTALL)
if m2:
    print("Alignment 633:")
    print(m2.group(0))
