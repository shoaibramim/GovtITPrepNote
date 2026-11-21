# Update ch02
with open("latex/ch02_algorithms.tex", "r", encoding="utf-8") as f:
    ch02 = f.read()

# 1. Names replacement in ch02:
# L73-74:
# 1 & Rahim  & 85 \\
# 2 & Karim  & 92 \\
# Stable / unstable results:
# Nabila (78) -> Rahim (85) -> Salma (85) -> Karim (92)
# Question: Input records: (Rahim, 80), (Karim, 90), (Salma, 80)
# Let's replace Rahim with Shoaib, and Karim with Ramim!
# (Salma and Nabila can remain or stay, but Rahim and Karim are replaced)

ch02_mod = ch02.replace(r"1 & Rahim  & 85 \\", r"1 & Shoaib & 85 \\")
ch02_mod = ch02_mod.replace(r"2 & Karim  & 92 \\", r"2 & Ramim  & 92 \\")
ch02_mod = ch02_mod.replace(r"\textbf{Rahim (85)}", r"\textbf{Shoaib (85)}")
ch02_mod = ch02_mod.replace(r"\text{Karim (92)}", r"\text{Ramim (92)}")
ch02_mod = ch02_mod.replace(r"Rahim appears before Salma because Rahim preceded Salma", r"Shoaib appears before Salma because Shoaib preceded Salma")
ch02_mod = ch02_mod.replace(r"Salma is placed ahead of Rahim, reversing their input chronology", r"Salma is placed ahead of Shoaib, reversing their input chronology")
ch02_mod = ch02_mod.replace(r"(\text{Rahim}, 80), (\text{Karim}, 90)", r"(\text{Shoaib}, 80), (\text{Ramim}, 90)")
ch02_mod = ch02_mod.replace(r"(\text{Rahim}, 80), (\text{Salma}, 80), (\text{Karim}, 90)", r"(\text{Shoaib}, 80), (\text{Salma}, 80), (\text{Ramim}, 90)")
ch02_mod = ch02_mod.replace(r"(\text{Salma}, 80), (\text{Rahim}, 80), (\text{Karim}, 90)", r"(\text{Salma}, 80), (\text{Shoaib}, 80), (\text{Ramim}, 90)")
ch02_mod = ch02_mod.replace(r"\textbf{Answer: Option A is stable.} Rahim appeared before Salma", r"\textbf{Answer: Option A is stable.} Shoaib appeared before Salma")

# 2. Fix L734 table in ch02:
# \begin{tabularx}{\textwidth}{p{3.2cm} p{1.8cm} p{1.8cm} p{1.8cm} p{2.6cm} c c}
# Notice this has no X column! Let's make it:
# \begin{tabularx}{\textwidth}{l c c c X c c} or keep widths with X
# Let's check the columns: Algorithm, Best Time, Average Time, Worst Time, Auxiliary Space, Stable?, In-Place?
# If we use: \begin{tabularx}{\textwidth}{l c c c X c c}
old_tab_ch02 = r"\begin{tabularx}{\textwidth}{p{3.2cm} p{1.8cm} p{1.8cm} p{1.8cm} p{2.6cm} c c}"
new_tab_ch02 = r"\begin{tabularx}{\textwidth}{l c c c X c c}"
ch02_mod = ch02_mod.replace(old_tab_ch02, new_tab_ch02)

# Also fix L4116 in ch02:
# \begin{tabularx}{\textwidth}{p{5.5cm} c c}
old_tab_ch02_2 = r"\begin{tabularx}{\textwidth}{p{5.5cm} c c}"
new_tab_ch02_2 = r"\begin{tabularx}{\textwidth}{X c c}"
ch02_mod = ch02_mod.replace(old_tab_ch02_2, new_tab_ch02_2)

with open("latex/ch02_algorithms.tex", "w", encoding="utf-8") as f:
    f.write(ch02_mod)
print("Updated ch02_algorithms.tex!")
