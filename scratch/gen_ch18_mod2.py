\section{Recursion and Recursive Function Output Tracing}
\label{sec:recursion_output_tracing}

Recursion occurs when a computational procedure is partitioned such that a function directly or indirectly invokes itself. Every robust recursive function requires two invariant properties:
\begin{enumerate}[leftmargin=*]
    \item \textbf{Base Case (Anchor):} A non-recursive terminal branch that halts the descent.
    \item \textbf{Recursive Step (Inductive Step):} A self-invocation that strictly reduces the problem domain toward the base case.
\end{enumerate}

\subsection{Activation Records and the Runtime Call Stack}
Each function invocation instantiates an \textbf{Activation Record} (stack frame) on the program's runtime call stack. The activation record encapsulates:
\begin{itemize}[leftmargin=*]
    \item Formal parameter values passed to the function.
    \item Local (automatic) variables scoped within the function.
    \item The caller's Return Address (instruction pointer).
    \item Saved frame pointers and processor register contexts.
\end{itemize}

\subsection{Execution Phases: Winding (Descent) vs. Unwinding (Ascent)}
A critical examination concept is that statements placed \textbf{before} the recursive call execute in forward sequence during stack frame allocation (winding phase), whereas statements placed \textbf{after} the recursive call execute in reverse sequence during frame deallocation (unwinding phase).

\begin{lstlisting}[language=C]
#include <stdio.h>

void trace(int n) {
    if (n == 0)
        return;
    printf("%d ", n);   // Executes during WINDING (descent)
    trace(n - 1);       // Recursive invocation
    printf("%d ", n);   // Executes during UNWINDING (ascent)
}

int main() {
    trace(3);
    return 0;
}
\end{lstlisting}

\begin{figure}[htbp]
\centering
\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Call Stack Trace for \texttt{trace(3)}}]
\begin{enumerate}[leftmargin=*]
    \item \texttt{trace(3)} prints \textbf{3}, pushes frame to stack, invokes \texttt{trace(2)}.
    \item \texttt{trace(2)} prints \textbf{2}, pushes frame to stack, invokes \texttt{trace(1)}.
    \item \texttt{trace(1)} prints \textbf{1}, pushes frame to stack, invokes \texttt{trace(0)}.
    \item \texttt{trace(0)} matches base case ($n == 0$) and returns immediately.
    \item Execution resumes in \texttt{trace(1)} at line 8: prints \textbf{1}, pops frame.
    \item Execution resumes in \texttt{trace(2)} at line 8: prints \textbf{2}, pops frame.
    \item Execution resumes in \texttt{trace(3)} at line 8: prints \textbf{3}, pops frame.
\end{enumerate}
\textbf{Final Program Output:} \texttt{3 2 1 1 2 3}
\end{tcolorbox}
\end{figure}

\subsection{Static Variables Within Recursive Scopes}
A local variable marked \texttt{static} resides in the program's data segment rather than on the stack. It is initialized exactly once at program launch and retains its updated value across all recursive activations.

\begin{lstlisting}[language=C]
#include <stdio.h>

void static_recurse(int n) {
    static int x = 0;
    if (n == 0)
        return;
    x++;
    printf("%d ", x);
    static_recurse(n - 1);
}

int main() {
    static_recurse(3);
    return 0;
}
\end{lstlisting}
Because variable $x$ is shared across all activations:
\begin{itemize}[leftmargin=*]
    \item Call 1 ($n=3$): $x$ increments from $0$ to $1$; prints \textbf{1}.
    \item Call 2 ($n=2$): $x$ increments from $1$ to $2$; prints \textbf{2}.
    \item Call 3 ($n=1$): $x$ increments from $2$ to $3$; prints \textbf{3}.
\end{itemize}
Output: \texttt{1 2 3}. In contrast, without the \texttt{static} keyword, each stack frame possesses an independent local variable $x$, yielding \texttt{1 1 1}.

\subsection{Tree Recursion and Exponential Growth: Fibonacci}
When a function issues multiple recursive calls per activation, it produces tree recursion. The naïve recursive Fibonacci implementation represents the classical benchmark:
\[
F(n) = \begin{cases} 0 & n = 0 \\ 1 & n = 1 \\ F(n-1) + F(n-2) & n \ge 2 \end{cases}
\]

\begin{lstlisting}[language=C]
int fib(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}
\end{lstlisting}
Because each call forks into two child calls, identical subproblems (e.g., $F(n-3)$) are evaluated repeatedly across different branches of the call tree. The number of leaf nodes scales as $\approx \phi^n$ where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$, resulting in an exponential time complexity of $O(2^n)$ and maximum stack depth (space complexity) of $O(n)$.

\section{Prime Numbers, Floyd's Triangle, and Numerical Series}
\label{sec:prime_numbers_series}

\subsection{Prime Number Verification in $O(\sqrt{n})$}
A prime number is an integer $n > 1$ divisible solely by $1$ and itself. The number $1$ is neither prime nor composite; $2$ is the unique even prime.

\begin{keyconcept}[Mathematical Justification for the $\sqrt{n}$ Boundary]
If an integer $n$ is composite, it can be factored as $n = a \times b$. If both factors $a$ and $b$ were strictly greater than $\sqrt{n}$, their product would exceed $n$:
\[
a > \sqrt{n} \quad \text{and} \quad b > \sqrt{n} \implies a \times b > \sqrt{n} \times \sqrt{n} = n
\]
This contradiction proves that at least one factor must satisfy $a \le \sqrt{n}$. Therefore, trial division up to $\lfloor\sqrt{n}\rfloor$ is mathematically sufficient to establish primality, collapsing the runtime from $O(n)$ to $O(\sqrt{n})$.
\end{keyconcept}

\begin{lstlisting}[language=C]
#include <stdio.h>

int is_prime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
    }
    return 1;
}
\end{lstlisting}

