with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

errors = []
for i, line in enumerate(lines):
    if line.startswith("!"):
        ctx = "".join(lines[i:min(len(lines), i+10)])
        errors.append(ctx)

print(f"Total LaTeX errors: {len(errors)}")
for err in errors:
    print(err)
    print("="*40)
