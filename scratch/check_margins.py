import re

files = [
    "latex/ch01_data_structures.tex",
    "latex/ch02_algorithms.tex",
    "latex/ch03_networking_subnetting.tex",
    "latex/ch04_cybersecurity.tex",
    "latex/ch05_dbms_sql.tex",
    "latex/ch06_operating_system.tex",
    "latex/ch07_software_engineering.tex",
    "latex/ch08_cloud_ml.tex",
    "latex/ch09_computer_architecture.tex",
    "latex/ch10_electronics_hardware.tex",
    "latex/ch11_programming.tex",
    "latex/chapter1_location.tex",
    "latex/chapter2_technical.tex",
    "latex/chapter3_banking.tex"
]

print("=== CHECKING ALL TABULAR / TABULARX COLUMNS AND WIDTHS ===")

# We want to identify every table that exceeds textwidth (approx 16-17cm)
# In LaTeX, \textwidth for a4paper with geometry margins (say 1in/2.5cm or 0.75in):
# Let's check geometry in main.tex
with open("latex/main.tex", "r", encoding="utf-8") as f:
    main_tex = f.read()

for line in main_tex.splitlines():
    if "geometry" in line:
        print("Geometry:", line)

