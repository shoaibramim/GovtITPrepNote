with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    ch09 = f.read()

# L156: \begin{tabularx}{\textwidth}{l c X l}
# Notice: Functional Responsibility was in 'l', so that huge sentence didn't wrap!
# And Typical Width was in 'X'!
# We should change spec to:
# \begin{tabularx}{\textwidth}{l c c X} or \begin{tabularx}{\textwidth}{p{2.5cm} p{3.2cm} p{3cm} X}
old_tab_156 = r"\begin{tabularx}{\textwidth}{l c X l}"
new_tab_156 = r"\begin{tabularx}{\textwidth}{l >{\centering\arraybackslash}p{3.2cm} >{\centering\arraybackslash}p{2.8cm} X}"

if old_tab_156 in ch09:
    ch09 = ch09.replace(old_tab_156, new_tab_156)
    with open("latex/ch09_computer_architecture.tex", "w", encoding="utf-8") as f:
        f.write(ch09)
    print("Fixed L156 in ch09!")
else:
    print("Could not find old_tab_156")
