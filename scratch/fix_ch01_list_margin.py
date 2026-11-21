import re

# Update ch01
with open("latex/ch01_data_structures.tex", "r", encoding="utf-8") as f:
    ch01 = f.read()

old_enum_ch01 = r"""\begin{enumerate}[label=\bfseries Part \Roman*:]
    \item \textbf{Stack and Queue Architectures:} LIFO and FIFO operations, queue implementation using two stacks, amortized analysis, real-world systems applications, and common MCQ traps.
    \item \textbf{Linked Lists and Binary Heaps:} Singly, doubly, and circular linked lists, array vs. pointer trade-offs, max-heap and min-heap construction (heapify), insertion, deletion, and Heap Sort.
    \item \textbf{Circular Queues and Priority Queues:} Eliminating linear memory exhaustion via modulo arithmetic indexing, priority queue heap mappings, and scheduling algorithms.
    \item \textbf{Trees, Binary Trees, and B+ Trees:} Tree hierarchies, binary search trees (BST), balanced AVL trees, and exact mathematical formulations for minimum/maximum keys in B+ trees.
    \item \textbf{Graphs, Adjacency Representations, and Hash Tables:} Graph theory, adjacency list vs. matrix space/time trade-offs, hash functions, and collision resolution (chaining vs. open addressing).
    \item \textbf{Data Structure Recruitment Examination Problem Bank:} Essential worked algorithm-tracing problems, programming solutions, and analytical viva questions with complete step-by-step solutions.
\end{enumerate}"""

new_enum_ch01 = r"""\begin{enumerate}[label=\bfseries Part \Roman*:, leftmargin=*, align=left, itemsep=4pt, parsep=2pt]
    \item \textbf{Stack and Queue Architectures:} LIFO and FIFO operations, queue implementation using two stacks, amortized analysis, real-world systems applications, and common MCQ traps.
    \item \textbf{Linked Lists and Binary Heaps:} Singly, doubly, and circular linked lists, array vs. pointer trade-offs, max-heap and min-heap construction (heapify), insertion, deletion, and Heap Sort.
    \item \textbf{Circular Queues and Priority Queues:} Eliminating linear memory exhaustion via modulo arithmetic indexing, priority queue heap mappings, and scheduling algorithms.
    \item \textbf{Trees, Binary Trees, and B+ Trees:} Tree hierarchies, binary search trees (BST), balanced AVL trees, and exact mathematical formulations for minimum/maximum keys in B+ trees.
    \item \textbf{Graphs, Adjacency Representations, and Hash Tables:} Graph theory, adjacency list vs. matrix space/time trade-offs, hash functions, and collision resolution (chaining vs. open addressing).
    \item \textbf{Data Structure Recruitment Examination Problem Bank:} Essential worked algorithm-tracing problems, programming solutions, and analytical viva questions with complete step-by-step solutions.
\end{enumerate}"""

if old_enum_ch01 in ch01:
    ch01 = ch01.replace(old_enum_ch01, new_enum_ch01)
    with open("latex/ch01_data_structures.tex", "w", encoding="utf-8") as f:
        f.write(ch01)
    print("Updated ch01 list alignment!")
else:
    print("Could not find exact old_enum_ch01")

# Also check ch02
with open("latex/ch02_algorithms.tex", "r", encoding="utf-8") as f:
    ch02 = f.read()

old_enum_ch02 = r"""\begin{enumerate}[label=\bfseries Part \Roman*:]
    \item \textbf{Sorting, Searching, and Graph Traversal Algorithms:} Comparative analysis of comparison-based sorts (Bubble, Insertion, Merge, Quick), non-comparison sorts, two-pointer search, Binary Search, Breadth-First Search (BFS), Depth-First Search (DFS), and A* heuristic search.
    \item \textbf{Greedy Algorithms, Recursion, and Dynamic Programming:} Greedy-choice properties, Fractional Knapsack, Activity Selection, Huffman Coding, recursion trees, and dynamic programming formulations (0/1 Knapsack, Longest Common Subsequence, Matrix Chain Multiplication).
    \item \textbf{High-Value Algorithmic Problems and Solutions:} Number theory, prime generation, Euclidean GCD/LCM, series summation, two-sum variations, Bellman-Ford, Floyd-Warshall, Dijkstra, and advanced analytical viva problems.
\end{enumerate}"""

new_enum_ch02 = r"""\begin{enumerate}[label=\bfseries Part \Roman*:, leftmargin=*, align=left, itemsep=4pt, parsep=2pt]
    \item \textbf{Sorting, Searching, and Graph Traversal Algorithms:} Comparative analysis of comparison-based sorts (Bubble, Insertion, Merge, Quick), non-comparison sorts, two-pointer search, Binary Search, Breadth-First Search (BFS), Depth-First Search (DFS), and A* heuristic search.
    \item \textbf{Greedy Algorithms, Recursion, and Dynamic Programming:} Greedy-choice properties, Fractional Knapsack, Activity Selection, Huffman Coding, recursion trees, and dynamic programming formulations (0/1 Knapsack, Longest Common Subsequence, Matrix Chain Multiplication).
    \item \textbf{High-Value Algorithmic Problems and Solutions:} Number theory, prime generation, Euclidean GCD/LCM, series summation, two-sum variations, Bellman-Ford, Floyd-Warshall, Dijkstra, and advanced analytical viva problems.
\end{enumerate}"""

if old_enum_ch02 in ch02:
    ch02 = ch02.replace(old_enum_ch02, new_enum_ch02)
    with open("latex/ch02_algorithms.tex", "w", encoding="utf-8") as f:
        f.write(ch02)
    print("Updated ch02 list alignment!")
