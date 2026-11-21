\section{Model Examination Questions with Worked Solutions}
\label{sec:model_exam_questions_solutions}

\subsection{Section A: Code Output Analysis}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 1: Multiple Increment Sequencing}]
\textbf{Problem:} Determine the exact output of the following C program:
\begin{lstlisting}[language=C]
int x = 5;
printf("%d ", x++);
printf("%d ", ++x);
printf("%d", x);
\end{lstlisting}
\textbf{Solution:}
\begin{enumerate}[leftmargin=*]
    \item \texttt{printf("\%d ", x++);} evaluates to the current value of $x$ ($5$), prints \textbf{5}, then post-increments $x$ to $6$.
    \item \texttt{printf("\%d ", ++x);} pre-increments $x$ from $6$ to $7$, then yields and prints \textbf{7}.
    \item \texttt{printf("\%d", x);} prints the current value of $x$ (\textbf{7}).
\end{enumerate}
\textbf{Output:} \texttt{5 7 7}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 2: Integer Arithmetic and Precedence}]
\textbf{Problem:} Determine the output of the following code snippet:
\begin{lstlisting}[language=C]
int a = 10, b = 3;
printf("%d ", a / b);
printf("%d ", a % b);
printf("%d", a / b * b);
\end{lstlisting}
\textbf{Solution:}
\begin{itemize}[leftmargin=*]
    \item $a / b = 10 / 3 = 3$ (fractional component discarded). Prints \textbf{3}.
    \item $a \% b = 10 \pmod 3 = 1$. Prints \textbf{1}.
    \item $a / b * b$: Associates left-to-right: $(10 / 3) \times 3 = 3 \times 3 = 9$. Prints \textbf{9}.
\end{itemize}
\textbf{Output:} \texttt{3 1 9}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 3: Short-Circuit Logic with Side Effects}]
\textbf{Problem:} Trace the execution and determine the output:
\begin{lstlisting}[language=C]
int x = 0;
if (x++ && ++x)
    printf("A");
else
    printf("B");
printf("%d", x);
\end{lstlisting}
\textbf{Solution:}
\begin{itemize}[leftmargin=*]
    \item In \texttt{x++ \&\& ++x}, the left operand \texttt{x++} yields $0$ (false) and then post-increments $x$ to $1$.
    \item Because the left operand of logical AND is false, \textbf{short-circuit evaluation skips \texttt{++x}}.
    \item The condition evaluates to false; the \texttt{else} branch prints \textbf{B}.
    \item The trailing statement prints the current value of $x$ (\textbf{1}).
\end{itemize}
\textbf{Output:} \texttt{B1}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 4: Bitwise Left Shift Multiplication}]
\textbf{Problem:} What is the printed value of the expression \texttt{printf("\%d", a << 2);} when \texttt{int a = 3;}? \\
\textbf{Solution:} A bitwise left shift by $k$ bits ($a \ll k$) multiplies the non-negative integer by $2^k$:
\[
3 \ll 2 = 3 \times 2^2 = 3 \times 4 = 12
\]
Binary verification: $3_{10} = 00000011_2 \implies 00001100_2 = 12_{10}$. \\
\textbf{Output:} \texttt{12}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 5: Switch Statement Fall-Through}]
\textbf{Problem:} Determine the output when $x = 2$:
\begin{lstlisting}[language=C]
int x = 2;
switch (x) {
    case 1: printf("A");
    case 2: printf("B");
    case 3: printf("C");
            break;
    default: printf("D");
}
\end{lstlisting}
\textbf{Solution:} Control jumps directly to \texttt{case 2}, printing \textbf{B}. Because no \texttt{break} exists under \texttt{case 2}, execution falls through into \texttt{case 3}, printing \textbf{C}. The \texttt{break} under \texttt{case 3} terminates the switch. \\
\textbf{Output:} \texttt{BC}
\end{tcolorbox}

\subsection{Section B: Recursion Output Tracing}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 6: Static Variable Accumulation in Recursion}]
\textbf{Problem:} Trace the return value and output of \texttt{printf("\%d", fun(3));}:
\begin{lstlisting}[language=C]
int fun(int n) {
    static int x = 1;
    if (n == 0) return 0;
    x++;
    return x + fun(n - 1);
}
\end{lstlisting}
\textbf{Solution:}
Variable $x$ is static and persists across all calls:
\begin{itemize}[leftmargin=*]
    \item Call 1 ($n=3$): $x$ becomes $2$. Returns $2 + \text{fun}(2)$.
    \item Call 2 ($n=2$): $x$ becomes $3$. Returns $3 + \text{fun}(1)$.
    \item Call 3 ($n=1$): $x$ becomes $4$. Returns $4 + \text{fun}(0)$.
    \item Call 4 ($n=0$): Base case matches; returns $0$.
    \item Summation: $2 + 3 + 4 + 0 = 9$.
