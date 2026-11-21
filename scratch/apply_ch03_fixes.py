with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f:
    ch03 = f.read()

# Fix L1929: \begin{tabularx}{\textwidth}{ccccc} -> change to \begin{tabularx}{\textwidth}{c X X X X}
ch03_mod = ch03.replace(r"\begin{tabularx}{\textwidth}{ccccc}", r"\begin{tabularx}{\textwidth}{c X X X X}")

# Fix L2423: \begin{tabularx}{\textwidth}{p{2.8cm} c p{3.2cm} c c} -> change to \begin{tabularx}{\textwidth}{p{2.8cm} c X c c}
ch03_mod = ch03_mod.replace(r"\begin{tabularx}{\textwidth}{p{2.8cm} c p{3.2cm} c c}", r"\begin{tabularx}{\textwidth}{p{2.8cm} c X c c}")

# Fix L2829: wide tabular:
# \begin{tabular}{ccc}
# \textbf{Modulation Scheme} & \textbf{Number of Constellation Symbols ($M$)} & \textbf{Spectral Efficiency (Bits/Symbol = $\log_2 M$)} \\
# Let's check lines around 2829 in ch03
with open("latex/ch03_networking_subnetting.tex", "w", encoding="utf-8") as f:
    f.write(ch03_mod)
print("Updated ch03 tables!")
