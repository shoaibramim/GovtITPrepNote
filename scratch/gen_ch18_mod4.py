\section{Methods, Functions, Objects, Classes, and Friendship Mechanics}
\label{sec:methods_classes_friends}

\subsection{Free Functions versus Class Methods}
A \textbf{Free Function} (procedural function) exists independently in a namespace or global scope, accepting all operational state via its parameter list. A \textbf{Method} (member function) is declared within the scope of a class or struct, receiving an implicit \texttt{this} pointer (in C++) or reference (in Java) that binds the operation directly to an object instance.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Architectural Property} & \textbf{Free Function} & \textbf{Class Method} \\
\midrule
\textbf{Structural Scope} & Global scope or namespace; procedural. & Enclosed within a class, struct, or interface. \\
\textbf{Implicit Instance Binding} & No implicit object binding; no \texttt{this} pointer. & Operates on the invoking instance via implicit \texttt{this}. \\
\textbf{Access to Private State} & Denied unless declared as an explicit \texttt{friend}. & Granted full unrestricted access to private/protected state. \\
\textbf{Java Equivalence} & Non-existent; all Java functions are methods. & Standard instance and \texttt{static} class methods. \\
\bottomrule
\end{tabularx}
\caption{Systematic Distinction: Free Functions versus Object Methods}
\label{tab:function_vs_method}
\end{table}

\subsection{Friend Functions and Friend Classes in C++}
C++ provides the \texttt{friend} mechanism to grant external functions or external classes controlled access to internal \texttt{private} and \texttt{protected} members, bypassing normal access barriers.

\begin{lstlisting}[language=C++]
#include <iostream>

class Vector; // Forward declaration

class Matrix {
private:
    int data[3][3];
public:
    Matrix() { /* initialize data */ }
    friend Vector multiply(const Matrix& m, const Vector& v); // Friend function
    friend class LinearAlgebraEngine;                        // Friend class
};

class Vector {
private:
    int elements[3];
public:
    Vector() { /* initialize elements */ }
    friend Vector multiply(const Matrix& m, const Vector& v); // Friend function
};
\end{lstlisting}

\begin{keyconcept}[Fundamental Axioms of C++ Friendship]
\begin{itemize}[leftmargin=*]
    \item \textbf{Friendship is Granted, Not Taken:} Class $A$ must explicitly declare class $B$ or function $F$ as its friend. Class $B$ cannot declare itself a friend of $A$.
    \item \textbf{Friendship is Not Reciprocal:} If class $A$ declares class $B$ as a friend, class $B$ can access private members of $A$, but class $A$ \textbf{cannot} access private members of $B$.
    \item \textbf{Friendship is Not Transitive:} If $A$ is a friend of $B$, and $B$ is a friend of $C$, $A$ is \textbf{not} automatically a friend of $C$.
    \item \textbf{Friendship is Not Inherited:} If base class $A$ grants friendship to function $F$, derived class $D$ does \textbf{not} grant friendship to $F$.
    \item \textbf{Java Absence:} The \texttt{friend} keyword does not exist in Java. Java enforces package-level accessibility (default/package-private) instead.
\end{itemize}
\end{keyconcept}

\section{Method Overloading versus Method Overriding}
\label{sec:overloading_vs_overriding}

\subsection{Rules Governing Method Overloading (Compile-Time)}
Overloading permits multiple functions or methods to share an identical identifier within the same lexical scope, provided their formal parameter signatures are unambiguously distinguishable.
\begin{itemize}[leftmargin=*]
    \item Parameter signatures must differ in parameter count, parameter types, or ordering of types.
    \item \textbf{The Return Type Trap:} Altering the return type alone \textbf{does not constitute a valid overload}. The code below triggers a fatal compile-time ambiguity error:
    \begin{lstlisting}[language=C++]
    int calculate(int x);
    double calculate(int x); // COMPILE ERROR: Cannot overload on return type alone!
    \end{lstlisting}
\end{itemize}

\subsection{Rules Governing Method Overriding (Runtime)}
Overriding occurs when a derived class redefines an inherited virtual member function, substituting a specialized implementation.
\begin{itemize}[leftmargin=*]
    \item The method name, parameter count, parameter types, and const-qualifications must match the base virtual function signature exactly.
    \item The base method must be declared \texttt{virtual} in C++. Derived methods should use the \texttt{override} specifier (C++11) to trigger compiler verification.
    \item \textbf{Covariant Return Types:} Both C++ and Java allow an overridden method to return a pointer or reference to a more derived type than that returned by the base virtual method.
