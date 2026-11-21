import re
from collections import Counter

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

# Let's search for names commonly used in examples, DBMS queries, networks/security, etc.
# Also let's inspect SQL statements: 'INSERT INTO', 'VALUES', etc.
common_names = [
    "Alice", "Bob", "Charlie", "Dave", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan",
    "Judy", "Mallory", "Oscar", "Peggy", "Sybil", "Trent", "Trudy", "Victor", "Walter",
    "John", "Jane", "Smith", "Doe", "Rahim", "Karim", "Kamal", "Jamal", "Tanvir", "Hasan",
    "Ahmed", "Ali", "Fatima", "Ayesha", "Sultana", "Kavita", "Rahul", "Priya", "Amit", "Rohit",
    "Arun", "Suresh", "Ramesh", "Anil", "Sunil", "Rajesh", "Pooja", "Neha", "Sneha", "Vikram",
    "Tom", "Jerry", "Mark", "Steve", "Bill", "Elon", "Mary", "Peter", "Paul"
]

pattern = re.compile(r'\b(' + '|'.join(common_names) + r')\b', re.IGNORECASE)

print("=== COMMON NAMES FOUND ===")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    matches = pattern.findall(text)
    if matches:
        counts = Counter(matches)
        print(fpath, dict(counts))

# Also search for 'name' or 'Name' in quotes or single quotes in SQL / examples
sql_name_pattern = re.compile(r"['\"]([A-Z][a-z]+)['\"]")
print("\n=== POTENTIAL NAMES IN QUOTES (SQL / CODE) ===")
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    found = []
    for line in lines:
        if any(k in line.lower() for k in ["insert into", "values", "employee", "student", "customer", "user", "name =", "name="]):
            m = sql_name_pattern.findall(line)
            if m:
                found.extend(m)
    if found:
        print(fpath, set(found))