\end{itemize}
\textbf{Output:} \texttt{9}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 7: Unwinding Print vs. Winding Print}]
\textbf{Problem:} Compare the outputs of \texttt{funA(4)} and \texttt{funB(4)}:
\begin{lstlisting}[language=C]
void funA(int n) {
    if (n == 0) return;
    printf("%d ", n);
    funA(n - 1);
}

void funB(int n) {
    if (n == 0) return;
    funB(n - 1);
    printf("%d ", n);
}
\end{lstlisting}
\textbf{Solution:}
\begin{itemize}[leftmargin=*]
    \item In \texttt{funA}, \texttt{printf} precedes the recursive call (winding phase). Output: \texttt{4 3 2 1}.
    \item In \texttt{funB}, \texttt{printf} follows the recursive call (unwinding phase). Output: \texttt{1 2 3 4}.
\end{itemize}
\end{tcolorbox}

\subsection{Section C: Object-Oriented C++ Dispatch}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 8: Virtual vs. Non-Virtual Member Function Dispatch}]
\textbf{Problem:} What is the printed output of the following C++ program?
\begin{lstlisting}[language=C++]
class A {
public:
    void show() { std::cout << "A"; }
};

class B : public A {
public:
    void show() { std::cout << "B"; }
};

int main() {
    B obj;
    A *ptr = &obj;
    ptr->show();
    return 0;
}
\end{lstlisting}
\textbf{Solution:} Function \texttt{show()} is \textbf{non-virtual}. The compiler resolves the invocation at compile-time using the static pointer type (\texttt{A*}). It does not consult the vtable. \\
\textbf{Output:} \texttt{A}. \\
\textit{Note:} If \texttt{virtual void show()} were declared in base class \texttt{A}, dynamic dispatch would invoke \texttt{B::show()}, yielding \texttt{B}.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 9: Constructor and Destructor Destruction Sequencing}]
\textbf{Problem:} Predict the console output:
\begin{lstlisting}[language=C++]
class Test {
public:
    Test()  { std::cout << "C"; }
    ~Test() { std::cout << "D"; }
};

int main() {
    Test a;
    Test b;
    return 0;
}
\end{lstlisting}
\textbf{Solution:} Local stack objects are constructed in forward declaration order (\texttt{a} then \texttt{b}), printing \texttt{CC}. Upon exiting \texttt{main()}, local objects are destroyed in strictly \textbf{reverse order} (\texttt{b} then \texttt{a}), printing \texttt{DD}. \\
\textbf{Output:} \texttt{CCDD}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Question 10: Base and Derived Construction Hierarchy}]
\textbf{Problem:} What does the following program print?
\begin{lstlisting}[language=C++]
class A { public: A() { std::cout << "A"; } };
class B : public A { public: B() { std::cout << "B"; } };
int main() { B obj; return 0; }
\end{lstlisting}
\textbf{Solution:} When an instance of derived class \texttt{B} is instantiated, the base class \texttt{A} constructor must complete before the body of derived constructor \texttt{B} begins. \\
\textbf{Output:} \texttt{AB}
\end{tcolorbox}

\section{Analytical Viva Voce Question Bank}
\label{sec:viva_voce_question_bank}