\subsection{The Sieve of Eratosthenes ($O(N \log \log N)$)}
To generate all primes up to a large threshold $N$, independent trial division requires $O(N \sqrt{N})$ time. The \textbf{Sieve of Eratosthenes} achieves $O(N \log \log N)$ by iteratively marking multiples of confirmed primes as composite.

\begin{lstlisting}[language=C]
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void sieve(int n) {
    bool prime[n + 1];
    memset(prime, true, sizeof(prime));
    prime[0] = prime[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            // Mark multiples starting from p^2
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
    for (int p = 2; p <= n; p++) {
        if (prime[p])
            printf("%d ", p);
    }
    printf("\n");
}
\end{lstlisting}

\subsection{Floyd's Triangle and Pattern Synthesis}
Floyd's triangle arranges consecutive positive integers into a right-angled triangle. Row $i$ contains exactly $i$ elements.

\begin{lstlisting}[language=C]
#include <stdio.h>

int main() {
    int rows = 5, num = 1;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%-3d ", num++);
        }
        printf("\n");
    }
    return 0;
}
\end{lstlisting}
Output for 5 rows:
\begin{lstlisting}
1   
2   3   
4   5   6   
7   8   9   10  
11  12  13  14  15  
\end{lstlisting}
The cumulative count of integers displayed across $n$ rows corresponds to the $n$-th triangular number:
\[
S_n = \sum_{k=1}^{n} k = \frac{n(n+1)}{2} \implies S_5 = \frac{5 \times 6}{2} = 15
\]

\section{Factorial and Summation of Series}
\label{sec:factorial_summation_series}

\subsection{Factorial Calculation and 64-Bit Integer Capacity Limits}
The mathematical factorial $n! = \prod_{k=1}^{n} k$ exhibits rapid combinatorial growth. In computer systems, primitive integer registers impose definitive ceilings:
\begin{itemize}[leftmargin=*]
    \item Standard 32-bit signed \texttt{int}: Overflow occurs at $13!$ ($12! = 479,001,600$; $13! = 6,227,020,800 > 2^{31}-1$).
    \item 64-bit unsigned \texttt{unsigned long long}: Maximum capacity is $20! \approx 2.43 \times 10^{18} < 2^{64}-1 \approx 1.84 \times 10^{19}$. At $21!$, arithmetic modulo $2^{64}$ causes silent data corruption.
\end{itemize}

\subsection{Fundamental Digit Extraction and Manipulation}
Algorithmic manipulation of decimal digits relies on the two complementary base-10 arithmetic operations:
\begin{itemize}[leftmargin=*]
    \item \texttt{n \% 10}: Extracts the least significant decimal digit.
    \item \texttt{n / 10}: Truncates the least significant decimal digit, shifting the number rightward.
\end{itemize}

\subsubsection{Integer Reversal and Palindrome Validation}
\begin{lstlisting}[language=C]
#include <stdio.h>

int is_palindrome(int n) {
    if (n < 0) return 0; // Negative integers are not palindromes
    int temp = n, reversed = 0;
    while (temp > 0) {
        int digit = temp % 10;
        reversed = reversed * 10 + digit;
        temp /= 10;
    }
    return (n == reversed);
}
\end{lstlisting}

\subsubsection{Armstrong (Narcissistic) Numbers}
An $n$-digit integer is an Armstrong number if the sum of its individual digits raised to the $n$-th power equals the original number:
\[
N = \sum_{k=1}^{d} (\text{digit}_k)^d \quad \text{e.g., } 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
\]

\subsection{Harmonic and Alternating Series Implementations}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X l}
\toprule
\textbf{Series Classification} & \textbf{Mathematical Definition} & \textbf{Closed-Form / Computational Rule} \\
\midrule
Sum of First $n$ Integers & $S_n = 1 + 2 + 3 + \dots + n$ & $S_n = \frac{n(n+1)}{2}$ \\
Sum of First $n$ Squares & $S_n = 1^2 + 2^2 + \dots + n^2$ & $S_n = \frac{n(n+1)(2n+1)}{6}$ \\
Sum of First $n$ Cubes & $S_n = 1^3 + 2^3 + \dots + n^3$ & $S_n = \left[\frac{n(n+1)}{2}\right]^2$ \\
Harmonic Series & $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n}$ & Iterative: \texttt{sum += 1.0 / i} (Floating-point) \\
Alternating Series & $S_n = 1 - 2 + 3 - 4 + \dots + (-1)^{n+1}n$ & Parity Branching or $(-1)^{n+1} \times \lceil n/2 \rceil$ \\
\bottomrule
\end{tabularx}
\caption{Mathematical Series and Asymptotic Summation Identities}
\label{tab:mathematical_series}
\end{table}
