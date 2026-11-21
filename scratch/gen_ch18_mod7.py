\section{High-Probability Algorithmic Problems and Solutions}
\label{sec:algorithmic_problems_solutions}

\subsection{Finding the Distinct Second-Largest Array Element in $O(n)$}
Finding the second-largest element without full sorting ($O(n \log n)$) requires maintaining two tracking variables across a single linear pass.

\begin{lstlisting}[language=C]
#include <stdio.h>
#include <limits.h>

int find_second_largest(int arr[], int n) {
    if (n < 2) return INT_MIN; // Insufficient elements
    int largest = INT_MIN, second = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            second = largest;
            largest = arr[i];
        } else if (arr[i] > second && arr[i] < largest) {
            second = arr[i]; // Distinct second-largest
        }
    }
    return second;
}
\end{lstlisting}

\subsection{Binary Search and the Integer Overflow Mitigation Trap}
Binary search operates on sorted sequences by halving the search space on each iteration.
\begin{tcolorbox}[colback=codebg,colframe=quotetext,title=\textbf{Exam Trap: Midpoint Index Arithmetic Overflow}]
A classic bug occurs when computing the midpoint as \texttt{mid = (low + high) / 2}. In large arrays where $low + high > 2^{31}-1$, the sum wraps around to a negative integer, triggering a segmentation fault. Always write:
\[
\boxed{\text{mid} = \text{low} + \frac{\text{high} - \text{low}}{2}}
\]
\end{tcolorbox}

\begin{lstlisting}[language=C]
int binary_search(int a[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key)
            return mid; // Key found at index mid
        else if (a[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; // Key absent
}
\end{lstlisting}

\subsection{Sorting Algorithm Comparative Taxonomy}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l l l l l l}
\toprule
\textbf{Algorithm} & \textbf{Best Time} & \textbf{Average Time} & \textbf{Worst Time} & \textbf{Space} & \textbf{Stability} \\
\midrule
\textbf{Bubble Sort} & $O(n)$ (Optimized) & $O(n^2)$ & $O(n^2)$ & $O(1)$ & Stable \\
\textbf{Selection Sort} & $O(n^2)$ & $O(n^2)$ & $O(n^2)$ & $O(1)$ & Unstable \\
\textbf{Insertion Sort} & $O(n)$ & $O(n^2)$ & $O(n^2)$ & $O(1)$ & Stable \\
\textbf{Merge Sort} & $O(n \log n)$ & $O(n \log n)$ & $O(n \log n)$ & $O(n)$ & Stable \\
\textbf{Quick Sort} & $O(n \log n)$ & $O(n \log n)$ & $O(n^2)$ & $O(\log n)$ & Unstable \\
\textbf{Heap Sort} & $O(n \log n)$ & $O(n \log n)$ & $O(n \log n)$ & $O(1)$ & Unstable \\
\bottomrule
\end{tabularx}
\caption{Algorithmic Performance Matrix: Core Comparison of Sorting Paradigms}
\label{tab:sorting_comparison}
\end{table}

\subsection{Euclidean GCD and LCM Formulation}
The Euclidean algorithm computes the Greatest Common Divisor via repeated modulo division:
\[
\gcd(a, b) = \gcd(b, a \pmod b) \quad \text{until } b = 0
\]
The Least Common Multiple (LCM) is subsequently derived:
\[
\text{LCM}(a, b) = \frac{|a \times b|}{\gcd(a, b)}
\]

\begin{lstlisting}[language=C]
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b; // Divide first to avoid integer overflow
}
\end{lstlisting}

\subsection{Leap Year Gregorian Century Validation}
An astronomical calendar year is a leap year if and only if:
\[
(\text{year} \pmod{400} == 0) \quad \lor \quad (\text{year} \pmod 4 == 0 \ \land \ \text{year} \pmod{100} \ne 0)
\]
Years divisible by $100$ (e.g., 1900) are \textbf{not} leap years unless divisible by $400$ (e.g., 2000).

\section{Additional Programming Concepts Frequently Tested}
\label{sec:additional_frequently_tested_concepts}

