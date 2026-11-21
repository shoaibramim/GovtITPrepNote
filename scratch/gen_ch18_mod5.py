\section{Branching and Looping: Control-Flow Tracing}
\label{sec:branching_looping_tracing}

\subsection{Dangling Else Ambiguity and Control Branching}
In C, C++, and Java, the compiler parses unbraced nested \texttt{if-else} statements by pairing each \texttt{else} with the \textbf{nearest preceding unmatched \texttt{if}} within the same block scope.

\begin{lstlisting}[language=C]
int a = 1, b = 0;
if (a == 1)
    if (b == 1)
        printf("A");
else
    printf("B");
\end{lstlisting}
Despite misleading indentation, the \texttt{else} binds to \texttt{if (b == 1)}. Because $a == 1$ is true but $b == 1$ is false, execution routes to the inner \texttt{else}, printing \texttt{B}. Explicit bracing must be utilized to bind the \texttt{else} to the outer condition.

\subsection{Switch Fall-Through Mechanics}
In a \texttt{switch} statement, control transfers to the matching \texttt{case} label. If the branch terminates without an explicit \texttt{break} statement, execution \textbf{falls through} sequentially into all subsequent case blocks regardless of their label conditions.

\begin{lstlisting}[language=C]
int x = 2;
switch (x) {
    case 1: printf("One ");
    case 2: printf("Two ");   // Matches here; falls through!
    case 3: printf("Three "); // Executes due to missing break!
            break;            // Exits switch here
    default: printf("Default");
}
\end{lstlisting}
Output: \texttt{Two Three }.

\subsection{Entry-Controlled vs. Exit-Controlled Iteration}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Operational Feature} & \textbf{\texttt{while} Loop} & \textbf{\texttt{do-while} Loop} \\
\midrule
\textbf{Control Classification} & Entry-controlled (pre-test). & Exit-controlled (post-test). \\
\textbf{Condition Evaluation} & Evaluated \textit{before} executing the loop body. & Evaluated \textit{after} executing the loop body. \\
\textbf{Minimum Executions} & \textbf{Zero} (if initial condition is false). & \textbf{Exactly One} (body executes unconditionally once). \\
\textbf{Syntax Structure} & \texttt{while (condition) \{ ... \}} & \texttt{do \{ ... \} while (condition);} \\
\bottomrule
\end{tabularx}
\caption{Systematic Comparison: \texttt{while} versus \texttt{do-while} Iteration}
\label{tab:while_vs_dowhile}
\end{table}

\begin{tcolorbox}[colback=codebg,colframe=quotetext,title=\textbf{Exam Trap: The \texttt{continue} Statement in \texttt{while} vs. \texttt{for} Loops}]
In a \texttt{for} loop, issuing \texttt{continue} skips the remaining body but \textbf{still executes the loop step expression} (\texttt{i++}). In a \texttt{while} loop, if the increment statement resides at the bottom of the body, \texttt{continue} skips the increment entirely, resulting in an \textbf{infinite loop}:
\begin{lstlisting}[language=C]
int i = 1;
while (i <= 5) {
    if (i == 3) continue; // TRAP: Skips i++; i remains 3 forever!
    printf("%d ", i);
    i++;
}
\end{lstlisting}
\end{tcolorbox}

\section{Parameter Passing, Pointers, and Memory Allocation}
\label{sec:parameter_passing_pointers}

\subsection{Call by Value vs. Call by Reference}
\begin{itemize}[leftmargin=*]
    \item \textbf{Call by Value (C Default):} The caller's argument is evaluated, and an independent bitwise copy is assigned to the function's formal parameter. Modifications made within the function affect only the local activation record.
    \item \textbf{Call by Reference (C++):} The formal parameter is declared as an alias (\texttt{\&}) bound directly to the caller's original lvalue. Modifications mutate the caller's variable directly.
    \item \textbf{Pointer Simulation in C:} C achieves reference semantics by explicitly passing the variable's memory address (\texttt{\&var}) into a pointer parameter (\texttt{*ptr}) and dereferencing it.
\end{itemize}

\begin{keyconcept}[The Java Pass-by-Value Invariant]
Java is \textbf{strictly 100\% pass-by-value}. There is no call-by-reference in Java:
\begin{itemize}[leftmargin=*]
    \item When passing primitive types (\texttt{int}, \texttt{double}), the raw value is copied.
    \item When passing object references (\texttt{MyClass obj}), \textbf{the reference handle itself (pointer value) is passed by value}. Both caller and callee reference copies point to the identical heap object. Mutating object fields (\texttt{obj.value = 100}) modifies the shared heap state. However, reassigning the parameter variable (\texttt{obj = new MyClass()}) mutates only the local copy, leaving the caller's reference unchanged!
\end{itemize}
\end{keyconcept}

