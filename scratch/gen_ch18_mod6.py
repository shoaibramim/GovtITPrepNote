\section{Version Control with Git}
\label{sec:version_control_git}

Git is a distributed version control system (DVCS) where every developer clone functions as a complete repository containing full cryptographic history.

\subsection{Architectural Stages: The Three-Tier Workflow}
\begin{figure}[htbp]
\centering
\begin{tcolorbox}[colback=white,colframe=primary,title=\textbf{Git Architecture: The Four Lifecycle Zones}]
\begin{enumerate}[leftmargin=*]
    \item \textbf{Working Directory:} Physical sandbox where files are edited locally.
    \item \textbf{Staging Area (Index):} Intermediate binary index staging changes targeted for the next commit (\texttt{git add}).
    \item \textbf{Local Repository:} Committed snapshots stored locally inside the hidden \texttt{.git} object database (\texttt{git commit}).
    \item \textbf{Remote Repository:} Centralized host (GitHub, GitLab, Bitbucket) facilitating distributed synchronization (\texttt{git push} / \texttt{git fetch}).
\end{enumerate}
\end{tcolorbox}
\end{figure}

\subsection{Git Terminology and Essential Command Reference}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X}
\toprule
\textbf{Git Command} & \textbf{Operational Function} \\
\midrule
\texttt{git init} & Initializes a new, empty Git repository in the current directory. \\
\texttt{git clone <url>} & Clones an entire remote repository, including branches and history, to local disk. \\
\texttt{git status} & Displays working tree state: untracked, modified, and staged files. \\
\texttt{git add <path>} & Stages modified file contents into the Index ready for commit. \\
\texttt{git commit -m "msg"} & Records a permanent snapshot of staged changes into the local commit history. \\
\texttt{git log --oneline} & Displays commit history as compact single-line SHA-1 hashes and commit messages. \\
\texttt{git diff} & Compares modifications between the working directory and the staging area. \\
\texttt{git diff --staged} & Compares staged modifications against the most recent commit (\texttt{HEAD}). \\
\texttt{git switch -c <br>} & Creates and immediately checks out a new feature branch (replaces \texttt{git checkout -b}). \\
\texttt{git merge <branch>} & Combines history from the specified branch into the currently checked-out branch. \\
\texttt{git fetch <remote>} & Downloads commits, files, and refs from a remote repository without integrating. \\
\texttt{git pull <remote>} & Executes \texttt{git fetch} followed immediately by \texttt{git merge} into current branch. \\
\texttt{git push <rem> <br>} & Transmits local branch commits to the upstream remote repository. \\
\bottomrule
\end{tabularx}
\caption{Essential Git Command Reference for IT Engineers}
\label{tab:git_commands}
\end{table}

\subsection{Git Merge versus Git Rebase}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Feature} & \textbf{Git Merge} & \textbf{Git Rebase} \\
\midrule
\textbf{Branch History} & Preserves complete non-linear branch topology and chronological order. & Rewrites commit history into a clean, linear sequence. \\
\textbf{Merge Commit} & Creates a dedicated 3-way merge commit (unless fast-forwarded). & Never creates a merge commit; reapplies commits individually. \\
\textbf{Traceability} & Explicitly records when features were integrated. & Linearizes history; obscures actual parallel branch lifecycles. \\
\textbf{The Golden Rule} & Safe for shared, published public branches. & \textbf{Never rebase public shared branches}; rewrites public history! \\
\bottomrule
\end{tabularx}
\caption{Systematic Comparison: Git Merge versus Git Rebase}
\label{tab:git_merge_vs_rebase}
\end{table}

\subsection{Undoing Changes: Git Reset versus Git Revert}
\begin{itemize}[leftmargin=*]
    \item \textbf{\texttt{git reset --soft HEAD\~{}1}:} Moves branch pointer backward by 1 commit. Leaves all modified files intact in the \textbf{Staging Area}.
    \item \textbf{\texttt{git reset --mixed HEAD\~{}1} (Default):} Moves branch pointer backward by 1 commit. Unstages changes, leaving modified files intact in the \textbf{Working Directory}.
    \item \textbf{\texttt{git reset --hard HEAD\~{}1}:} Moves branch pointer backward and \textbf{permanently destroys} all uncommitted working tree and staging area changes!
    \item \textbf{\texttt{git revert <commit-hash>}:} Non-destructive undo. Generates a \textbf{brand-new commit} that mathematically reverses the patch introduced by the target commit, safely preserving historical integrity on public branches.
\end{itemize}

\section{Essential Bash Commands for IT Recruitment Exams}
\label{sec:bash_commands_it_exams}

