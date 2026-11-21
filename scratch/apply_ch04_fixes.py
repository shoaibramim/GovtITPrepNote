with open("latex/ch04_cybersecurity.tex", "r", encoding="utf-8") as f:
    ch04 = f.read()

# 1. Names replacement in ch04:
# Alice & Bob in asymmetric encryption example (L630, L678-681) -> Tareq & Zunaeed
# Alice & Bob in RSA & digital signature exam questions (L6479-6493) -> Tonmoy & Likhon

# L630:
ch04_mod = ch04.replace(
    r"\textbf{Example:} Alice and Bob share a secret key. Alice encrypts a message using that key, and Bob uses the same key to decrypt it.",
    r"\textbf{Example:} Tareq and Zunaeed share a secret key. Tareq encrypts a message using that key, and Zunaeed uses the same key to decrypt it."
)

# L678-681:
ch04_mod = ch04_mod.replace(
    r"\item Bob shares his public key with Alice.",
    r"\item Zunaeed shares his public key with Tareq."
)
ch04_mod = ch04_mod.replace(
    r"\item Alice encrypts a message using Bob's public key.",
    r"\item Tareq encrypts a message using Zunaeed's public key."
)
ch04_mod = ch04_mod.replace(
    r"\item Alice sends the ciphertext to Bob.",
    r"\item Tareq sends the ciphertext to Zunaeed."
)
ch04_mod = ch04_mod.replace(
    r"\item Bob decrypts it using his private key.",
    r"\item Zunaeed decrypts it using his private key."
)

# L6479-6486:
ch04_mod = ch04_mod.replace(
    r"Alice wishes to transmit a confidential encrypted message to Bob using RSA. Which key must Alice use for encryption, and which key must Bob use for decryption?",
    r"Tonmoy wishes to transmit a confidential encrypted message to Likhon using RSA. Which key must Tonmoy use for encryption, and which key must Likhon use for decryption?"
)
ch04_mod = ch04_mod.replace(
    r"\item Alice encrypts using \textbf{Bob's Public Key} ($K_{\text{pub-Bob}}$).",
    r"\item Tonmoy encrypts using \textbf{Likhon's Public Key} ($K_{\text{pub-Likhon}}$)."
)
ch04_mod = ch04_mod.replace(
    r"\item Bob decrypts using \textbf{Bob's Private Key} ($K_{\text{priv-Bob}}$).",
    r"\item Likhon decrypts using \textbf{Likhon's Private Key} ($K_{\text{priv-Likhon}}$)."
)
ch04_mod = ch04_mod.replace(
    r"\[ \boxed{\text{\textbf{Encryption: Bob's Public Key; Decryption: Bob's Private Key}}} \]",
    r"\[ \boxed{\text{\textbf{Encryption: Likhon's Public Key; Decryption: Likhon's Private Key}}} \]"
)

# L6490-6493:
ch04_mod = ch04_mod.replace(
    r"Alice digitally signs a legal government contract using her private key and transmits the contract and signature to Bob. Which key does Bob use to verify Alice's signature?",
    r"Tonmoy digitally signs a legal government contract using his private key and transmits the contract and signature to Likhon. Which key does Likhon use to verify Tonmoy's signature?"
)
ch04_mod = ch04_mod.replace(
    r"\item \textbf{Solution:} Bob verifies the signature using \textbf{Alice's Public Key} ($K_{\text{pub-Alice}}$).",
    r"\item \textbf{Solution:} Likhon verifies the signature using \textbf{Tonmoy's Public Key} ($K_{\text{pub-Tonmoy}}$)."
)
ch04_mod = ch04_mod.replace(
    r"\[ \boxed{\text{\textbf{Alice's Public Key}}} \]",
    r"\[ \boxed{\text{\textbf{Tonmoy's Public Key}}} \]"
)

# 2. Fix L4163 in ch04 (AES specs table):
# \begin{tabularx}{\textwidth}{l c c c c}
# Notice this table was 140.89pt overfull!
# Columns: AES Variant | Key Size (bits / bytes) | Block Size (bits / bytes) | Number of Rounds | Round Key Size
# If we use: \begin{tabularx}{\textwidth}{l X X c X} with centered/left wrapped columns:
old_aes_tab = r"\begin{tabularx}{\textwidth}{l c c c c}"
new_aes_tab = r"\begin{tabularx}{\textwidth}{l >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
ch04_mod = ch04_mod.replace(old_aes_tab, new_aes_tab)

with open("latex/ch04_cybersecurity.tex", "w", encoding="utf-8") as f:
    f.write(ch04_mod)
print("Updated ch04_cybersecurity.tex successfully!")
