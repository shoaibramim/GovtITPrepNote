# -*- coding: utf-8 -*-
"""
Module 1 for Chapter 18: Programming — Problem Solving, Code Tracing, OOP and Practical IT Skills
Covers:
- Chapter Header & Comprehensive Roadmap
- Section 1: C/C++/Java Code Snippet Output Analysis
- Section 2: Increment and Decrement Operators
"""

content = r'''
\chapter{Programming: Problem Solving, Code Tracing, OOP, and Practical IT Skills}
\label{ch:programming_oop_skills}

This chapter focuses on \textbf{program analysis, mental code tracing, output prediction, algorithmic problem solving, object-oriented design, and practical developer tools} essential for Assistant Programmer, Assistant Network Engineer, Database Administrator, and IT Specialist recruitment examinations under the Bangladesh Public Service Commission (BPSC), state-owned banks (Bankers Selection Committee), and government ministries. Rather than basic syntax, this material targets recurring examination traps: operator precedence, integer truncation, side-effect sequencing, call stack unwinding in recursion, dynamic method dispatch, pointer arithmetic, object lifecycles, Git branching workflows, and Linux system management.

\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Code-Snippet Output Analysis:} Operator precedence, associativity, integer division, truncation toward zero, short-circuit evaluation, the comma operator, conditional expressions, and C/C++ undefined behavior.
    \item \textbf{Increment and Decrement Operators:} Prefix versus postfix evaluation, side effects within expressions, loop boundary mutations, and pointer increment expressions (\texttt{*p++} vs. \texttt{(*p)++}).
    \item \textbf{Recursion and Call Stack Tracing:} Activation records, winding vs. unwinding execution, static variables in recursive scopes, Fibonacci exponential trees, and recursion-to-iteration transformations.
    \item \textbf{Prime Numbers, Series, and Floyd's Triangle:} Prime checks in $O(\sqrt{n})$, Sieve of Eratosthenes, Floyd's triangle generation, geometric and star pattern printing, and arithmetic/geometric summations.
    \item \textbf{Factorial and Digit Manipulation:} Iterative and recursive factorials, integer overflow mitigation, digit extraction/summation, number reversal, palindrome validation, Armstrong numbers, and harmonic/alternating series.
    \item \textbf{Matrix Operations and Dimensional Rules:} Two-dimensional array representations, matrix addition conformability, matrix multiplication algorithms ($O(mnp)$), and algebraic properties.
    \item \textbf{Object-Oriented Programming (OOP) Fundamentals:} The four pillars (Encapsulation, Abstraction, Inheritance, Polymorphism), class vs. object, inheritance models, the diamond problem, and C++ virtual inheritance.
    \item \textbf{Polymorphism and Method Dispatch:} Compile-time vs. runtime polymorphism, function and operator overloading, virtual functions, vtables, vptrs, and static vs. dynamic binding in C++ and Java.
    \item \textbf{Advanced Class Mechanisms:} Free functions vs. methods, friend functions, friend classes, encapsulation boundaries, and Java architectural contrasts.
    \item \textbf{Method Overloading vs. Overriding:} Signature rules, return-type constraints, name hiding, covariant return types, and virtual function dispatch.
    \item \textbf{Constructors, Destructors, and Object Lifecycles:} Default, parameterized, copy, and move constructors, member initializer lists, execution order in inheritance hierarchies, virtual destructors, and Java garbage collection semantics.
    \item \textbf{Control-Flow Tracing:} Dangling else ambiguities, switch fall-through mechanics, entry-controlled (\texttt{while}) vs. exit-controlled (\texttt{do-while}) loops, and \texttt{break} vs. \texttt{continue} traps.
    \item \textbf{Parameter Passing, Pointers, and Memory Allocation:} Pass-by-value, pass-by-reference, pointer simulation in C, Java reference semantics, pointer arithmetic, array decay, null/wild/dangling pointers, and dynamic memory management (\texttt{malloc}, \texttt{calloc}, \texttt{free}).
    \item \textbf{Data Types, Type Conversion, and Storage Classes:} Primitive type sizing, signed vs. unsigned modular arithmetic, integer promotion rules, floating-point IEEE-754 precision traps, and storage durations (\texttt{auto}, \texttt{static}, \texttt{extern}, \texttt{volatile}).
    \item \textbf{Version Control with Git:} Distributed VCS architecture, working directory, staging index, commit DAGs, branching, merging vs. rebasing, conflict resolution, \texttt{.gitignore}, and remote collaboration.
    \item \textbf{Essential Bash Commands for IT Engineers:} Filesystem navigation, text filtering (\texttt{grep}, \texttt{find}), octal file permissions (\texttt{chmod}, \texttt{chown}), process management, signaling (\texttt{SIGTERM}, \texttt{SIGKILL}), and pipeline redirection.
    \item \textbf{High-Probability Algorithmic Problems:} Linear and binary search, sorting algorithms (Bubble, Selection, Insertion, Merge, Quick), array rotation, string palindromes, Euclidean GCD/LCM, and leap-year logic.
    \item \textbf{Comparative Language Architectures:} C vs. C++ vs. Java feature matrix, Big-O complexity classifications, and memory models.
    \item \textbf{Model Examination Questions \& Detailed Solutions:} 20 multi-part code-tracing and analytical problems with complete step-by-step solutions.
    \item \textbf{Analytical Viva Voce Question Bank:} 30 foundational oral examination questions covering programming, OOP, and data structure internals.
    \item \textbf{Practice Problem Set \& Self-Test:} Structured multiple-choice questions with verified answer keys.
    \item \textbf{Examination Traps \& Revision Sheet:} Concise reference matrix highlighting high-frequency candidate pitfalls.
    \item \textbf{Mathematical Formula and Complexity Cheat Sheet:} Quick-reference summary of mathematical series formulas and algorithmic asymptotic runtimes.
    \item \textbf{Recommended Preparation Priorities:} Strategic topic weighting for government IT written and oral examinations.
\end{enumerate}

\section{C/C++/Java Code Snippet Output Analysis}
\label{sec:code_snippet_output_analysis}

Output-tracing questions assess a candidate's ability to mentally simulate the target language's abstract state machine, adhering strictly to language standards rather than casual assumptions.

\subsection{Operator Precedence and Associativity}
\textbf{Precedence} establishes the relative priority of distinct operators when competing for operands in an unparenthesized expression. \textbf{Associativity} dictates the evaluation grouping (left-to-right or right-to-left) of adjacent operators sharing identical precedence.

\begin{lstlisting}[language=C]
int x = 10 + 5 * 2;
printf("%d", x);
\end{lstlisting}

Because multiplication (\texttt{*}) has higher precedence than addition (\texttt{+}), the multiplication executes first:
\[
x = 10 + (5 \times 2) = 10 + 10 = 20
\]

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X l}
\toprule
\textbf{Operators} & \textbf{Description / Operation} & \textbf{Associativity} \\
\midrule
\texttt{()}, \texttt{[]}, \texttt{->}, \texttt{.} & Scope resolution, function call, array subscript, member access & Left-to-right \\
\texttt{++}, \texttt{--}, \texttt{!}, \texttt{\~{}}, \texttt{+}, \texttt{-}, \texttt{*}, \texttt{\&}, \texttt{sizeof} & Unary prefix operators, logical/bitwise NOT, address-of, dereference & Right-to-left \\
\texttt{*}, \texttt{/}, \texttt{\%} & Multiplicative arithmetic operators (multiplication, division, modulus) & Left-to-right \\
\texttt{+}, \texttt{-} & Additive arithmetic operators (addition, subtraction) & Left-to-right \\
\texttt{<<}, \texttt{>>} & Bitwise bit-shift operators (left shift, right shift) & Left-to-right \\
\texttt{<}, \texttt{<=}, \texttt{>}, \texttt{>=} & Relational relational comparison operators & Left-to-right \\
\texttt{==}, \texttt{!=} & Equality comparison operators & Left-to-right \\
\texttt{\&} & Bitwise AND operator & Left-to-right \\
\texttt{\^{}} & Bitwise XOR (exclusive OR) operator & Left-to-right \\
\texttt{|} & Bitwise OR (inclusive OR) operator & Left-to-right \\
\texttt{\&\&} & Logical short-circuit AND operator & Left-to-right \\
\texttt{||} & Logical short-circuit OR operator & Left-to-right \\
\texttt{?:} & Ternary conditional operator & Right-to-left \\
\texttt{=}, \texttt{+=}, \texttt{-=}, \texttt{*=}, \texttt{/=} & Compound assignment operators & Right-to-left \\
\texttt{,} & Comma operator (sequencing expression) & Left-to-right \\
\bottomrule
\end{tabularx}
\caption{C and C++ Operator Precedence and Associativity Hierarchy}
\label{tab:c_operator_precedence}
\end{table}

\begin{tcolorbox}[colback=blockbg,colframe=primary,title=\textbf{Important Distinction: Precedence vs. Evaluation Order}]
Operator precedence and associativity determine \textbf{grammatical grouping} (syntax tree structure), \textit{not} the physical temporal order of operand evaluation. In C and C++, the order in which subexpressions (operands) are evaluated is generally \textbf{unspecified}. In the expression $f(a) + g(b) \times h(c)$, multiplication groups $g(b)$ with $h(c)$, but the compiler is entirely free to invoke function $h()$ before $f()$ or $g()$.
\end{tcolorbox}

\subsubsection{Right-to-Left Assignment Associativity}
\begin{lstlisting}[language=C]
int a, b, c;
a = b = c = 5;
printf("%d %d %d", a, b, c);
\end{lstlisting}
Because assignment (\texttt{=}) is right-associative, the expression parses as:
\[
a = (b = (c = 5))
\]
The inner assignment sets $c = 5$ and yields the value $5$, which is assigned to $b$, and subsequently to $a$. The program prints:
\begin{lstlisting}
5 5 5
\end{lstlisting}

\subsubsection{Multiplicative and Additive Precedence Tracing}
\begin{lstlisting}[language=C]
int x = 20, y = 5, z = 2;
printf("%d", x / y * z + 3);
\end{lstlisting}
Division (\texttt{/}) and multiplication (\texttt{*}) share equal precedence and associate left-to-right:
\[
(x / y) \times z + 3 = (20 / 5) \times 2 + 3 = 4 \times 2 + 3 = 8 + 3 = 11
\]
The program outputs \texttt{11}.

\subsection{Integer Division, Modulus, and Truncation Toward Zero}
When both operands of the division operator (\texttt{/}) are integers, the language standard mandates \textbf{integer division}: any fractional remainder is discarded (truncated).

\begin{lstlisting}[language=C]
int a = 17, b = 5;
printf("%d\n", a / b);
printf("%d\n", a % b);
\end{lstlisting}
The output is:
\begin{lstlisting}
3
2
\end{lstlisting}
This satisfies the algebraic identity:
\[
a = (a / b) \times b + (a \pmod b) \implies 17 = (3 \times 5) + 2
\]

\begin{tcolorbox}[colback=codebg,colframe=quotetext,title=\textbf{Exam Trap: Integer Division Before Floating-Point Assignment}]
\begin{lstlisting}[language=C]
float x = 5 / 2;
printf("%.1f", x);
\end{lstlisting}
Because both $5$ and $2$ are integer literals, integer division executes first, yielding the integer $2$. This integer is only then implicitly promoted to a float ($2.0$). To retain the fractional component, at least one operand must be of floating-point type:
\begin{lstlisting}[language=C]
float x = 5.0 / 2;       // Evaluates to 2.5
float y = (float)5 / 2;   // Evaluates to 2.5
\end{lstlisting}
\end{tcolorbox}

\subsubsection{Negative Integer Truncation (C99, C++11, and Java Standards)}
Prior to C99, integer division with negative operands was implementation-defined. Modern C, C++, and Java standards strictly mandate \textbf{truncation toward zero}:
\begin{lstlisting}[language=C]
printf("%d %d\n", -7 / 2, -7 % 2);
printf("%d %d\n", 7 / -2, 7 % -2);
\end{lstlisting}
Output:
\begin{lstlisting}
-3 -1
-3 1
\end{lstlisting}
In all cases, $(-3) \times (\pm 2) + (\text{remainder}) = \pm 7$. The sign of the modulus result always matches the sign of the numerator (dividend).

\subsection{Short-Circuit Evaluation of Logical Operators}
The logical AND (\texttt{\&\&}) and logical OR (\texttt{||}) operators exhibit guaranteed short-circuit evaluation:
\begin{itemize}[leftmargin=*]
    \item \textbf{\texttt{A \&\& B}:} If expression $A$ evaluates to false ($0$), expression $B$ is \textbf{guaranteed not to be evaluated}.
    \item \textbf{\texttt{A || B}:} If expression $A$ evaluates to true ($\ne 0$), expression $B$ is \textbf{guaranteed not to be evaluated}.
\end{itemize}

\begin{lstlisting}[language=C]
int x = 5;
if (x > 10 && ++x > 5)
    printf("Branch A\n");
printf("%d\n", x);
\end{lstlisting}
Because $x > 10$ ($5 > 10$) is false, the right-hand operand (\texttt{++x > 5}) is never evaluated. The variable $x$ remains unchanged at $5$.

\begin{lstlisting}[language=C]
int x = 5;
if (x == 5 || ++x > 5)
    printf("Branch B\n");
printf("%d\n", x);
\end{lstlisting}
Because $x == 5$ is true, the \texttt{||} operator short-circuits immediately. The second operand is skipped, and $x$ remains $5$. The code prints \texttt{Branch B} followed by \texttt{5}.

\subsection{The Comma Operator as an Expression Sequencer}
In C and C++, the comma operator (\texttt{,}) has the lowest precedence of all operators. It evaluates its left operand, completely discards the resulting value, introduces a sequence point, evaluates its right operand, and yields the right operand's value and type.

\begin{lstlisting}[language=C]
int x;
x = (10, 20, 30);
printf("%d\n", x);
\end{lstlisting}
Parentheses bind the comma operators together. The expressions $10$ and $20$ are evaluated and discarded; $30$ is returned and assigned to $x$. Output: \texttt{30}.

\begin{lstlisting}[language=C]
int a = 1, b = 2, c;
c = (a++, b++, a + b);
printf("%d %d %d\n", a, b, c);
\end{lstlisting}
Tracing step-by-step:
\begin{enumerate}[leftmargin=*]
    \item \texttt{a++} increments $a$ from $1$ to $2$; value discarded.
    \item \texttt{b++} increments $b$ from $2$ to $3$; value discarded.
    \item \texttt{a + b} computes $2 + 3 = 5$, which is assigned to $c$.
\end{enumerate}
Output: \texttt{2 3 5}.

\subsection{Undefined Behavior in C and C++ Expressions}
An expression exhibits \textbf{Undefined Behavior (UB)} when the language standard imposes no requirements on the compiler. The executable may crash, generate garbage results, or produce erratic output that varies across compiler optimization levels (-O0 vs. -O3).

\begin{tcolorbox}[colback=codebg,colframe=quotetext,title=\textbf{Critical Examination Warning: Modification Without Sequencing}]
Consider the notorious snippet:
\begin{lstlisting}[language=C]
int i = 5;
printf("%d %d\n", i++, ++i); // UNDEFINED BEHAVIOR!
i = i++;                     // UNDEFINED BEHAVIOR!
int x = i++ + ++i;           // UNDEFINED BEHAVIOR!
\end{lstlisting}
Prior to C++17, modifying a scalar object more than once between two consecutive sequence points without an intervening read yields \textbf{strictly undefined behavior}. Even under modern C++17 sequencing rules, writing $i = i++$ or combining multiple unsequenced mutations within arithmetic operands is illegal. In written recruitment examinations, candidates should explicitly write: \textit{``The expression exhibits Undefined Behavior under standard C/C++ due to unsequenced side-effects.''}
\end{tcolorbox}

\section{Increment and Decrement Operators}
\label{sec:increment_decrement_operators}

\subsection{Prefix vs. Postfix Semantics}
\begin{itemize}[leftmargin=*]
    \item \textbf{Prefix Increment (\texttt{++i}):} Increments the operand by $1$ as a side-effect, and produces the \textbf{new, updated value} as the result of the expression.
    \item \textbf{Postfix Increment (\texttt{i++}):} Increments the operand by $1$ as a side-effect, but produces the \textbf{original, un-incremented value} as the result of the expression.
\end{itemize}

\begin{lstlisting}[language=C]
int a = 5;
int b = ++a; // a becomes 6, b is assigned 6
int c = a++; // c is assigned 6, a becomes 7
printf("%d %d %d", a, b, c);
\end{lstlisting}
Output: \texttt{7 6 6}.

\subsection{Postfix and Prefix Operators Combined with Pointers}
Pointer arithmetic combined with dereferencing represents one of the most common examination hurdles:
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Expression} & \textbf{Equivalent Grouping} & \textbf{Operational Behavior} \\
\midrule
\texttt{*p++} & \texttt{*(p++)} & Dereferences current pointer $p$, yields the value at that address, then increments the pointer address by \texttt{sizeof(*p)}. \\
\texttt{*++p} & \texttt{*(++p)} & Increments pointer address $p$ first, then dereferences and yields the value at the new address. \\
\texttt{++*p} & \texttt{++(*p)} & Dereferences pointer $p$, then increments the stored value at that address (prefix). \\
\texttt{(*p)++} & \texttt{(*p)++} & Dereferences pointer $p$, yields current stored value, then increments the value at that address (postfix). \\
\bottomrule
\end{tabularx}
\caption{Pointer Dereference and Increment Precedence Matrix}
\label{tab:pointer_increment_matrix}
\end{table}

\begin{lstlisting}[language=C]
int a[] = {10, 20, 30};
int *p = a;
printf("%d ", *p++); // Prints 10; p now points to a[1] (20)
printf("%d\n", *p);  // Prints 20

int b[] = {10, 20, 30};
int *q = b;
printf("%d ", (*q)++); // Prints 10; b[0] is incremented to 11
printf("%d\n", *q);    // Prints 11; q still points to b[0]
\end{lstlisting}
'''
