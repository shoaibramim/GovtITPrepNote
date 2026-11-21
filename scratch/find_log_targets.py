# Find which files lines 525 and 633 belong to
with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    log_lines = f.readlines()

for target in ["lines 525--525", "lines 633--633"]:
    for i, line in enumerate(log_lines):
        if target in line:
            print(f"=== Found {target} at line {i+1} ===")
            # Look backwards for the most recently entered .tex file
            for j in range(i, max(0, i-500), -1):
                if ".tex" in log_lines[j]:
                    print(f"   Context line {j+1}: {log_lines[j].strip()}")
                    break
