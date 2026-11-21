# Fix ch06:
with open("latex/ch06_operating_system.tex", "r", encoding="utf-8") as f:
    ch06 = f.read()

# L1184 is \begin{tabularx}{\textwidth}{l c >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
# L1194 was \end{tabular}
ch06 = ch06.replace(r"""\textbf{99.9999\% ("Six Nines")} & 0.999999 & $31.54\text{ seconds}$ & $2.59\text{ seconds}$ \\
\bottomrule
\end{tabular}
\end{table}""", r"""\textbf{99.9999\% ("Six Nines")} & 0.999999 & $31.54\text{ seconds}$ & $2.59\text{ seconds}$ \\
\bottomrule
\end{tabularx}
\end{table}""")

with open("latex/ch06_operating_system.tex", "w", encoding="utf-8") as f:
    f.write(ch06)

# Fix ch09:
# In ch09, we converted \begin{tabularx} to \begin{tabular} for:
# L464, L533, L687, L723, L869, L1269, L2522
# Let's inspect each \end{tabularx} at those lines and replace with \end{tabular}
with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Let's write a script that replaces \end{tabularx} with \end{tabular} for those specific table blocks
for idx in [472, 541, 695, 735, 878, 1277, 2530]:
    if idx < len(lines):
        print(f"L{idx+1} before: {lines[idx].strip()}")
        if r"\end{tabularx}" in lines[idx]:
            lines[idx] = lines[idx].replace(r"\end{tabularx}", r"\end{tabular}")
            print(f"L{idx+1} after: {lines[idx].strip()}")

with open("latex/ch09_computer_architecture.tex", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Fixed mismatches in ch06 and ch09!")
