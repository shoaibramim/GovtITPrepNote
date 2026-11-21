with open("latex/ch06_operating_system.tex", "r", encoding="utf-8") as f:
    ch06 = f.read()

# Replace alice with shoaib in setfacl example
ch06_mod = ch06.replace(r"\texttt{setfacl -m u:alice:rw financial\_report.xlsx}",
                        r"\texttt{setfacl -m u:shoaib:rw financial\_report.xlsx}")

# Fix availability table L1184 (99.0% nines table):
# Lines 1184--1195 in ch06:
# \begin{tabular}{l l l l}
# \textbf{Availability ("Nines")} & \textbf{Availability Fraction} & \textbf{Downtime per Year (365 d)} & \textbf{Downtime per Month (30 d)} \\
old_tab_os = r"""\begin{tabular}{l l l l}
\toprule
\textbf{Availability ("Nines")} & \textbf{Availability Fraction} & \textbf{Downtime per Year (365 d)} & \textbf{Downtime per Month (30 d)} \\"""

new_tab_os = r"""\begin{tabularx}{\textwidth}{l c >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Availability ("Nines")} & \textbf{Availability Fraction} & \textbf{Downtime per Year (365 d)} & \textbf{Downtime per Month (30 d)} \\"""

if old_tab_os in ch06_mod:
    ch06_mod = ch06_mod.replace(old_tab_os, new_tab_os)
    ch06_mod = ch06_mod.replace(r"""\bottomrule
\end{tabular}
\end{table}

\subsection{Multicore CPU Scaling""", r"""\bottomrule
\end{tabularx}
\end{table}

\subsection{Multicore CPU Scaling""")
    print("Replaced L1184 table in ch06!")
else:
    print("Could not find exact old_tab_os in ch06")

with open("latex/ch06_operating_system.tex", "w", encoding="utf-8") as f:
    f.write(ch06_mod)
print("Updated ch06_operating_system.tex successfully!")