\begin{enumerate}[leftmargin=*,label=\textbf{Q\arabic*.}]
    \item \textbf{What is the difference between \texttt{=} and \texttt{==} in C/C++?} \\
    \textbf{Answer:} \texttt{=} is the assignment operator, storing an rvalue into an lvalue memory location. \texttt{==} is the relational equality operator, comparing two values and returning $1$ (true) or $0$ (false).
    \item \textbf{Why does \texttt{\&\&} differ fundamentally from \texttt{\&}?} \\
    \textbf{Answer:} \texttt{\&\&} is a logical operator supporting short-circuit evaluation. \texttt{\&} is a bitwise operator performing bit-by-bit conjunction across integral operands without short-circuiting.
    \item \textbf{Explain the difference between \texttt{break} and \texttt{continue}.} \\
    \textbf{Answer:} \texttt{break} terminates the innermost enclosing loop or switch construct immediately. \texttt{continue} terminates only the current iteration, advancing immediately to the loop's next evaluation cycle.
    \item \textbf{Can a constructor be declared \texttt{virtual} in C++? Why or why not?} \\
    \textbf{Answer:} \textbf{No.} A constructor cannot be virtual. Virtual function dispatch relies on the virtual table pointer (\texttt{vptr}) inside the object. The \texttt{vptr} is only initialized during constructor execution; prior to object construction, no vtable linkage exists.
    \item \textbf{Can a destructor be declared \texttt{virtual} in C++? When is it mandatory?} \\
    \textbf{Answer:} \textbf{Yes.} A virtual destructor is mandatory whenever derived class objects are deleted polymorphically through a base class pointer (\texttt{Base* ptr = new Derived(); delete ptr;}). A non-virtual destructor results in undefined behavior and resource leaks.
    \item \textbf{Can constructors or destructors be overloaded?} \\
    \textbf{Answer:} Constructors \textbf{can} be overloaded with distinct parameter signatures. Destructors \textbf{cannot} be overloaded; a class possesses exactly one parameterless destructor.
    \item \textbf{What is a pure virtual function and an abstract class?} \\
    \textbf{Answer:} A pure virtual function is a virtual member function declared with \texttt{= 0} and no implementation in the base class. Any class containing at least one pure virtual function is an abstract class and cannot be instantiated.
    \item \textbf{Is a C++ \texttt{friend} function a member of the class granting friendship?} \\
    \textbf{Answer:} \textbf{No.} A friend function is a non-member function granted special access to private and protected members. It does not possess a \texttt{this} pointer and is not inherited.
    \item \textbf{Why does an uninitialized pointer represent a catastrophic security risk?} \\
    \textbf{Answer:} An uninitialized (wild) pointer contains arbitrary memory garbage. Writing through it can overwrite kernel memory, corrupt the call stack, or introduce arbitrary code execution vulnerabilities.
    \item \textbf{Explain why Java does not provide support for multiple inheritance of classes.} \\
    \textbf{Answer:} To eliminate the structural complexity and method ambiguity inherent in the \textbf{Diamond Problem}. Java achieves polymorphic multiple inheritance of interface contracts via \texttt{interface} declarations.
    \item \textbf{What is the difference between \texttt{df -h} and \texttt{du -sh} in Linux administration?} \\
    \textbf{Answer:} \texttt{df -h} inspects filesystem superblocks, reporting aggregate disk partition capacity, used space, and mount points. \texttt{du -sh} traverses directory trees recursively, summing file sizes to report disk space consumed by specific folders.
    \item \textbf{Why should a system administrator issue \texttt{kill -15} before \texttt{kill -9}?} \\
    \textbf{Answer:} \texttt{kill -15} sends \texttt{SIGTERM}, allowing the process to intercept the signal, terminate child threads, flush database buffers, and delete lock files. \texttt{kill -9} sends \texttt{SIGKILL}, which terminates the process abruptly via the kernel, potentially leaving databases corrupted.
    \item \textbf{What is the difference between Git merge and Git rebase?} \\
    \textbf{Answer:} \texttt{git merge} joins two branches by creating a 3-way merge commit, preserving historical topology. \texttt{git rebase} lifts commits from the feature branch and replays them linearly onto the target branch, rewriting commit hashes.
    \item \textbf{What is the difference between \texttt{git reset} and \texttt{git revert}?} \\
    \textbf{Answer:} \texttt{git reset} moves branch refs backward in time, modifying history (dangerous on public branches). \texttt{git revert} creates a brand-new commit that applies the inverse diff of a target commit, safely preserving history.
    \item \textbf{What is the purpose of the \texttt{.gitignore} configuration file?} \\
    \textbf{Answer:} It specifies path patterns that Git should intentionally ignore, preventing untracked build artifacts, secrets (\texttt{.env}), and temporary files from being committed.
    \item \textbf{What is the time complexity of searching a sorted array using Binary Search versus Linear Search?} \\
    \textbf{Answer:} Linear Search requires $O(n)$ time. Binary Search halves the search space each step, requiring $O(\log n)$ time.
    \item \textbf{Explain the fundamental structural difference between an array and a linked list.} \\
    \textbf{Answer:} Arrays allocate contiguous memory blocks offering $O(1)$ random indexing but $O(n)$ middle insertions. Linked lists store nodes non-contiguously via pointers, offering $O(1)$ insertions when the node reference is held, but $O(n)$ sequential access and pointer memory overhead.
    \item \textbf{What is the difference between \texttt{malloc()} and \texttt{calloc()} in C?} \\
    \textbf{Answer:} \texttt{malloc(size)} allocates raw uninitialized heap memory. \texttt{calloc(num, size)} allocates heap memory and initializes all allocated bytes to zero.
    \item \textbf{Explain the concept of memory leaks and how they are diagnosed.} \\
    \textbf{Answer:} A memory leak occurs when dynamically allocated heap blocks lose all pointer references without being deallocated via \texttt{free()}. They are detected via profiling tools such as Valgrind or AddressSanitizer.
    \item \textbf{What is the difference between Stack and Queue data structures?} \\
    \textbf{Answer:} A Stack operates under Last-In, First-Out (LIFO) semantics (\texttt{push}, \texttt{pop}). A Queue operates under First-In, First-Out (FIFO) semantics (\texttt{enqueue}, \texttt{dequeue}).
    \item \textbf{What is a Circular Queue and what problem does it solve?} \\
    \textbf{Answer:} A circular queue wraps the rear pointer back to index $0$ modulo the capacity. It resolves the ``false overflow'' problem of standard linear array queues where empty front slots cannot be reused.
    \item \textbf{Differentiate between BFS (Breadth-First Search) and DFS (Depth-First Search).} \\
    \textbf{Answer:} BFS traverses graphs level-by-level using a FIFO Queue ($O(V+E)$). DFS traverses deeply along graph branches before backtracking using a LIFO Stack or recursion ($O(V+E)$).
    \item \textbf{What is the difference between a Structure and a Union in C?} \\
    \textbf{Answer:} In a \texttt{struct}, each member has distinct memory. In a \texttt{union}, all members share the same base address; modifying one member overwrites the others.
    \item \textbf{What is the difference between a shallow copy and a deep copy?} \\
    \textbf{Answer:} A shallow copy duplicates primitive values and copies pointers directly, leaving both objects pointing to shared heap data. A deep copy allocates new independent heap memory and duplicates the underlying data.
    \item \textbf{What is a dangling pointer and how is it mitigated?} \\
    \textbf{Answer:} A dangling pointer points to memory that has already been freed. Mitigation: Immediately assign \texttt{ptr = NULL;} after invoking \texttt{free(ptr);}.
    \item \textbf{Why does \texttt{float x = 5 / 2;} evaluate to 2.0 rather than 2.5?} \\
    \textbf{Answer:} Because both $5$ and $2$ are integer literals, integer division truncates the result to $2$ before assignment to the float. Use \texttt{5.0 / 2}.
    \item \textbf{What does the \texttt{volatile} keyword signify to the C compiler?} \\
    \textbf{Answer:} It informs the optimizer that the variable's value can change unexpectedly (via hardware registers or ISRs), forcing the compiler to reload the value from memory on every read rather than caching it in CPU registers.
    \item \textbf{Explain the difference between \texttt{a++} and \texttt{++a}.} \\
    \textbf{Answer:} \texttt{a++} (postfix) yields the current value before incrementing. \texttt{++a} (prefix) increments the variable first and yields the updated value.
    \item \textbf{What is the Sieve of Eratosthenes and its time complexity?} \\
    \textbf{Answer:} An ancient algorithm that generates prime numbers up to $N$ by marking multiples of primes. Its time complexity is $O(N \log \log N)$.
    \item \textbf{What is the Diamond Problem in C++ and how is it resolved?} \\
    \textbf{Answer:} It occurs in multiple inheritance when a class derives from two classes that share a common base, resulting in duplicate base subobjects. It is resolved using \texttt{virtual} inheritance (\texttt{class B : virtual public A}).
