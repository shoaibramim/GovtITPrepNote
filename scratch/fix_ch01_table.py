with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace longtable widths: 9.8cm + 6.8cm = 16.6cm -> 10.5cm + 6.2cm = 16.7cm (total with padding <= 17.5cm)
# Actually \begin{longtable}{r p{9.8cm} p{6.8cm}}
# r takes ~0.6cm. 0.6 + 9.8 + 6.8 + 6 * \tabcolsep (6*6pt = 36pt = 1.27cm) = 18.47cm > 18.0cm!
# That explains why it overflowed by 7.9pt!
# If we change to:
# r takes 0.6cm. p{10.2cm} and p{5.7cm}: 0.6 + 10.2 + 5.7 + 1.27 = 17.77cm <= 18.0cm!

old_lt = r"\begin{longtable}{r p{9.8cm} p{6.8cm}}"
new_lt = r"\begin{longtable}{r p{10.0cm} p{5.8cm}}"

if old_lt in text:
    text = text.replace(old_lt, new_lt)
    with open("latex/ch01_data_structures.tex", "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated ch01 longtable!")
else:
    print("Could not find old_lt in ch01")
