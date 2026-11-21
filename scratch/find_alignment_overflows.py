with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
# Look for Overfull \hbox in alignment
alignment_overflows = re.findall(r'Overfull \\hbox \(([0-9\.]+)pt too wide\) in alignment at lines (\d+)--(\d+)', text)
print(f"Alignment overflows: {len(alignment_overflows)}")
for pts, l1, l2 in alignment_overflows:
    print(f"   {pts} pt at lines {l1}--{l2}")
