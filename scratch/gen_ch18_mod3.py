\section{Matrix Addition and Multiplication}
\label{sec:matrix_addition_multiplication}

Two-dimensional arrays in C and C++ are laid out in memory according to \textbf{Row-Major Order}, where row elements occupy contiguous linear addresses ($A[i][j] \implies \text{Base} + (i \times \text{Cols} + j) \times \text{sizeof(element)}$).

\subsection{Matrix Addition Conformability and Algorithm}
Two matrices $A$ and $B$ can be summed if and only if they share identical dimensions ($m \times n$).
\[
C_{ij} = A_{ij} + B_{ij} \quad \forall \ i \in [1, m], \ j \in [1, n]
\]
Computational time complexity is strictly $O(mn)$, requiring $O(1)$ auxiliary space beyond the destination storage.

\subsection{Matrix Multiplication Conformability and Algorithm}
Matrix multiplication is defined if and only if the number of columns in the multiplicand matrix $A$ equals the number of rows in the multiplier matrix $B$:
\[
A_{m \times n} \times B_{n \times p} = C_{m \times p}
\]
Each element $C_{ij}$ is computed as the vector dot product of row $i$ of matrix $A$ and column $j$ of matrix $B$:
\[
C_{ij} = \sum_{k=0}^{n-1} A_{ik} \times B_{kj}
\]

\begin{lstlisting}[language=C]
#include <stdio.h>

void multiply_matrices(int r1, int c1, int A[r1][c1],
                       int r2, int c2, int B[r2][c2],
                       int C[r1][c2]) {
    if (c1 != r2) {
        printf("Error: Incompatible dimensions for matrix multiplication.\n");
        return;
    }
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            C[i][j] = 0; // CRITICAL: Reset accumulator prior to summation
            for (int k = 0; k < c1; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}
\end{lstlisting}

\begin{keyconcept}[Asymptotic Complexity and Algebraic Properties]
\begin{itemize}[leftmargin=*]
    \item \textbf{Asymptotic Complexity:} Standard triple-nested iteration exhibits a runtime of $O(m \times n \times p)$. For two square matrices of dimension $n \times n$, complexity is $O(n^3)$.
    \item \textbf{Non-Commutative Property:} In general, matrix multiplication is \textbf{not commutative} ($AB \ne BA$). In fact, even when $AB$ is defined, $BA$ may be undefined unless $m = p$.
    \item \textbf{Associative and Distributive Properties:} Matrix multiplication is strictly associative ($(AB)C = A(BC)$) and distributive over addition ($A(B + C) = AB + AC$).
\end{itemize}
\end{keyconcept}

\section{Object-Oriented Programming (OOP) and the Four Pillars}
\label{sec:oop_four_pillars}

Object-Oriented Programming (OOP) organizes software systems into modular units called \textbf{Objects}, binding internal state (data members / attributes) with behavior (member functions / methods).

\begin{figure}[htbp]
\centering
\begin{tcolorbox}[colback=blockbg,colframe=primary,title=\textbf{The Four Foundational Pillars of Object-Oriented Architecture}]
\begin{enumerate}[leftmargin=*]
    \item \textbf{Encapsulation:} Bundling state and operations within a boundary, enforcing access restrictions to prevent unauthorized state tampering.
    \item \textbf{Abstraction:} Exposing clean, essential behavioral contracts while completely concealing low-level implementation mechanics.
    \item \textbf{Inheritance:} Deriving new specialized abstractions from existing generalized base classes, promoting hierarchical reuse.
    \item \textbf{Polymorphism:} Providing a unified interface that transparently executes distinct, type-specific behaviors at runtime.
\end{enumerate}
\end{tcolorbox}
\end{figure}

\subsection{Encapsulation and Data Hiding}
Encapsulation enforces internal data consistency by restricting external access via access specifiers (\texttt{private}, \texttt{protected}, \texttt{public}).
\begin{lstlisting}[language=C++]
class BankAccount {
private:
    double balance; // Hidden from direct external manipulation

public:
    BankAccount() : balance(0.0) {}
    void deposit(double amount) {
        if (amount > 0) balance += amount; // Validated state mutation
    }
    double getBalance() const { return balance; } // Controlled access
};
\end{lstlisting}

\subsection{Abstraction: Abstract Classes and Pure Virtual Functions}
In C++, an \textbf{Abstract Class} serves as an interface contract containing at least one \textbf{Pure Virtual Function} (\texttt{virtual void f() = 0;}). Direct instantiation of an abstract class is prohibited by the compiler.

\begin{lstlisting}[language=C++]
class Shape {
public:
    virtual double area() const = 0; // Pure virtual function
    virtual ~Shape() {}              // Virtual destructor mandatory
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(double l, double w) : length(l), width(w) {}
    double area() const override { return length * width; }
};
\end{lstlisting}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Architectural Metric} & \textbf{Abstraction} & \textbf{Encapsulation} \\
\midrule
\textbf{Core Focus} & Concentrates on \textit{what} an object does. & Concentrates on \textit{how} internal data is guarded. \\
\textbf{Implementation} & Achieved via abstract classes and interfaces. & Achieved via classes and access specifiers (\texttt{private}). \\
\textbf{Design Goal} & Hides implementation complexity. & Hides internal data representation and state mutations. \\
\textbf{Real-World Analogy} & An automobile accelerator pedal and dashboard. & The internal engine cylinder combustion chamber. \\
\bottomrule
\end{tabularx}
\caption{Systematic Architectural Comparison: Abstraction versus Encapsulation}
\label{tab:abstraction_vs_encapsulation}
\end{table}

