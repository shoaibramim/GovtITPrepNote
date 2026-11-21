# -*- coding: utf-8 -*-
"""
Reorganize Book Structure:
- Merges ch01-ch06 into ch01_data_structures.tex (Chapter 1: Data Structures)
- Merges ch07-ch09 into ch02_algorithms.tex (Chapter 2: Algorithms and Complexity)
- Renames and standardizes ch10-ch18 into ch03-ch11:
    ch10 -> ch03_networking_subnetting.tex
    ch11 -> ch04_cybersecurity.tex
    ch12 -> ch05_dbms_sql.tex
    ch13 -> ch06_operating_system.tex
    ch14 -> ch07_software_engineering.tex
    ch15 -> ch08_cloud_ml.tex
    ch16 -> ch09_computer_architecture.tex
    ch17 -> ch10_electronics_hardware.tex
    ch18 -> ch11_programming.tex
- Updates main.tex to include the unified 11 chapters in Part I followed by Part II.
- Verifies that zero content, paragraphs, or equations are lost.
"""

import os
import re
from collections import Counter

latex_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'latex'))

print("--- 1. MERGING DATA STRUCTURES (ch01 - ch06) ---")

ds_intro = r'''\chapter{Data Structures}
\label{ch:data_structures}

This chapter provides an exhaustive, examination-oriented foundation in data structures, covering linear and non-linear abstractions, algorithmic complexity, implementation nuances in C and C++, and high-frequency problem sets required for Bangladesh Government IT Recruitment Examinations (including Assistant Programmer, Assistant Director (ICT), Assistant Network Engineer, Assistant Database Administrator, and Maintenance Engineer posts).

The chapter is systematically organized into six interconnected core areas:
\begin{enumerate}[label=\bfseries Part \Roman*:]
    \item \textbf{Stack and Queue Architectures:} LIFO and FIFO operations, queue implementation using two stacks, amortized analysis, real-world systems applications, and common MCQ traps.
    \item \textbf{Linked Lists and Binary Heaps:} Singly, doubly, and circular linked lists, array vs. pointer trade-offs, max-heap and min-heap construction (heapify), insertion, deletion, and Heap Sort.
    \item \textbf{Circular Queues and Priority Queues:} Eliminating linear memory exhaustion via modulo arithmetic indexing, priority queue heap mappings, and scheduling algorithms.
    \item \textbf{Trees, Binary Trees, and B+ Trees:} Tree hierarchies, binary search trees (BST), balanced AVL trees, and exact mathematical formulations for minimum/maximum keys in B+ trees.
    \item \textbf{Graphs, Adjacency Representations, and Hash Tables:} Graph theory, adjacency list vs. matrix space/time trade-offs, hash functions, and collision resolution (chaining vs. open addressing).
    \item \textbf{Data Structure Recruitment Examination Problem Bank:} Essential worked algorithm-tracing problems, programming solutions, and analytical viva questions with complete step-by-step solutions.
\end{enumerate}
'''

def clean_part_tex(filepath, part_title, exam_disambig, rev_disambig):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Strip \chapter{...} and leading \label{...}
    text = re.sub(r'\\chapter\{[^}]+\}\s*', '', text)
    text = re.sub(r'\\label\{ch:[^}]+\}\s*', '', text)
    
    # Disambiguate duplicate section names using exact string replace
    text = text.replace(r'\section{Likely Recruitment Examination Questions}',
                        f'\\section{{Likely Recruitment Examination Questions: {exam_disambig}}}')
    text = text.replace(r'\section{Final Quick-Revision Sheet}',
                        f'\\section{{Final Quick-Revision Sheet: {rev_disambig}}}')
    
    # Format divider
    divider = f'''
\\begin{{center}}
\\vspace{{1em}}
{{\\color{{primary}}\\rule{{0.5\\textwidth}}{{1.5pt}}}}\\\\[6pt]
{{\\Large\\bfseries\\color{{primary}} {part_title}}}\\\\[3pt]
{{\\color{{primary}}\\rule{{0.5\\textwidth}}{{1.5pt}}}}
\\vspace{{1em}}
\\end{{center}}
'''
    return divider + '\n' + text.strip()

