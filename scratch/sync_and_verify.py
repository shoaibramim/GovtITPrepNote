import shutil
import hashlib
import os

main_pdf = "latex/main.pdf"
target_pdf = "GovtITPrepNote.pdf"

# Copy main.pdf to GovtITPrepNote.pdf
shutil.copy2(main_pdf, target_pdf)

def get_hash_and_size(path):
    size = os.path.getsize(path)
    with open(path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    return size, h

s1, h1 = get_hash_and_size(main_pdf)
s2, h2 = get_hash_and_size(target_pdf)

print(f"main.pdf: size={s1}, sha256={h1}")
print(f"{target_pdf}: size={s2}, sha256={h2}")
assert s1 == s2 and h1 == h2, "PDF mismatch!"
print(f"Successfully synchronized {target_pdf} with latex/main.pdf!")
