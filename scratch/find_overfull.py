with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

overfull_boxes = []
for i, line in enumerate(lines):
    if "Overfull \\hbox" in line:
        context = "".join(lines[i:min(len(lines), i+6)])
        overfull_boxes.append(context)

print(f"Total Overfull \\hbox found: {len(overfull_boxes)}")

# Filter for large overfull boxes (e.g. > 15pt or > 20pt or tables)
large_overfull = []
for ob in overfull_boxes:
    # extract pt
    import re
    m = re.search(r'Overfull \\hbox \(([0-9\.]+)pt too wide\)', ob)
    if m:
        pts = float(m.group(1))
        if pts > 15.0:
            large_overfull.append((pts, ob))

large_overfull.sort(key=lambda x: x[0], reverse=True)
print(f"Overfull > 15pt count: {len(large_overfull)}")
for pts, ob in large_overfull[:25]:
    print(f"\n--- {pts}pt too wide ---")
    print(ob.strip())