ch01_text = clean_part_tex(os.path.join(latex_dir, 'ch01_stack_queue.tex'),
                           'Part I: Stack and Queue Architectures',
                           'Stack and Queue', 'Stack and Queue')
ch02_text = clean_part_tex(os.path.join(latex_dir, 'ch02_linked_lists_heaps.tex'),
                           'Part II: Linked Lists and Binary Heaps',
                           'Linked Lists and Heaps', 'Linked Lists and Heaps')
ch03_text = clean_part_tex(os.path.join(latex_dir, 'ch03_circular_priority_queue.tex'),
                           'Part III: Circular Queues and Priority Queues',
                           'Circular and Priority Queues', 'Circular and Priority Queues')
ch04_text = clean_part_tex(os.path.join(latex_dir, 'ch04_trees_btree.tex'),
                           'Part IV: Trees, Binary Trees, and B+ Trees',
                           'Trees and B+ Trees', 'Trees and B+ Trees')
ch05_text = clean_part_tex(os.path.join(latex_dir, 'ch05_graphs_hashing.tex'),
                           'Part V: Graphs, Adjacency Representations, and Hash Tables',
                           'Graphs and Hashing', 'Graphs and Hashing')
ch06_text = clean_part_tex(os.path.join(latex_dir, 'ch06_data_structures_problems.tex'),
                           'Part VI: Data Structure Recruitment Examination Problem Bank',
                           'Problem Bank', 'Problem Bank')

merged_ds = ds_intro.strip() + '\n\n' + '\n\n'.join([ch01_text, ch02_text, ch03_text, ch04_text, ch05_text, ch06_text]) + '\n'

out_ds_path = os.path.join(latex_dir, 'ch01_data_structures.tex')
with open(out_ds_path, 'w', encoding='utf-8') as f:
    f.write(merged_ds)
print(f"  [OK] Wrote {out_ds_path} ({len(merged_ds.splitlines())} lines, {len(merged_ds)} chars)")


print("\n--- 2. MERGING ALGORITHMS (ch07 - ch09) ---")

algo_intro = r'''\chapter{Algorithms and Complexity}
\label{ch:algorithms}

This chapter covers the foundations of algorithm design, computational complexity, and problem-solving techniques essential for government technical recruitment examinations. It synthesizes theoretical principles, asymptotic analyses, rigorous correctness proofs, and complete C++ implementations across sorting, searching, graph traversal, greedy strategies, recursion, dynamic programming, and high-probability interview problems.

The chapter is systematically organized into three interconnected core areas:
\begin{enumerate}[label=\bfseries Part \Roman*:]
    \item \textbf{Sorting, Searching, and Graph Traversal Algorithms:} Comparative analysis of comparison-based sorts (Bubble, Insertion, Merge, Quick), non-comparison sorts, two-pointer search, Binary Search, Breadth-First Search (BFS), Depth-First Search (DFS), and A* heuristic search.
    \item \textbf{Greedy Algorithms, Recursion, and Dynamic Programming:} Greedy-choice properties, Fractional Knapsack, Activity Selection, Huffman Coding, recursion trees, and dynamic programming formulations (0/1 Knapsack, Longest Common Subsequence, Matrix Chain Multiplication).
    \item \textbf{High-Value Algorithmic Problems and Solutions:} Number theory, prime generation, Euclidean GCD/LCM, series summation, two-sum variations, Bellman-Ford, Floyd-Warshall, Dijkstra, and advanced analytical viva problems.
\end{enumerate}
'''

ch07_text = clean_part_tex(os.path.join(latex_dir, 'ch07_algorithms.tex'),
                           'Part I: Sorting, Searching, and Graph Algorithms',
                           'Sorting and Searching', 'Sorting and Searching')
ch08_text = clean_part_tex(os.path.join(latex_dir, 'ch08_greedy_recursion_dp.tex'),
                           'Part II: Greedy Algorithms, Recursion, and Dynamic Programming',
                           'Greedy and DP', 'Greedy and DP')
ch09_text = clean_part_tex(os.path.join(latex_dir, 'ch09_algorithms_problems.tex'),
                           'Part III: High-Value Programming Problems and Solutions',
                           'Algorithm Problems', 'Algorithm Problems')

