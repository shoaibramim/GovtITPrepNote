with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    ch01 = f.read()

# Replace longtable widths:
# old: \begin{longtable}{r p{9.8cm} p{6.8cm}}
# let's change to: \begin{longtable}{r p{9.2cm} p{6.0cm}}
ch01 = ch01.replace(r"\begin{longtable}{r p{9.8cm} p{6.8cm}}", r"\begin{longtable}{r p{9.2cm} p{6.0cm}}")
with open("latex/ch01_data_structures.tex", "w", encoding="utf-8") as f:
    f.write(ch01)

with open("latex/ch09_computer_architecture.tex", "r", encoding="utf-8") as f:
    ch09 = f.read()

# L513: \begin{tabularx}{\textwidth}{l c l X}
# "Behavioral Logic Condition" header and equations: let's give X to description:
# \begin{tabularx}{\textwidth}{l c X l}
ch09 = ch09.replace(r"\begin{tabularx}{\textwidth}{l c l X}", r"\begin{tabularx}{\textwidth}{l c X l}")

# L621: \begin{tabularx}{0.65\textwidth}{X c c} -> headers:
# Target Logic Function & Minimum 2-Input NAND Gates & Minimum 2-Input NOR Gates
# Notice: "Minimum 2-Input NAND Gates" is long! In 0.65\textwidth, columns are narrow!
# If width is \textwidth or 0.85\textwidth:
ch09 = ch09.replace(r"\begin{tabularx}{0.65\textwidth}{X c c}", r"\begin{tabularx}{0.85\textwidth}{X >{\centering\arraybackslash}p{4cm} >{\centering\arraybackslash}p{4cm}}")

with open("latex/ch09_computer_architecture.tex", "w", encoding="utf-8") as f:
    f.write(ch09)

print("Applied adjustments to ch01 and ch09!")
