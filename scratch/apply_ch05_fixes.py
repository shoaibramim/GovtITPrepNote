with open("latex/ch05_dbms_sql.tex", "r", encoding="utf-8") as f:
    ch05 = f.read()

# 1. Names replacement in ch05:
# In student / employee / query examples:
# Rahim -> Shoaib
# Karim -> Ramim
# Hasan -> Tonmoy
# Nabila -> Sifat (Nabila was used alongside Rahim/Karim in student tables)
# Tania -> Hridoy (Tania was used alongside Rahim/Karim in employee tables)
# Sara -> Bappi

# Check L128-131:
ch05_mod = ch05.replace(
    r"\[ \langle 101, \text{'Rahim'}, \text{'CSE'}, 3.75 \rangle \]",
    r"\[ \langle 101, \text{'Shoaib'}, \text{'CSE'}, 3.75 \rangle \]"
)
ch05_mod = ch05_mod.replace(
    r"records complete information for student Rahim.",
    r"records complete information for student Shoaib."
)
ch05_mod = ch05_mod.replace(
    r"(e.g., Rahim's CGPA value \texttt{3.75})",
    r"(e.g., Shoaib's CGPA value \texttt{3.75})"
)

# Table L152 tab:degree_cardinality_example
# 101 & Rahim & CSE & 3.75 \\
# 102 & Karim & EEE & 3.60 \\
# 103 & Nabila & CSE & 3.90 \\
# 104 & Tania & BBA & 3.80 \\
# 105 & Hasan & ME & 3.45 \\
ch05_mod = ch05_mod.replace(r"101 & Rahim & CSE & 3.75 \\", r"101 & Shoaib & CSE & 3.75 \\")
ch05_mod = ch05_mod.replace(r"102 & Karim & EEE & 3.60 \\", r"102 & Ramim & EEE & 3.60 \\")
ch05_mod = ch05_mod.replace(r"103 & Nabila & CSE & 3.90 \\", r"103 & Sifat & CSE & 3.90 \\")
ch05_mod = ch05_mod.replace(r"104 & Tania & BBA & 3.80 \\", r"104 & Hridoy & BBA & 3.80 \\")
ch05_mod = ch05_mod.replace(r"105 & Hasan & ME & 3.45 \\", r"105 & Tonmoy & ME & 3.45 \\")

# L688-691:
ch05_mod = ch05_mod.replace(r"101 & Rahim & 10 & CSE & CSE101 & Programming & A \\", r"101 & Shoaib & 10 & CSE & CSE101 & Programming & A \\")
ch05_mod = ch05_mod.replace(r"101 & Rahim & 10 & CSE & CSE102 & Database & A- \\", r"101 & Shoaib & 10 & CSE & CSE102 & Database & A- \\")
ch05_mod = ch05_mod.replace(r"102 & Karim & 20 & EEE & CSE101 & Programming & B+ \\", r"102 & Ramim & 20 & EEE & CSE101 & Programming & B+ \\")
ch05_mod = ch05_mod.replace(r"103 & Nabila & 10 & CSE & CSE101 & Programming & A \\", r"103 & Sifat & 10 & CSE & CSE101 & Programming & A \\")

ch05_mod = ch05_mod.replace(
    r"student Rahim's name and department are repeated across multiple rows",
    r"student Shoaib's name and department are repeated across multiple rows"
)
ch05_mod = ch05_mod.replace(
    r"Student 102 (Karim) is the sole student enrolled in the \texttt{EEE101} course. If Karim drops out and his record is deleted",
    r"Student 102 (Ramim) is the sole student enrolled in the \texttt{EEE101} course. If Ramim drops out and his record is deleted"
)

# L2011, 2015, 2027, 2029 (MongoDB examples):
ch05_mod = ch05_mod.replace(r'"name": "Rahim"', r'"name": "Shoaib"')
ch05_mod = ch05_mod.replace(r'"email": "rahim@example.com"', r'"email": "shoaib@example.com"')
ch05_mod = ch05_mod.replace(r'db.students.insertOne({ _id: 101, name: "Rahim", department: "CSE", cgpa: 3.75 });',
                            r'db.students.insertOne({ _id: 101, name: "Shoaib", department: "CSE", cgpa: 3.75 });')
ch05_mod = ch05_mod.replace(r'{ _id: 102, name: "Karim", department: "EEE", cgpa: 3.60 }',
                            r'{ _id: 102, name: "Ramim", department: "EEE", cgpa: 3.60 }')