\subsection{Inheritance Taxonomies and The Diamond Problem}
C++ supports five distinct inheritance topologies: Single, Multilevel, Multiple, Hierarchical, and Hybrid.

\begin{keyconcept}[The Diamond Problem and Virtual Inheritance]
In multiple inheritance, when class $D$ inherits from both classes $B$ and $C$, which both inherit from base class $A$, class $D$ inherits two distinct, duplicate subobjects of $A$. Any reference to a member of $A$ (e.g., \texttt{d.x}) produces a compiler ambiguity error:
\begin{lstlisting}[language=C++]
class A { public: int x; };
class B : public A {};
class C : public A {};
class D : public B, public C {}; // Ambiguous: D contains two copies of A!
\end{lstlisting}
To eliminate this ambiguity, C++ introduces \textbf{Virtual Base Classes}. By declaring inheritance as \texttt{virtual public A}, the compiler ensures that only one shared, canonical instance of base class $A$ is instantiated within derived object $D$:
\begin{lstlisting}[language=C++]
class B : virtual public A {};
class C : virtual public A {};
class D : public B, public C {}; // Resolved: Exactly one shared subobject of A
\end{lstlisting}
\end{keyconcept}

\subsection{C++ Access Specifiers Under Inheritance}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Base Member Access} & \textbf{Public Inheritance} & \textbf{Protected Inheritance} & \textbf{Private Inheritance} \\
\midrule
\texttt{public} & \texttt{public} in derived & \texttt{protected} in derived & \texttt{private} in derived \\
\texttt{protected} & \texttt{protected} in derived & \texttt{protected} in derived & \texttt{private} in derived \\
\texttt{private} & Inaccessible directly & Inaccessible directly & Inaccessible directly \\
\bottomrule
\end{tabularx}
\caption{Inherited Member Accessibility Under C++ Derivation Modes}
\label{tab:inheritance_access_modes}
\end{table}

\section{Polymorphism, Static Binding, and Dynamic Binding}
\label{sec:polymorphism_binding}

Polymorphism (``many forms'') enables a single programmatic interface to execute distinct implementations based on object context.

\subsection{Compile-Time (Static) Polymorphism}
Resolved entirely by the compiler during translation. Incurs zero runtime overhead.
\begin{itemize}[leftmargin=*]
    \item \textbf{Function Overloading:} Declaring multiple functions within the same scope sharing an identical name but differing in parameter count or parameter data types.
    \item \textbf{Operator Overloading:} Redefining the semantics of C++ operators for user-defined types (e.g., implementing vector addition via \texttt{operator+}).
    \item \textbf{Templates (Generic Programming):} Parameterizing functions and classes over types, instantiated during compilation.
\end{itemize}

\subsection{Runtime (Dynamic) Polymorphism and Virtual Tables}
Runtime polymorphism enables a base class pointer or reference to invoke derived class method overrides dynamically based on the actual type of the underlying heap/stack object.

\begin{figure}[htbp]
\centering
\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Vtable and Vptr Internal Dispatch Mechanics in C++}]
\begin{enumerate}[leftmargin=*]
    \item \textbf{Virtual Table (vtable):} For every class declaring or inheriting at least one virtual function, the compiler constructs a static lookup table (\texttt{vtable}) containing function pointers to the most-derived implementations of those virtual methods.
    \item \textbf{Virtual Table Pointer (vptr):} Every object instance of a polymorphic class contains an implicit hidden pointer (\texttt{vptr}) inserted at byte-offset zero, pointing directly to that class's static \texttt{vtable}.
    \item \textbf{Dynamic Dispatch Resolution:} When invoking \texttt{ptr->virtualMethod()}, the machine code dereferences \texttt{ptr} to find \texttt{vptr}, indexes into the \texttt{vtable} at the method's assigned slot, and jumps to the target function address.
\end{enumerate}
\end{tcolorbox}
\end{figure}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Dispatch Feature} & \textbf{Static Binding (Early Binding)} & \textbf{Dynamic Binding (Late Binding)} \\
\midrule
\textbf{Resolution Phase} & Compile-time and link-time. & Runtime during program execution. \\
\textbf{Mechanisms} & Non-virtual functions, overloaded functions. & Overridden \texttt{virtual} methods via base pointers. \\
\textbf{Performance} & Direct memory jump; can be inlined. & Indirection overhead via \texttt{vptr} and \texttt{vtable}. \\
\textbf{Flexibility} & Fixed at build time. & High extensibility; supports open-closed design. \\
\textbf{Java Equivalence} & \texttt{static}, \texttt{final}, and \texttt{private} methods. & Standard instance methods (polymorphic by default). \\
\bottomrule
\end{tabularx}
\caption{Comprehensive Comparison: Static Binding versus Dynamic Binding}
\label{tab:static_vs_dynamic_binding}
\end{table}
