# Fix ch07
with open("latex/ch07_software_engineering.tex", "r", encoding="utf-8") as f:
    ch07 = f.read()

# 1. Replace L199 in ch07:
# \begin{tabularx}{\textwidth}{l p{4cm} p{3.5cm} l c} -> \begin{tabularx}{\textwidth}{l X X l c}
ch07 = ch07.replace(r"\begin{tabularx}{\textwidth}{l p{4cm} p{3.5cm} l c}", r"\begin{tabularx}{\textwidth}{l X X l c}")

# 2. Replace L1277 in ch07:
# \begin{tabularx}{\textwidth}{l p{5cm} c c c c} -> \begin{tabularx}{\textwidth}{l X c c c c}
ch07 = ch07.replace(r"\begin{tabularx}{\textwidth}{l p{5cm} c c c c}", r"\begin{tabularx}{\textwidth}{l X c c c c}")

# 3. Replace L2340 in ch07 (tabular that overflows):
# \begin{tabular}{p{3.5cm}p{5.5cm}p{3cm}p{3cm}} -> tabularx:
# \begin{tabularx}{\textwidth}{p{2.5cm} X p{3cm} p{3.5cm}}
old_tab_2340 = r"\begin{tabular}{p{3.5cm}p{5.5cm}p{3cm}p{3cm}}"
new_tab_2340 = r"\begin{tabularx}{\textwidth}{p{2.5cm} X p{3.2cm} p{3.8cm}}"

if old_tab_2340 in ch07:
    ch07 = ch07.replace(old_tab_2340, new_tab_2340)
    # Also replace \end{tabular} with \end{tabularx} at L2351
    # Check context:
    ch07 = ch07.replace(r"""Age = -5, Age = "abc" \\
\bottomrule
\end{tabular}
\end{center}""", r"""Age = -5, Age = "abc" \\
\bottomrule
\end{tabularx}
\end{center}""")
    print("Fixed L2340 table in ch07!")
else:
    print("Could not find old_tab_2340 in ch07")

with open("latex/ch07_software_engineering.tex", "w", encoding="utf-8") as f:
    f.write(ch07)

# Fix ch08
with open("latex/ch08_cloud_ml.tex", "r", encoding="utf-8") as f:
    ch08 = f.read()

# Fix L89 in ch08 (Service model stack table in tcolorbox):
# \begin{tabular}{|l|c|c|c|c|}
# Change to tabularx or add \small \setlength{\tabcolsep}{4pt}
old_tab_ch08 = r"\begin{tabular}{|l|c|c|c|c|}"
new_tab_ch08 = r"\setlength{\tabcolsep}{4.5pt}\begin{tabularx}{\linewidth}{|X|c|c|c|c|}"

if old_tab_ch08 in ch08:
    ch08 = ch08.replace(old_tab_ch08, new_tab_ch08)
    ch08 = ch08.replace(r"""Facility Physical Security & \textbf{Customer} & CSP & CSP & CSP \\
\hline
\end{tabular}
\end{center}
\end{tcolorbox}""", r"""Facility Physical Security & \textbf{Customer} & CSP & CSP & CSP \\
\hline
\end{tabularx}
\end{center}
\end{tcolorbox}""")
    print("Fixed L89 table in ch08!")

with open("latex/ch08_cloud_ml.tex", "w", encoding="utf-8") as f:
    f.write(ch08)

# Fix ch09
with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    ch09 = f.read()

# Fix tabularx without X in ch09:
# L308: \begin{tabularx}{\textwidth}{l c c c} -> \begin{tabularx}{0.75\textwidth}{X c c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{l c c c}", r"\begin{tabularx}{0.75\textwidth}{X c c c}")

# L464: \begin{tabularx}{\textwidth}{c c c c c c c c} -> \begin{tabularx}{0.85\textwidth}{c c c c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{c c c c c c c c}", r"\begin{tabularx}{0.85\textwidth}{c c c c c c c c}")

# L533: \begin{tabularx}{\textwidth}{c c c c c c c c} -> \begin{tabularx}{0.85\textwidth}{c c c c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{c c c c c c c c}", r"\begin{tabularx}{0.85\textwidth}{c c c c c c c c}")

# L621: \begin{tabularx}{\textwidth}{l c c} -> \begin{tabularx}{0.65\textwidth}{X c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{l c c}", r"\begin{tabularx}{0.65\textwidth}{X c c}")