# L2867-2871 (SQL practical questions):
ch05_mod = ch05_mod.replace(r"101 & Rahim & IT & 50000 \\", r"101 & Shoaib & IT & 50000 \\")
ch05_mod = ch05_mod.replace(r"102 & Karim & HR & 45000 \\", r"102 & Ramim & HR & 45000 \\")
ch05_mod = ch05_mod.replace(r"103 & Nabila & Finance & 60000 \\", r"103 & Sifat & Finance & 60000 \\")
ch05_mod = ch05_mod.replace(r"104 & Tania & IT & 55000 \\", r"104 & Hridoy & IT & 55000 \\")
ch05_mod = ch05_mod.replace(r"105 & Hasan & HR & 48000 \\", r"105 & Tonmoy & HR & 48000 \\")

# L3054-3058:
ch05_mod = ch05_mod.replace(r"A table has row: $\langle 101, \text{'Rahim'}, \text{'01711111111, 01822222222'} \rangle$",
                            r"A table has row: $\langle 101, \text{'Shoaib'}, \text{'01711111111, 01822222222'} \rangle$")
ch05_mod = ch05_mod.replace(r"Split into two rows: $\langle 101, \text{'Rahim'}, \text{'01711111111'} \rangle$ and $\langle 101, \text{'Rahim'}, \text{'01822222222'} \rangle$",
                            r"Split into two rows: $\langle 101, \text{'Shoaib'}, \text{'01711111111'} \rangle$ and $\langle 101, \text{'Shoaib'}, \text{'01822222222'} \rangle$")

# L3211-3216:
ch05_mod = ch05_mod.replace(r"101 & Rahim  & 10 & 50,000 \\", r"101 & Shoaib  & 10 & 50,000 \\")
ch05_mod = ch05_mod.replace(r"102 & Karim  & 20 & 45,000 \\", r"102 & Ramim  & 20 & 45,000 \\")
ch05_mod = ch05_mod.replace(r"103 & Nabila & 10 & 60,000 \\", r"103 & Sifat & 10 & 60,000 \\")
ch05_mod = ch05_mod.replace(r"104 & Tania  & 30 & 55,000 \\", r"104 & Hridoy  & 30 & 55,000 \\")
ch05_mod = ch05_mod.replace(r"105 & Hasan  & 20 & 48,000 \\", r"105 & Tonmoy  & 20 & 48,000 \\")
ch05_mod = ch05_mod.replace(r"106 & Sara   & 10 & 70,000 \\", r"106 & Bappi   & 10 & 70,000 \\")

# L3402-3420:
ch05_mod = ch05_mod.replace(r"for student Rahim (ID 101, CSE, CGPA 3.75)", r"for student Shoaib (ID 101, CSE, CGPA 3.75)")
ch05_mod = ch05_mod.replace(r"Update Rahim's CGPA to 3.90 in collection \texttt{students}.", r"Update Shoaib's CGPA to 3.90 in collection \texttt{students}.")

# 2. Fix tables in ch05:
# Table L152: \begin{tabularx}{\textwidth}{c l c c} -> \begin{tabularx}{0.75\textwidth}{c X c c}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{\textwidth}{c l c c}", r"\begin{tabularx}{0.75\textwidth}{c X c c}")

# Table L609: \begin{tabularx}{\textwidth}{l c c c c} -> \begin{tabularx}{\textwidth}{l X X X X}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{\textwidth}{l c c c c}", r"\begin{tabularx}{\textwidth}{l >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}")

# Table L684: \begin{tabularx}{\textwidth}{c l c l c l c} -> \begin{tabularx}{\textwidth}{c X c X c X c}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{\textwidth}{c l c l c l c}", r"\begin{tabularx}{\textwidth}{c X c X c X c}")

# Table L2863: \begin{tabularx}{0.8\textwidth}{c l c c} -> \begin{tabularx}{0.8\textwidth}{c X c c}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{0.8\textwidth}{c l c c}", r"\begin{tabularx}{0.8\textwidth}{c X c c}")

# Table L3207: \begin{tabularx}{\textwidth}{c l c r} -> \begin{tabularx}{0.75\textwidth}{c X c r}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{\textwidth}{c l c r}", r"\begin{tabularx}{0.75\textwidth}{c X c r}")

# Table L3224: \begin{tabularx}{\textwidth}{c l} -> \begin{tabularx}{0.6\textwidth}{c X}
ch05_mod = ch05_mod.replace(r"\begin{tabularx}{\textwidth}{c l}", r"\begin{tabularx}{0.6\textwidth}{c X}")

with open("latex/ch05_dbms_sql.tex", "w", encoding="utf-8") as f:
    f.write(ch05_mod)
print("Updated ch05_dbms_sql.tex successfully!")