\end{itemize}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Technical Criterion} & \textbf{Method Overloading} & \textbf{Method Overriding} \\
\midrule
\textbf{Polymorphism Type} & Static / Compile-time polymorphism. & Dynamic / Runtime polymorphism. \\
\textbf{Scope Requirement} & Same class or same namespace scope. & Distinct classes connected via inheritance. \\
\textbf{Signature Match} & Must have different parameter lists. & Must have strictly identical parameter signatures. \\
\textbf{Return Type Constraint} & Return type may vary, but cannot be sole difference. & Must match base return type (or be covariant). \\
\textbf{Virtual Keyword} & \texttt{virtual} is irrelevant. & Base method must be explicitly \texttt{virtual} (in C++). \\
\bottomrule
\end{tabularx}
\caption{Systematic Comparison: Method Overloading versus Method Overriding}
\label{tab:overloading_vs_overriding}
\end{table}

\section{Constructors, Destructors, and Object Lifecycles}
\label{sec:constructors_destructors}

\subsection{Constructor Taxonomies and Initializer Lists}
Constructors initialize the memory allocated for an object instance.
\begin{itemize}[leftmargin=*]
    \item \textbf{Default Constructor:} Accepts zero arguments or provides defaults for all arguments.
    \item \textbf{Parameterized Constructor:} Initializes attributes using supplied argument values.
    \item \textbf{Copy Constructor (\texttt{T(const T\&)}):} Initializes an object by copying state from an existing instance of the identical class.
    \item \textbf{Move Constructor (\texttt{T(T\&\&) noexcept}):} Transfers ownership of heap-allocated resources from a temporary rvalue reference, avoiding expensive deep copies.
\end{itemize}

\begin{keyconcept}[Mandatory Use Cases for Member Initializer Lists]
A member initializer list directly initializes data members prior to the execution of the constructor body:
\begin{lstlisting}[language=C++]
class Device {
private:
    const int id;      // Const member: CANNOT be assigned inside body
    int& refPort;      // Reference member: MUST be bound at initialization
    Sensor sensor;     // Member lacking default constructor
public:
    Device(int i, int& port, int sVal) : id(i), refPort(port), sensor(sVal) {
        // Constructor body executes AFTER members are initialized
    }
};
\end{lstlisting}
Member initializer lists are strictly mandatory for: (1) \texttt{const} data members, (2) reference data members (\texttt{\&}), (3) members lacking default constructors, and (4) forwarding arguments to base class constructors.
\end{keyconcept}

\subsection{Constructor and Destructor Execution Order in Inheritance}
When instantiating a derived object, construction proceeds from the top of the inheritance tree downward; destruction proceeds in exactly reverse order (bottom-up):
\begin{enumerate}[leftmargin=*]
    \item Virtual base class constructors execute first.
    \item Non-virtual direct base class constructors execute in order of declaration.
    \item Non-static member objects execute their constructors in order of member declaration.
    \item The derived class constructor body executes.
    \item \textbf{Destruction Phase:} Executes in precisely reverse chronological sequence.
\end{enumerate}

\begin{lstlisting}[language=C++]
#include <iostream>

class Base {
public:
    Base() { std::cout << "Base Constructor\n"; }
    virtual ~Base() { std::cout << "Base Destructor\n"; }
};

class Derived : public Base {
public:
    Derived() { std::cout << "Derived Constructor\n"; }
    ~Derived() override { std::cout << "Derived Destructor\n"; }
};

int main() {
    Derived d;
    return 0;
}
\end{lstlisting}
Output:
\begin{lstlisting}
Base Constructor
Derived Constructor
Derived Destructor
Base Destructor
\end{lstlisting}

\begin{tcolorbox}[colback=codebg,colframe=quotetext,title=\textbf{Exam Trap: The Absolute Necessity of Virtual Destructors}]
If a derived class object is allocated dynamically on the heap and manipulated via a base class pointer (\texttt{Base* ptr = new Derived();}), deleting the object via \texttt{delete ptr;} results in \textbf{Undefined Behavior} and fatal memory leaks if the base class destructor is non-virtual! The compiler will statically bind the destructor call to \texttt{\~Base()}, failing to invoke \texttt{\~Derived()}. Always declare base class destructors \texttt{virtual} in polymorphic classes.
\end{tcolorbox}
