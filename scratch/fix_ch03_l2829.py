with open("latex/ch03_networking_subnetting.tex", "r", encoding="utf-8") as f:
    ch03 = f.read()

# Make tab:digital_modulation_symbols a clean tabularx with centered X columns or appropriate column widths
old_tab_2829 = r"""\begin{tabular}{ccc}
\toprule
\textbf{Modulation Scheme} & \textbf{Number of Constellation Symbols ($M$)} & \textbf{Spectral Efficiency ($\text{Bits/Symbol} = \log_2 M$)} \\"""

new_tab_2829 = r"""\begin{tabularx}{0.85\textwidth}{>{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Modulation Scheme} & \textbf{Number of Constellation Symbols ($M$)} & \textbf{Spectral Efficiency ($\text{Bits/Symbol} = \log_2 M$)} \\"""

if old_tab_2829 in ch03:
    ch03 = ch03.replace(old_tab_2829, new_tab_2829)
    ch03 = ch03.replace(r"""\bottomrule
\end{tabular}
\end{table}
Example:""", r"""\bottomrule
\end{tabularx}
\end{table}
Example:""")
    with open("latex/ch03_networking_subnetting.tex", "w", encoding="utf-8") as f:
        f.write(ch03)
    print("Fixed L2829 table in ch03!")
else:
    print("Could not find exact old_tab_2829")