\end{enumerate}

\section{Practical Programming Problems: Exam Practice Set}
\label{sec:exam_practice_set}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 1}]
\textbf{Question:} What is the printed output of: \texttt{printf("\%d", 17 / 5 + 17 \% 5);}? \\
\textbf{Options:} (A) 3 \quad (B) 4 \quad (C) 5 \quad (D) 6 \\
\textbf{Answer:} \textbf{(C) 5}. Tracing: $17 / 5 = 3$; $17 \pmod 5 = 2$; $3 + 2 = 5$.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 2}]
\textbf{Question:} Which iterative control loop is guaranteed to execute its body at least once? \\
\textbf{Options:} (A) \texttt{for} \quad (B) \texttt{while} \quad (C) \texttt{do-while} \quad (D) None \\
\textbf{Answer:} \textbf{(C) \texttt{do-while}}. It is an exit-controlled loop evaluating its condition at the bottom.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 3}]
\textbf{Question:} Which search algorithm requires the underlying dataset to be strictly ordered? \\
\textbf{Options:} (A) Linear search \quad (B) Binary search \quad (C) Both \quad (D) Neither \\
\textbf{Answer:} \textbf{(B) Binary search}. Relies on order to divide the search space in $O(\log n)$.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 4}]
\textbf{Question:} Which C++ mechanism enables runtime dynamic dispatch? \\
\textbf{Options:} (A) Function overloading \quad (B) Virtual functions \quad (C) Friend functions \quad (D) Templates \\
\textbf{Answer:} \textbf{(B) Virtual functions}. Dispatch is routed dynamically via the object's vtable.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 5}]
\textbf{Question:} What is the average-case asymptotic time complexity of Binary Search? \\
\textbf{Options:} (A) $O(1)$ \quad (B) $O(\log n)$ \quad (C) $O(n)$ \quad (D) $O(n^2)$ \\
\textbf{Answer:} \textbf{(B) $O(\log n)$}.
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Self-Test Question 6}]
\textbf{Question:} Which Git command moves staged index changes permanently into the local repository history? \\
\textbf{Options:} (A) \texttt{git add} \quad (B) \texttt{git push} \quad (C) \texttt{git commit} \quad (D) \texttt{git fetch} \\
\textbf{Answer:} \textbf{(C) \texttt{git commit}}.
\end{tcolorbox}