\subsection{File System Navigation and Manipulation}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l X l}
\toprule
\textbf{Command} & \textbf{Description} & \textbf{Typical Practical Invocation} \\
\midrule
\texttt{pwd} & Print current absolute working directory path & \texttt{pwd} \\
\texttt{ls} & List directory contents with metadata & \texttt{ls -la /var/log} \\
\texttt{cd} & Change current shell working directory & \texttt{cd /etc/nginx} \\
\texttt{mkdir} & Create directory (including parent directories) & \texttt{mkdir -p /opt/app/logs} \\
\texttt{rm} & Remove files or recursively delete directory trees & \texttt{rm -rf /tmp/cache} \\
\texttt{cp} & Copy files or directories recursively & \texttt{cp -r src/ /backup/src/} \\
\texttt{mv} & Move or rename files and directories & \texttt{mv old\_name.c new\_name.c} \\
\texttt{head} / \texttt{tail} & Display top or bottom $N$ lines of a file & \texttt{tail -f /var/log/syslog} \\
\texttt{wc} & Count lines, words, and byte counts in a file & \texttt{wc -l access.log} \\
\bottomrule
\end{tabularx}
\caption{Core Bash Filesystem Navigation and File Operations}
\label{tab:bash_file_commands}
\end{table}

\subsection{Octal Permissions and Ownership Management}
Linux filesystems enforce a 3-tier security model: \textbf{Owner (User)}, \textbf{Group}, and \textbf{Others}. Permissions are quantified as:
\begin{itemize}[leftmargin=*]
    \item \textbf{Read ($r = 4$):} Permits viewing file contents or listing directory entries.
    \item \textbf{Write ($w = 2$):} Permits modifying file contents or creating/deleting files within a directory.
    \item \textbf{Execute ($x = 1$):} Permits running the file as a program or entering/traversing a directory.
\end{itemize}

\begin{keyconcept}[Octal Calculation for \texttt{chmod 755}]
\begin{itemize}[leftmargin=*]
    \item Owner: $r + w + x = 4 + 2 + 1 = \mathbf{7}$ (Full read, write, execute).
    \item Group: $r + x = 4 + 0 + 1 = \mathbf{5}$ (Read and execute only).
    \item Others: $r + x = 4 + 0 + 1 = \mathbf{5}$ (Read and execute only).
    \item Command: \texttt{chmod 755 deploy.sh} $\implies$ \texttt{-rwxr-xr-x}.
\end{itemize}
\end{keyconcept}

\subsection{Process Management and Inter-Process Signals}
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{l l X}
\toprule
\textbf{Signal Name} & \textbf{Number} & \textbf{Operational Semantics} \\
\midrule
\texttt{SIGHUP} & 1 & Hangup detected on controlling terminal; reloads daemon configurations. \\
\texttt{SIGINT} & 2 & Interrupt from keyboard (\texttt{Ctrl+C}); gracefully requests process halt. \\
\texttt{SIGKILL} & 9 & \textbf{Unconditional, immediate termination} enforced directly by the OS kernel. Cannot be caught, blocked, or ignored. Prevents process cleanup. \\
\texttt{SIGTERM} & 15 & \textbf{Polite termination request} (Default for \texttt{kill}). Allows process to release sockets, flush buffers, and close file handles. \\
\bottomrule
\end{tabularx}
\caption{Standard POSIX Process Signals and Operational Hierarchy}
\label{tab:posix_signals}
\end{table}

\subsection{Networking and Socket Inspection Diagnostics}
\begin{itemize}[leftmargin=*]
    \item \textbf{\texttt{ip addr}:} Displays all network interfaces, link states, MAC addresses, and assigned IPv4/IPv6 addresses (replaces legacy \texttt{ifconfig}).
    \item \textbf{\texttt{ss -tulnp}:} Modern socket statistics utility. Displays active listening TCP/UDP ports (\texttt{-t} TCP, \texttt{-u} UDP, \texttt{-l} listening, \texttt{-n} numeric ports, \texttt{-p} process PID/name). Replaces legacy \texttt{netstat}.
    \item \textbf{\texttt{ping -c 4 8.8.8.8}:} Injects ICMP Echo Request datagrams to verify Layer~3 IP connectivity and measure round-trip packet latency.
    \item \textbf{\texttt{curl -I https://api.gov.bd}:} Fetches HTTP response headers without downloading the body payload, verifying web service status.
    \item \textbf{\texttt{dig domain.com}:} Performs authoritative DNS lookup diagnostics, querying nameserver records (A, AAAA, MX, NS, CNAME).
\end{itemize}

\subsection{Pipes and Stream Redirection Operators}
\begin{itemize}[leftmargin=*]
    \item \textbf{Standard Pipe (\texttt{|}):} Diverts \texttt{stdout} of upstream command directly into \texttt{stdin} of downstream command (\texttt{ps aux | grep nginx}).
    \item \textbf{Output Redirection (\texttt{>}):} Redirects standard output to a file, \textbf{overwriting} existing contents (\texttt{echo "test" > file.txt}).
    \item \textbf{Append Redirection (\texttt{>>}):} Appends standard output to the end of a file without truncating (\texttt{echo "line" >> file.txt}).
    \item \textbf{Standard Error Redirection (\texttt{2>}):} Redirects \texttt{stderr} stream ($FD=2$) to a file (\texttt{make 2> errors.log}).
    \item \textbf{Unified Stream Redirection (\texttt{> file 2>\&1} or \texttt{\&> file}):} Merges both standard output and standard error into a single destination file.
\end{itemize}