\subsection{Const Pointers vs. Pointers to Const}
In C and C++, the positioning of the \texttt{const} keyword relative to the asterisk (\texttt{*}) determines mutability:
\begin{itemize}[leftmargin=*]
    \item \textbf{\texttt{const int *ptr} (or \texttt{int const *ptr}):} Pointer to constant data. The integer data being pointed to is read-only (\texttt{*ptr = 20;} is an error). The pointer address itself can be reassigned (\texttt{ptr = \&y;} is valid).
    \item \textbf{\texttt{int *const ptr = \&x;}:} Constant pointer to mutable data. The pointer address is permanently bound to $x$ (\texttt{ptr = \&y;} is an error). The underlying integer data can be modified (\texttt{*ptr = 20;} is valid).
    \item \textbf{\texttt{const int *const ptr = \&x;}:} Constant pointer to constant data. Neither the pointer address nor the underlying data can be modified.
\end{itemize}

\subsection{Structure versus Union Memory Architecture}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Architectural Metric} & \textbf{Structure (\texttt{struct})} & \textbf{Union (\texttt{union})} \\
\midrule
\textbf{Memory Allocation} & Every member receives its own distinct, non-overlapping memory offset. & All members share the exact same starting memory address (overlay). \\
\textbf{Aggregate Size} & Sum of member sizes plus compiler structure alignment padding. & Equal to the size of the largest individual member plus alignment padding. \\
\textbf{Active Members} & All members can store meaningful values simultaneously. & Only \textbf{one member} can hold an active, valid value at any instant. \\
\textbf{Mutation Impact} & Modifying member $A$ leaves member $B$ completely unaffected. & Writing to member $A$ overwrites and corrupts the bit-pattern of member $B$. \\
\bottomrule
\end{tabularx}
\caption{Architectural Comparison: C \texttt{struct} versus \texttt{union}}
\label{tab:struct_vs_union}
\end{table}

\subsection{C vs. C++ vs. Java Master Comparative Taxonomy}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Architectural Dimension} & \textbf{C} & \textbf{C++} & \textbf{Java} \\
\midrule
\textbf{Dominant Paradigm} & Procedural / Imperative & Multi-paradigm (OOP, Generic) & Pure Object-Oriented / Class-based \\
\textbf{Memory Model} & Manual (\texttt{malloc}/\texttt{free}) & Manual / RAII (\texttt{new}/\texttt{delete}) & Automatic Tracing Garbage Collection \\
\textbf{Pointer Manipulation} & Raw pointer arithmetic & Raw pointers and smart pointers & No pointer arithmetic; managed references \\
\textbf{Multiple Inheritance} & Unsupported & Supported (Virtual base classes) & Multiple interfaces; single class hierarchy \\
\textbf{Operator Overloading} & Unsupported & Fully supported & Unsupported (except built-in string \texttt{+}) \\
\textbf{Method Dispatch} & Static function calls & Static by default; \texttt{virtual} dynamic & Dynamic by default (except \texttt{static}/\texttt{final}) \\
\textbf{Exception Model} & Manual error codes & Structured try-catch-throw & Checked and unchecked exceptions \\
\bottomrule
\end{tabularx}
\caption{Cross-Language Architectural Matrix: C versus C++ versus Java}
\label{tab:c_cpp_java_matrix}
\end{table}

\subsection{Recurring Java Examination Traps}
\begin{enumerate}[leftmargin=*]
    \item \textbf{String Concatenation Evaluation Order:} In Java, \texttt{10 + 20 + "Java"} evaluates left-to-right as numeric addition ($30$) followed by concatenation: \texttt{"30Java"}. In contrast, \texttt{"Java" + 10 + 20} converts $10$ to string first (\texttt{"Java10"}), then concatenates $20$, producing \texttt{"Java1020"}.
    \item \textbf{Object Identity (\texttt{==}) vs. Value Equality (\texttt{.equals()}):} For object references, \texttt{a == b} evaluates whether both references point to the identical heap address. \texttt{a.equals(b)} evaluates semantic content equality. Two distinct \texttt{new String("Hello")} objects yield \texttt{false} for \texttt{==}, but \texttt{true} for \texttt{.equals()}.
    \item \textbf{Static Field Class Lifetime:} In Java, a \texttt{static} variable is tied to the Class object loaded in the JVM Metaspace, not individual object instances. Mutating a static field inside a constructor impacts the global class state across all past and future instances.
\end{enumerate}