\section{Common Examination Traps: Final Revision Table}
\label{sec:exam_traps_revision_table}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X}
\toprule
\textbf{Examination Trap / Syntax Pattern} & \textbf{Accurate Technical Interpretation} \\
\midrule
\texttt{5 / 2} vs. \texttt{5.0 / 2} & \texttt{5 / 2} evaluates to integer $2$; \texttt{5.0 / 2} evaluates to float $2.5$. \\
\texttt{i++} vs. \texttt{++i} & \texttt{i++} yields original value; \texttt{++i} increments first and yields new value. \\
\texttt{\&\&} vs. \texttt{\&} & \texttt{\&\&} is short-circuit logical AND; \texttt{\&} is bitwise conjunction without short-circuiting. \\
\texttt{||} vs. \texttt{|} & \texttt{||} is short-circuit logical OR; \texttt{|} is bitwise inclusive OR without short-circuiting. \\
\texttt{=} vs. \texttt{==} & \texttt{=} is assignment; \texttt{==} is relational equality comparison. \\
\texttt{break} vs. \texttt{continue} & \texttt{break} exits nearest loop/switch; \texttt{continue} skips to next iteration. \\
Missing \texttt{break} in \texttt{switch} & Causes unconditional fall-through execution into subsequent case blocks. \\
Recursion lacking base case & Triggers unbounded recursion leading to call stack exhaustion (crash). \\
Statement after recursive call & Executes in reverse order during call stack unwinding. \\
Local \texttt{static} variable & Initialized once at startup; retains state across all function activations. \\
Valid C array index bounds & For array of size $N$, valid indices span strictly from $0$ to $N-1$. \\
Matrix multiplication constraint & Multiplication $A \times B$ requires: Columns of $A$ == Rows of $B$. \\
\texttt{*p++} vs. \texttt{(*p)++} & \texttt{*p++} dereferences then moves pointer; \texttt{(*p)++} increments value at pointer. \\
Java argument passing rule & Java is \textbf{strictly pass-by-value}; object references are copied by value. \\
C++ base/derived construction & Base class constructor executes \textit{before} derived class constructor. \\
C++ base/derived destruction & Derived class destructor executes \textit{before} base class destructor. \\
C++ polymorphic deletion & Base class destructor must be declared \texttt{virtual} to prevent undefined leaks. \\
Overloading vs. return type & Functions cannot be overloaded on return type alone; parameters must differ. \\
\texttt{git reset --hard} & Irrevocably destroys uncommitted working tree and staging area changes. \\
\texttt{df -h} vs. \texttt{du -sh} & \texttt{df -h} reports partition superblock usage; \texttt{du -sh} calculates folder size. \\
\texttt{kill -9} vs. \texttt{kill -15} & \texttt{SIGKILL} (9) forces instant death; \texttt{SIGTERM} (15) requests clean shutdown. \\
\bottomrule
\end{tabularx}
\caption{Comprehensive Reference of Common Examination Traps and Pitfalls}
\label{tab:common_exam_traps}
\end{table}