\subsection{Pointer Topologies and Memory Hazards}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Pointer Classification} & \textbf{Architectural Definition} & \textbf{Safety Hazard / Mitigation} \\
\midrule
\textbf{Null Pointer} & Points to address $0$ (\texttt{NULL} / \texttt{nullptr}); explicitly denotes unassigned state. & Dereferencing causes OS segmentation fault (\texttt{SIGSEGV}). Always check \texttt{if (ptr != NULL)}. \\
\textbf{Void Pointer} & Generic pointer (\texttt{void*}) holding address of untyped memory. & Cannot be dereferenced or incremented without explicit typecasting. \\
\textbf{Wild Pointer} & Uninitialized pointer variable containing random stack/register garbage. & Unpredictable memory corruption. Always initialize to \texttt{NULL} or valid address. \\
\textbf{Dangling Pointer} & Points to storage that has been deallocated via \texttt{free()} or popped from stack. & Accessing causes undefined behavior. Immediately set \texttt{ptr = NULL} after \texttt{free(ptr)}. \\
\bottomrule
\end{tabularx}
\caption{Taxonomy of C/C++ Pointer Classifications and Memory Hazards}
\label{tab:pointer_hazards}
\end{table}

\subsection{Dynamic Memory Allocation: \texttt{malloc}, \texttt{calloc}, \texttt{realloc}, \texttt{free}}
\begin{itemize}[leftmargin=*]
    \item \textbf{\texttt{malloc(size\_t size)}:} Allocates a contiguous block of $size$ bytes on the heap. Leaves memory \textbf{uninitialized} (contains garbage).
    \item \textbf{\texttt{calloc(size\_t num, size\_t size)}:} Allocates storage for $num$ elements of $size$ bytes each, and explicitly initializes \textbf{all bytes to zero}.
    \item \textbf{\texttt{realloc(void* ptr, size\_t new\_size)}:} Resizes an existing heap block, relocating data to a new address if contiguous space is unavailable.
    \item \textbf{\texttt{free(void* ptr)}:} Releases the allocated heap block back to the runtime allocator.
    \item \textbf{Memory Leak:} Occurs when dynamically allocated heap storage is severed from all pointers without first invoking \texttt{free()}, exhausting available system RAM over time.
\end{itemize}

\section{Data Types, Type Conversion, and Storage Classes}
\label{sec:data_types_storage_classes}

\subsection{Fundamental Types and Integer Promotion Rules}
In C and C++, arithmetic operations are never performed directly on types narrower than \texttt{int}.
\begin{keyconcept}[Integer Promotion Axiom]
Whenever an expression involves small integer types (\texttt{char}, \texttt{signed char}, \texttt{unsigned char}, \texttt{short}, \texttt{unsigned short}), the compiler automatically promotes them to \texttt{int} (or \texttt{unsigned int} if \texttt{int} cannot represent all values of the original type) before performing the calculation.
\end{keyconcept}

\subsection{Unsigned Modular Arithmetic and Overflow Traps}
Signed integer overflow invokes \textbf{Undefined Behavior} in C and C++. In contrast, unsigned integer arithmetic is mathematically guaranteed to adhere to \textbf{modular arithmetic} ($x \pmod{2^n}$), where $n$ is the bit-width of the unsigned type.

\begin{lstlisting}[language=C]
unsigned int u = 0;
u--; // Underflows cleanly to (2^32 - 1) on 32-bit systems
printf("%u\n", u); // Prints 4294967295
\end{lstlisting}

\subsection{Floating-Point Representation and IEEE-754 Precision}
Binary floating-point numbers represent values as $(-1)^s \times (1 + \text{fraction}) \times 2^{\text{exponent}-127}$. Because decimal fractions such as $0.1$ and $0.2$ lack terminating representations in binary base-2, floating-point arithmetic incurs rounding discrepancies:
\[
0.1_{10} + 0.2_{10} = 0.3000000000000000444 \dots \ne 0.3_{10}
\]
In engineering examinations, never check floating-point equality using \texttt{if (a == b)}. Always check against an acceptable epsilon threshold: \texttt{if (fabs(a - b) < 1e-9)}.

\subsection{Storage Classes and Scoping Rules}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l l l X}
\toprule
\textbf{Storage Class} & \textbf{Storage Location} & \textbf{Scope} & \textbf{Lifetime / Architectural Semantics} \\
\midrule
\texttt{auto} & Stack & Block local & Automatically deallocated upon exiting the enclosing lexical block. \\
\texttt{static} (local) & Data segment & Block local & Retains state permanently across all subsequent function activations. \\
\texttt{static} (global) & Data segment & File scope & Restricts linkage to the current translation unit (internal linkage). \\
\texttt{extern} & Data segment & Global & References a variable or function defined in an external translation unit. \\
\texttt{volatile} & Memory / Register & Declared scope & Informs compiler that variable may mutate externally (hardware I/O / ISR); disables caching in registers. \\
\bottomrule
\end{tabularx}
\caption{Systematic Summary of C/C++ Storage Classes}
\label{tab:storage_classes}
\end{table}
