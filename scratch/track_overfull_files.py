with open("latex/main.log", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

current_file = "main.tex"
file_stack = ["main.tex"]

overfull_with_file = []

import re
file_enter_regex = re.compile(r'\((?:[a-zA-Z]:[\\/][^\)]+|[^\(\)\s]+\.tex|[^\(\)\s]+\.sty|[^\(\)\s]+\.def)')

# Let's track line by line
for line_idx, line in enumerate(lines):
    # check for open parens with filename
    # XeTeX outputs filenames like (./ch01_data_structures.tex or (ch01_data_structures.tex
    matches = re.findall(r'\(([^\(\)\s\n]+\.tex)', line)
    for m in matches:
        file_stack.append(m)
    # Check closing parens count
    # Note: simple paren matching can be noisy, but let's see
    if "Overfull \\hbox" in line:
        # extract pts
        m_pts = re.search(r'Overfull \\hbox \(([0-9\.]+)pt too wide\)', line)
        pts = float(m_pts.group(1)) if m_pts else 0.0
        # get line number from log
        m_line = re.search(r'lines? (\d+)', line)
        if not m_line:
            # check next lines
            for next_l in lines[line_idx+1:line_idx+4]:
                m_line = re.search(r'lines? (\d+)', next_l)
                if m_line:
                    break
        log_line_no = m_line.group(1) if m_line else "unknown"
        # look at context
        ctx = "".join(lines[line_idx:min(len(lines), line_idx+5)])
        current = file_stack[-1] if file_stack else "unknown"
        overfull_with_file.append((pts, current, log_line_no, ctx))

print(f"Total overfull recorded: {len(overfull_with_file)}")
# Sort by pts
overfull_with_file.sort(key=lambda x: x[0], reverse=True)
for pts, f, l, ctx in overfull_with_file[:40]:
    if pts > 20.0:
        print(f"[{pts} pt] File: {f} (around line {l})")
        print(ctx.strip())
        print("-" * 50)