\section{Formula and Complexity Cheat Sheet}
\label{sec:formula_complexity_sheet}

\subsection{Mathematical Series Closed-Form Identities}
\begin{align*}
\text{Sum of First } n \text{ Integers:} &\quad \sum_{k=1}^{n} k = \frac{n(n+1)}{2} \\
\text{Sum of First } n \text{ Even Integers:} &\quad \sum_{k=1}^{n} 2k = n(n+1) \\
\text{Sum of First } n \text{ Odd Integers:} &\quad \sum_{k=1}^{n} (2k - 1) = n^2 \\
\text{Sum of First } n \text{ Squares:} &\quad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6} \\
\text{Sum of First } n \text{ Cubes:} &\quad \sum_{k=1}^{n} k^3 = \left[\frac{n(n+1)}{2}\right]^2 \\
\text{Floyd's Triangle Elements (} n \text{ rows):} &\quad T_n = \frac{n(n+1)}{2} \\
\text{Least Common Multiple:} &\quad \text{LCM}(a, b) = \frac{|a \times b|}{\gcd(a, b)}
\end{align*}

\subsection{Master Algorithmic Complexity Table}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X l}
\toprule
\textbf{Algorithm / Operation} & \textbf{Time Complexity} & \textbf{Auxiliary Space} \\
\midrule
Array Element Access by Index & $O(1)$ & $O(1)$ \\
Linear Search & $O(n)$ & $O(1)$ \\
Binary Search (Sorted Array) & $O(\log n)$ & $O(1)$ \\
Bubble Sort & $O(n)$ Best, $O(n^2)$ Average/Worst & $O(1)$ \\
Selection Sort & $O(n^2)$ All cases & $O(1)$ \\
Insertion Sort & $O(n)$ Best, $O(n^2)$ Average/Worst & $O(1)$ \\
Merge Sort & $O(n \log n)$ All cases & $O(n)$ \\
Quick Sort & $O(n \log n)$ Average, $O(n^2)$ Worst & $O(\log n)$ \\
Heap Sort & $O(n \log n)$ All cases & $O(1)$ \\
Square Matrix Multiplication (Standard) & $O(n^3)$ & $O(1)$ \\
Prime Testing via Trial Division & $O(\sqrt{n})$ & $O(1)$ \\
Sieve of Eratosthenes & $O(n \log \log n)$ & $O(n)$ \\
Naïve Recursive Fibonacci & $O(2^n)$ Exponential & $O(n)$ Stack depth \\
\bottomrule
\end{tabularx}
\caption{Master Algorithmic Complexity Reference}
\label{tab:algorithmic_complexity_reference}
\end{table}

\section{Recommended Preparation Priorities}
\label{sec:recommended_preparation_priorities}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Priority Tier} & \textbf{Core Examination Modules} & \textbf{Technical Focus and Mastery Targets} \\
\midrule
\textbf{Very High} & C/C++ Code Output Tracing & Operator precedence, integer division, loop side-effects, pointer dereferencing. \\
\textbf{Very High} & Recursion Analysis & Call stack activation tracing, winding vs. unwinding output, static variables. \\
\textbf{Very High} & Object-Oriented Programming & Four pillars, inheritance hierarchies, virtual functions, dynamic method dispatch. \\
\textbf{Very High} & Constructor / Destructor Mechanics & Lifecycle execution order, member initializer lists, virtual destructors. \\
\textbf{High} & Arrays, Strings, and Matrices & Matrix multiplication conformability, binary search, string palindromes, Euclidean GCD. \\
\textbf{High} & Parameter Passing Semantics & Value vs. reference, pointer simulation in C, Java pass-by-value reference models. \\
\textbf{High} & Version Control (Git) & Branching, 3-tier architecture, merge vs. rebase, conflict markers, reset vs. revert. \\
\textbf{Medium--High} & Linux Shell & File permissions (octal \texttt{chmod}), process signals (\texttt{kill -9} vs. \texttt{-15}), pipes, \texttt{ss}, \texttt{df}/\texttt{du}. \\
\textbf{Medium} & Fundamental Data Structures & Stack (LIFO), Queue (FIFO), Circular Queue, linked list topologies, BFS vs. DFS traversal. \\
\bottomrule
\end{tabularx}
\caption{Strategic Preparation Roadmap for Government IT Recruitment Examinations}
\label{tab:preparation_priorities}
\end{table}