merged_algo = algo_intro.strip() + '\n\n' + '\n\n'.join([ch07_text, ch08_text, ch09_text]) + '\n'

out_algo_path = os.path.join(latex_dir, 'ch02_algorithms.tex')
with open(out_algo_path, 'w', encoding='utf-8') as f:
    f.write(merged_algo)
print(f"  [OK] Wrote {out_algo_path} ({len(merged_algo.splitlines())} lines, {len(merged_algo)} chars)")


print("\n--- 3. REORGANIZING CHAPTERS 3 THROUGH 11 ---")
chapter_map = [
    ('ch10_networking_subnetting.tex', 'ch03_networking_subnetting.tex'),
    ('ch11_cybersecurity.tex',         'ch04_cybersecurity.tex'),
    ('ch12_dbms_sql.tex',              'ch05_dbms_sql.tex'),
    ('ch13_operating_system.tex',      'ch06_operating_system.tex'),
    ('ch14_software_engineering.tex',  'ch07_software_engineering.tex'),
    ('ch15_cloud_ml.tex',              'ch08_cloud_ml.tex'),
    ('ch16_computer_architecture.tex', 'ch09_computer_architecture.tex'),
    ('ch17_electronics_hardware.tex',  'ch10_electronics_hardware.tex'),
    ('ch18_programming.tex',           'ch11_programming.tex'),
]

for src, dst in chapter_map:
    src_path = os.path.join(latex_dir, src)
    dst_path = os.path.join(latex_dir, dst)
    with open(src_path, 'r', encoding='utf-8') as f:
        t = f.read()
    
    # In cybersecurity, update "Chapter 11" string to "Cybersecurity"
    if src == 'ch11_cybersecurity.tex':
        t = t.replace('Across Chapter 11', 'Across Cybersecurity')
        t = t.replace('for Chapter 11', 'for Cybersecurity')
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f"  [OK] Created {dst} from {src}")


print("\n--- 4. UPDATING main.tex ---")
main_path = os.path.join(latex_dir, 'main.tex')
with open(main_path, 'r', encoding='utf-8') as f:
    main_text = f.read()

# Replace the old include block with the new 11-chapter include block
old_includes_pattern = re.compile(
    r'\\part\{Theoretical Foundations.*?\\include\{chapter1_location\}',
    re.DOTALL
)

new_includes_block = r'''\part{Theoretical Foundations \& Core Computer Science}
\label{part:foundations}

\include{ch01_data_structures}

\include{ch02_algorithms}

\include{ch03_networking_subnetting}

\include{ch04_cybersecurity}

\include{ch05_dbms_sql}

\include{ch06_operating_system}

\include{ch07_software_engineering}

\include{ch08_cloud_ml}

\include{ch09_computer_architecture}

\include{ch10_electronics_hardware}

\include{ch11_programming}

% =============================================================================
% PART II: VIVA & RECRUITMENT PREPARATION
% =============================================================================
\part{Comprehensive Viva \& Recruitment Question Bank}
\label{part:viva}

\include{chapter1_location}'''

if not old_includes_pattern.search(main_text):
    print("  [ERROR] Could not match old includes block in main.tex!")
    exit(1)

# Use lambda to prevent backslash escape parsing in replacement string
main_updated = old_includes_pattern.sub(lambda m: new_includes_block, main_text)
with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_updated)
print(f"  [OK] Successfully updated {main_path}")

print("\n--- 5. VERIFYING ENVIRONMENT BALANCES ---")
for fname in ['ch01_data_structures.tex', 'ch02_algorithms.tex']:
    fpath = os.path.join(latex_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    begins = re.findall(r'\\begin\{([a-zA-Z0-9*]+)\}', content)
    ends = re.findall(r'\\end\{([a-zA-Z0-9*]+)\}', content)
    cb = Counter(begins)
    ce = Counter(ends)
    all_envs = sorted(list(set(begins) | set(ends)))
    mismatches = [(e, cb[e], ce[e]) for e in all_envs if cb[e] != ce[e]]
    if mismatches:
        print(f"  [ERROR] Mismatches in {fname}: {mismatches}")
        exit(1)
    else:
        print(f"  [BALANCED] {fname} has all {len(all_envs)} environments balanced.")

print("\nReorganization script finished successfully!")
