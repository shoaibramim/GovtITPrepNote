# Let's inspect ch01 L1337, ch02 L734, ch02 L4116, ch03 L1929, ch03 L2423
with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f: ch01 = f.read()
with open("latex/ch02_algorithms.tex", "r", encoding="utf-8") as f: ch02 = f.read()
with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f: ch03 = f.read()

# ch01 L1337: \begin{tabularx}{0.85\textwidth}{ccccc} -> change to \begin{tabular}{ccccc}
ch01 = ch01.replace(r"\begin{tabularx}{0.85\textwidth}{ccccc}", r"\begin{tabular}{ccccc}")
ch01 = ch01.replace(r"""4 & 20 & 1    & --- & --- \\
\bottomrule
\end{tabularx}""", r"""4 & 20 & 1    & --- & --- \\
\bottomrule
\end{tabular}""")

with open("latex/ch01_data_structures.tex", "w", encoding="utf-8") as f:
    f.write(ch01)

# ch02 L734:
# Let's check exact string around L734 in ch02
idx = ch02.find(r"p{3.2cm} p{1.8cm}")
if idx != -1:
    print("Found L734 in ch02, snippet:")
    print(ch02[idx-30:idx+70])
    # Replace it properly
    # \begin{tabularx}{\textwidth}{p{3.2cm} p{1.8cm} p{1.8cm} p{1.8cm} p{2.6cm} c c}
    ch02 = ch02.replace(r"\begin{tabularx}{\textwidth}{p{3.2cm} p{1.8cm} p{1.8cm} p{1.8cm} p{2.6cm} c c}",
                        r"\begin{tabularx}{\textwidth}{l c c c X c c}")

# ch02 L4116:
idx2 = ch02.find(r"p{5.5cm} c c")
if idx2 != -1:
    print("Found L4116 in ch02, snippet:")
    print(ch02[idx2-30:idx2+50])
    ch02 = ch02.replace(r"\begin{tabularx}{\textwidth}{p{5.5cm} c c}",
                        r"\begin{tabularx}{\textwidth}{X c c}")

with open("latex/ch02_algorithms.tex", "w", encoding="utf-8") as f:
    f.write(ch02)

# ch03 L1929 & L2423:
idx3 = ch03.find(r"\begin{tabularx}{\textwidth}{ccccc}")
if idx3 != -1:
    print("Found L1929 in ch03!")
    ch03 = ch03.replace(r"\begin{tabularx}{\textwidth}{ccccc}",
                        r"\begin{tabularx}{\textwidth}{c X X X X}")

idx4 = ch03.find(r"p{2.8cm} c p{3.2cm} c c")
if idx4 != -1:
    print("Found L2423 in ch03!")
    ch03 = ch03.replace(r"\begin{tabularx}{\textwidth}{p{2.8cm} c p{3.2cm} c c}",
                        r"\begin{tabularx}{\textwidth}{p{2.8cm} c X c c}")

with open("latex/ch03_networking_subnetting.tex", "w", encoding="utf-8") as f:
    f.write(ch03)

# ch09 remaining:
with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f: ch09 = f.read()
# L464: \begin{tabularx}{0.85\textwidth}{c c c c c c c c} -> \begin{tabular}{c c c c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{0.85\textwidth}{c c c c c c c c}", r"\begin{tabular}{c c c c c c c c}")
ch09 = ch09.replace(r"""0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
\bottomrule
\end{tabularx}
\caption{Octal to 3-bit Binary Conversion Table}""", r"""0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
\bottomrule
\end{tabular}
\caption{Octal to 3-bit Binary Conversion Table}""")

# L533:
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Hexadecimal to 4-bit Binary Conversion Table (8 through F)}""", r"""\bottomrule
\end{tabular}
\caption{Hexadecimal to 4-bit Binary Conversion Table (8 through F)}""")

# L1269:
ch09 = ch09.replace(r"\begin{tabularx}{0.85\textwidth}{c c c c c c c c}", r"\begin{tabular}{c c c c c c c c}")
ch09 = ch09.replace(r"""1 & 1 & X & 0 & X & 0 & 1 & 0 \\
\bottomrule
\end{tabularx}
\caption{Master Excitation Table for All Flip-Flops}""", r"""1 & 1 & X & 0 & X & 0 & 1 & 0 \\
\bottomrule
\end{tabular}
\caption{Master Excitation Table for All Flip-Flops}""")

with open("latex/ch09_computer_architecture.tex", "w", encoding="utf-8") as f:
    f.write(ch09)

print("Finished applying all cleanups!")