# L687: \begin{tabularx}{0.6\textwidth}{c c c c} -> \begin{tabular}{c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{0.6\textwidth}{c c c c}", r"\begin{tabular}{c c c c}")
# L687 end:
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Half Adder Truth Table}""", r"""\bottomrule
\end{tabular}
\caption{Half Adder Truth Table}""")

# L723: \begin{tabularx}{0.7\textwidth}{c c c c c} -> \begin{tabular}{c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{0.7\textwidth}{c c c c c}", r"\begin{tabular}{c c c c c}")
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Full Adder Truth Table}""", r"""\bottomrule
\end{tabular}
\caption{Full Adder Truth Table}""")

# L869: \begin{tabularx}{\textwidth}{c c c c c c c} -> \begin{tabular}{c c c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{c c c c c c c}", r"\begin{tabular}{c c c c c c c}")
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Truth Table for 4-to-2 Priority Encoder}""", r"""\bottomrule
\end{tabular}
\caption{Truth Table for 4-to-2 Priority Encoder}""")

# L1269: \begin{tabularx}{\textwidth}{c c c c c c c c} -> \begin{tabular}{c c c c c c c c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{c c c c c c c c}", r"\begin{tabular}{c c c c c c c c}")
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Master Excitation Table for All Flip-Flops}""", r"""\bottomrule
\end{tabular}
\caption{Master Excitation Table for All Flip-Flops}""")

# L1563: \begin{tabularx}{\textwidth}{l l l c} -> \begin{tabularx}{\textwidth}{l X X c}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{l l l c}", r"\begin{tabularx}{\textwidth}{l X X c}")

# L2522: \begin{tabularx}{0.7\textwidth}{c c c} -> \begin{tabular}{c c c}
ch09 = ch09.replace(r"\begin{tabularx}{0.7\textwidth}{c c c}", r"\begin{tabular}{c c c}")
ch09 = ch09.replace(r"""\bottomrule
\end{tabularx}
\caption{Memory Layout for 32-bit Integer \texttt{0x12345678}}""", r"""\bottomrule
\end{tabular}
\caption{Memory Layout for 32-bit Integer \texttt{0x12345678}}""")

with open("latex/ch09_computer_architecture.tex", "w", encoding="utf-8") as f:
    f.write(ch09)

# Fix ch10
with open("latex/ch10_electronics_hardware.tex", "r", encoding="utf-8") as f:
    ch10 = f.read()

# Fix L1826: \begin{tabularx}{\linewidth}{c l l l} -> \begin{tabularx}{\linewidth}{c X X l}
ch10 = ch10.replace(r"\begin{tabularx}{\linewidth}{c l l l}", r"\begin{tabularx}{\linewidth}{c X X l}")

# Fix L2388 (93.6pt overflow!): \begin{tabularx}{\linewidth}{l l l l} -> \begin{tabularx}{\linewidth}{l c c X}
ch10 = ch10.replace(r"\begin{tabularx}{\linewidth}{l l l l}", r"\begin{tabularx}{\linewidth}{l c c X}")

with open("latex/ch10_electronics_hardware.tex", "w", encoding="utf-8") as f:
    f.write(ch10)

# Fix ch11
with open("latex/ch11_programming.tex", "r", encoding="utf-8") as f:
    ch11 = f.read()

# Fix L1227: \begin{tabularx}{\textwidth}{l l l l l l} -> \begin{tabularx}{\textwidth}{l X X X X c}
ch11 = ch11.replace(r"\begin{tabularx}{\textwidth}{l l l l l l}", r"\begin{tabularx}{\textwidth}{l X X X X c}")

with open("latex/ch11_programming.tex", "w", encoding="utf-8") as f:
    f.write(ch11)

# Fix chapter3_banking
with open("latex/chapter3_banking.tex", "r", encoding="utf-8") as f:
    ch3b = f.read()

# Fix L478: \begin{tabular}{|l|p{3.8cm}|p{3.8cm}|p{4.2cm}|}
# Width was 17.5cm (margins 1.5cm left/right leaves 18.0cm). But padding caused overflow!
old_tab_ch3b = r"\begin{tabular}{|l|p{3.8cm}|p{3.8cm}|p{4.2cm}|}"
new_tab_ch3b = r"\begin{tabularx}{\textwidth}{|l|X|X|X|}"
if old_tab_ch3b in ch3b:
    ch3b = ch3b.replace(old_tab_ch3b, new_tab_ch3b)
    ch3b = ch3b.replace(r"""ATM withdrawals, POS card swipes, instant app-to-app fund transfers. \\
\hline
\end{tabular}
\end{table}""", r"""ATM withdrawals, POS card swipes, instant app-to-app fund transfers. \\
\hline
\end{tabularx}
\end{table}""")
    print("Fixed L478 table in chapter3_banking!")

with open("latex/chapter3_banking.tex", "w", encoding="utf-8") as f:
    f.write(ch3b)

print("Applied table fixes across ch07, ch08, ch09, ch10, ch11, and chapter3_banking!")
