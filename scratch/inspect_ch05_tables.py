with open("latex/ch05_dbms_sql.tex", "r", encoding="utf-8") as f: ch05 = f.read()

# Let's inspect L150-165, L685-695, L2860-2875, L3210-3220
lines = ch05.splitlines()
for l in [155, 687, 2865, 3210]:
    print(f"--- Around L{l} ---")
    for i in range(max(0, l-3), min(len(lines), l+8)):
        print(f"L{i+1}: {lines[i]}")
