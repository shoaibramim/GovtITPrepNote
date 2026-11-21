with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    log_lines = f.readlines()

for i, line in enumerate(log_lines):
    if "lines 164--164" in line:
        print(f"=== Found lines 164--164 at log line {i+1} ===")
        for j in range(i, max(0, i-500), -1):
            if ".tex" in log_lines[j]:
                print(f"   Context line {j+1}: {log_lines[j].strip()}")
                break
        print("".join(log_lines[i:min(len(log_lines), i+8)]))
