# -*- coding: utf-8 -*-
"""
Module 6 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Contains:
- Section 35: Computer Hardware Subsystem Architecture
- Section 36: Motherboards, Form Factors, Expansion Buses, and Chipsets
- Section 37: Central Processing Units, Thermal Dynamics, and Throttling
- Section 38: RAM Topologies, NVMe/SATA SSDs, S.M.A.R.T., and RAID
- Section 39: BIOS versus UEFI Firmware and MBR versus GPT Partitioning
- Section 40: The Computer Startup Sequence, POST Diagnostics, and Bootstrapping
- Section 41: Systematic Boot Failure Troubleshooting (No Power, No POST, No Boot, No Video)
"""

def get_mod6_tex():
    return r'''
\section{Computer Hardware Subsystem Architecture}
\label{sec:hardware_architecture}

Modern enterprise computers are tightly integrated modular systems executing synchronized data exchanges across high-speed digital buses.

\subsection{Hardware, Software, and Firmware Abstraction Tiers}
\begin{table}[htbp]
\centering
\small
\caption{System Tiers: Hardware versus Software versus Firmware}
\label{tab:hw_sw_fw}
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Dimension} & \textbf{Hardware} & \textbf{Software} & \textbf{Firmware} \\
\midrule
\textbf{Physical Nature} & Tangible physical electronic circuits and silicon dies. & Abstract binary instruction sequences and data structures. & Low-level code permanently burned into non-volatile Flash ROM chips. \\
\textbf{Mutability} & Rigid; altered only by physical replacement or rework. & Highly dynamic; updated, compiled, and modified continuously. & Semi-permanent; updated via controlled cryptographic firmware flashing. \\
\textbf{Execution Layer} & Physical physical execution engine (ALU, registers). & Executes in User or Kernel space under OS scheduling. & Executes at hardware bare-metal level prior to OS bootstrap. \\
\textbf{Examples} & CPU, DDR5 RAM, PCIe NVMe SSD, Motherboard. & Linux Kernel, PostgreSQL, Nginx Web Server, Hypervisors. & UEFI Firmware, SSD Controller Firmware, RAID Controller BIOS. \\
\bottomrule
\end{tabularx}
\end{table}


\section{Motherboards, Form Factors, Expansion Buses, and Chipsets}
\label{sec:motherboards}

The \textbf{Motherboard} (mainboard) is the central printed circuit board (PCB) that routes high-speed data buses, distributes DC power rails, and interconnects the CPU, memory, and peripheral controllers.

\subsection{CPU Sockets and Packaging Types}
\begin{itemize}
    \item \textbf{LGA (Land Grid Array):} The physical pins reside inside the motherboard socket; the CPU has gold contact pads on its underside (standard for Intel and modern AMD AM5/SP5 processors). Reduces risk of bent CPU pins.
    \item \textbf{PGA (Pin Grid Array):} The pins are permanently attached to the CPU package and insert into a zero-insertion-force (ZIF) socket on the board (legacy AMD AM4).
    \item \textbf{BGA (Ball Grid Array):} The processor is permanently soldered to the motherboard using microscopic solder balls; non-upgradable (used in laptops, routers, and embedded appliances).
\end{itemize}

\subsection{PCI Express (PCIe) Architecture}
PCI Express is a high-speed, point-to-point serial differential expansion bus:
\begin{itemize}
    \item Bandwidth scales linearly with physical lanes: $\times 1, \times 4, \times 8, \times 16$.
    \item \textbf{Generational Bandwidth Scaling (per lane, simplex):}
    \begin{itemize}
        \item PCIe Gen 3: $\approx 1\text{ GB/s}$ per lane ($\times 16 \approx 16\text{ GB/s}$).
        \item PCIe Gen 4: $\approx 2\text{ GB/s}$ per lane ($\times 16 \approx 32\text{ GB/s}$).
        \item PCIe Gen 5: $\approx 4\text{ GB/s}$ per lane ($\times 16 \approx 64\text{ GB/s}$).
    \end{itemize}
\end{itemize}

\subsection{Motherboard Form Factors}
\begin{table}[htbp]
\centering
\small
\caption{Industry Motherboard Form Factor Specifications}
\label{tab:motherboard_form_factors}
\begin{tabularx}{\textwidth}{l c c X}
\toprule
\textbf{Form Factor} & \textbf{Dimensions (W $\times$ D)} & \textbf{PCIe Slots} & \textbf{Standard Deployment Domain} \\
\midrule
\textbf{Standard ATX} & $305 \times 244\text{ mm}$ ($12.0 \times 9.6\text{ in}$) & Up to 7 slots & Mid/Full-tower enterprise workstations and entry servers. \\
\textbf{Micro-ATX (mATX)} & $244 \times 244\text{ mm}$ ($9.6 \times 9.6\text{ in}$) & Up to 4 slots & Compact business desktop PCs and cost-sensitive systems. \\
\textbf{Mini-ITX} & $170 \times 170\text{ mm}$ ($6.7 \times 6.7\text{ in}$) & Exactly 1 slot & Ultra-small form factor (USFF) appliances, firewall nodes. \\
\bottomrule
\end{tabularx}
\end{table}


\section{Central Processing Units, Thermal Dynamics, and Throttling}
\label{sec:cpu_thermals}

\subsection{Physical Cores versus SMT Logical Threads}
A \textbf{Physical Core} is an independent, complete hardware execution unit containing its own private L1/L2 caches, instruction decoders, floating-point units, and integer execution ALUs.
\begin{itemize}
    \item \textbf{Simultaneous Multithreading (SMT / Hyper-Threading):} Replicates only the architectural register context (PC, flags, register file) within a single core while sharing execution units.
    \item A processor with 8 cores and 16 threads possesses \textbf{8 true physical hardware cores}, exposing 16 execution contexts to the operating system scheduler.
\end{itemize}

\subsection{Thermal Dynamics and Thermal Interface Material (TIM)}
Microscopic imperfections and air pockets on the mating surfaces of the CPU integrated heat spreader (IHS) and copper heatsink base create severe thermal contact resistance (air has a poor thermal conductivity $k_{\text{air}} \approx 0.026\text{ W}/(\text{m}\cdot\text{K})$).
\begin{itemize}
    \item \textbf{Thermal Paste (TIM):} A zinc-oxide or silicone suspension ($k \approx 4\text{ to } 12\text{ W}/(\text{m}\cdot\text{K})$) applied in a thin layer to fill microscopic air voids, facilitating efficient conductive heat transfer into the heatsink.
\end{itemize}

\subsection{Thermal Throttling: Mechanism and Diagnosis}
Every modern CPU incorporates internal digital thermal sensors (DTS). When junction temperature ($T_j$) approaches the calibrated critical ceiling (typically $95^{\circ}\text{C}$ to $105^{\circ}\text{C}$):
\begin{itemize}
    \item \textbf{Hardware Thermal Throttling:} The internal power management unit drops operating voltage and slashes clock multiplier frequencies (e.g., throttling from $4.8\text{ GHz} \to 1.2\text{ GHz}$) within microseconds to prevent silicon burnout.
    \item \textit{Symptoms:} Sudden, severe system performance degradation under load; loud fan noise; system stuttering.
    \item \textit{Root Causes:} Dust accumulation choking heatsink fins; dried, pumped-out thermal paste; failed liquid cooling pump; broken fan bearings.
\end{itemize}


\section{RAM Topologies, NVMe/SATA SSDs, S.M.A.R.T., and RAID}
\label{sec:ram_storage_hw}

\subsection{Multi-Channel Memory Architectures}
\begin{itemize}
    \item \textbf{Dual-Channel Memory:} Uses two independent 64-bit memory buses operating concurrently, effectively doubling memory bandwidth ($128\text{ bits}$ wide). Requires installing identical memory modules in matched motherboard slots (e.g., Slots A2 and B2).
    \item \textbf{RAM Failure Symptoms:} Blue Screen of Death (BSOD) stop codes (\texttt{MEMORY\_MANAGEMENT}, \texttt{PAGE\_FAULT\_IN\_NONPAGED\_AREA}), random silent data corruption, and failure to complete POST (continuous repeating beep codes).
\end{itemize}

\subsection{Storage Technologies: SATA SSD versus NVMe PCIe SSD}
\begin{table}[htbp]
\centering
\small
\caption{Comparative Analysis: SATA SSD versus NVMe PCIe SSD}
\label{tab:sata_vs_nvme}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Dimension} & \textbf{SATA Solid-State Drive (SSD)} & \textbf{NVMe PCIe Solid-State Drive (SSD)} \\
\midrule
\textbf{Underlying Bus} & Legacy SATA III bus ($6\text{ Gbps}$ physical link). & Direct PCI Express bus ($\times 4$ lanes; Gen 3/4/5). \\
\textbf{Protocol Stack} & Legacy AHCI (designed for mechanical hard disks). & Modern NVMe (Non-Volatile Memory Express). \\
\textbf{Queue Depth} & 1 command queue; maximum 32 commands. & Up to 64,000 command queues; 64,000 commands/queue. \\
\textbf{Max Throughput} & Hard ceiling at $\approx 550\text{ MB/s}$. & Up to $7,000\text{ MB/s}$ (Gen 4) or $14,000\text{ MB/s}$ (Gen 5). \\
\textbf{IOPS Performance} & $\sim 50,000\text{ to } 100,000\text{ IOPS}$. & $>1,000,000\text{ IOPS}$. \\
\textbf{Form Factors} & $2.5\text{ in}$ SATA drive enclosure or M.2 SATA. & M.2 2280 NVMe card, U.2, or PCIe Add-in-Card (AIC). \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{S.M.A.R.T. Drive Health Monitoring}
\textbf{Self-Monitoring, Analysis and Reporting Technology (S.M.A.R.T.)} records internal electromechanical and flash media indicators:
\begin{itemize}
    \item \textbf{Reallocated Sectors Count (HDD):} Indicates surface magnetic platter degradation. A non-zero, rising count mandates immediate drive replacement.
    \item \textbf{Media and Data Integrity Errors (NVMe):} Tracks unrecoverable flash read errors.
    \item \textbf{Available Spare / Percentage Used (SSD):} Indicates remaining flash endurance reserve. When Percentage Used approaches $100\%$, drive writes must be migrated.
\end{itemize}

\subsection{RAID Subsystems for Storage Availability}
\begin{itemize}
    \item \textbf{RAID 0 (Striping):} Splits data across $\ge 2$ drives. Maximum speed, but \textbf{zero fault tolerance} (a single drive failure destroys all data).
    \item \textbf{RAID 1 (Mirroring):} Duplicates identical data across 2 drives. Can tolerate 1 drive failure; total usable capacity is $50\%$.
    \item \textbf{RAID 5 (Distributed Parity):} Block-level striping with distributed XOR parity across $\ge 3$ drives. Can tolerate \textbf{1 drive failure}. Usable capacity: $(N - 1) \times \text{Size}$.
    \item \textbf{RAID 6 (Dual Distributed Parity):} Uses two independent parity blocks across $\ge 4$ drives. Can tolerate \textbf{2 simultaneous drive failures}.
    \item \textbf{RAID 10 (1+0, Mirrored Stripes):} Combines RAID 1 mirroring with RAID 0 striping across $\ge 4$ drives. Delivers high performance and allows recovery from multiple drive failures (provided failed drives are in different mirror sets).
\end{itemize}


\section{BIOS versus UEFI Firmware and MBR versus GPT Partitioning}
\label{sec:firmware_partitioning}

\subsection{BIOS versus UEFI Platform Firmware}
\begin{table}[htbp]
\centering
\small
\caption{System Architecture: Legacy BIOS versus Modern UEFI Firmware}
\label{tab:bios_vs_uefi}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Feature} & \textbf{Legacy BIOS (Basic Input/Output System)} & \textbf{UEFI (Unified Extensible Firmware Interface)} \\
\midrule
\textbf{Processor Mode} & 16-bit Real Mode execution; $1\text{ MB}$ memory limit. & Native 32-bit or 64-bit Protected/Long Mode execution. \\
\textbf{Boot Architecture} & Executes raw machine code from MBR Sector 0. & Executes compiled EFI application binaries from EFI Partition. \\
\textbf{Boot Drive Limit} & $2\text{ TiB}$ limit with standard $512\text{ B}$ sector MBR. & Supports up to $9.4\text{ ZB}$ ($1\text{ ZB} = 10^9\text{ TB}$) via GPT. \\
\textbf{Security Controls} & None; highly vulnerable to bootkit rootkits. & \textbf{Secure Boot} verifies cryptographic digital signatures. \\
\textbf{Legacy Support} & Native legacy operation. & Provides Compatibility Support Module (CSM) if needed. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{MBR versus GPT Disk Partitioning Schemes}
\begin{itemize}
    \item \textbf{Master Boot Record (MBR):} Historical 1983 standard. Stores the partition table inside the first physical 512-byte sector. Limits disks to a maximum of \textbf{4 primary partitions} and \textbf{$2\text{ TiB}$ maximum addressable capacity} due to 32-bit Logical Block Addressing (LBA):
    \[ 2^{32} \text{ sectors} \times 512\text{ bytes/sector} = 2,199,023,255,552\text{ bytes} \approx \mathbf{2.19\text{ TB}} \]
    \item \textbf{GUID Partition Table (GPT):} Part of the UEFI specification. Uses 64-bit LBA (supporting up to $18\text{ EB}$), supports up to \textbf{128 primary partitions} in Windows natively, and maintains backup partition tables at the physical end of the disk for automated redundancy.
\end{itemize}


\section{The Computer Startup Sequence, POST Diagnostics, and Bootstrapping}
\label{sec:boot_sequence}

\subsection{The 10-Phase Hardware Startup Protocol}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Power Switch Assertion:} Front-panel momentary power switch shorts the motherboard \texttt{PWR\_SW} pins, pulling the ATX PSU \texttt{PS\_ON} line low ($0\text{ V}$).
    \item \textbf{Power Good Signal:} The PSU switches on, stabilizes internal DC output voltages ($+12\text{V}, +5\text{V}, +3.3\text{V}$), and asserts the \textbf{\texttt{PWR\_OK} (Power Good)} signal ($+5\text{ V}$) to the motherboard chipset.
    \item \textbf{CPU Reset Release:} Upon receiving \texttt{PWR\_OK}, the motherboard chipset releases the CPU \texttt{RESET} pin. The CPU execution core begins executing instructions at the hardwired \textbf{Reset Vector} address (\texttt{0xFFFFFFF0} in x86).
    \item \textbf{Firmware Initialization:} The CPU executes the initial code from the SPI Flash ROM chip, initializing the chipset, memory controllers, and low-level registers.
    \item \textbf{Power-On Self-Test (POST):} The firmware executes exhaustive hardware diagnostic tests to verify essential subsystem viability:
    \begin{itemize}
        \item Tests CPU registers and ALU flags.
        \item Checks and sizes system RAM via SPD (Serial Presence Detect) probing.
        \item Enumerates PCIe buses and initializes the primary display adapter framebuffer.
        \item Checks keyboard, mouse, and system timers.
    \end{itemize}
    \item \textbf{Diagnostic Video / Beep Output:} If POST succeeds, the firmware initializes video output, displays the OEM splash logo, and emits one short confirmation beep.
    \item \textbf{Boot Device Enumeration:} The UEFI Boot Manager queries non-volatile NVRAM boot variables, scanning NVMe drives, SATA controllers, and network PXE interfaces.
    \item \textbf{Bootloader Execution:}
    \begin{itemize}
        \item \textit{Under UEFI:} Locates the FAT32 \textbf{EFI System Partition (ESP)} and executes the digitally signed EFI boot application (e.g., \texttt{\textbackslash EFI\textbackslash Microsoft\textbackslash Boot\textbackslash bootmgfw.efi} or \texttt{grubx64.efi}).
        \item \textit{Under Legacy BIOS:} Reads Sector 0 (MBR) into memory at address \texttt{0x7C00} and executes the partition boot record.
    \end{itemize}
    \item \textbf{Kernel Initialization:} The bootloader loads the operating system kernel and core device drivers into RAM, transferring hardware execution rights to the OS.
    \item \textbf{User-Space Login:} The OS initializes background system daemons, user services, and renders the graphical login console.
\end{enumerate}


\section{Systematic Boot Failure Troubleshooting}
\label{sec:boot_troubleshooting}

A professional Maintenance Engineer must strictly categorize an inoperative system into one of four mutually exclusive diagnostic domains:

\subsection{The Four Primary Startup Failure Categories}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{No Power:} The system exhibits zero electrical signs of life. No fans rotate, no chassis LEDs illuminate, and the PSU does not respond to the power button.
    \begin{itemize}
        \item \textit{Probable Causes:} Disconnected external mains; blown internal PSU fuse; tripped surge strip; defective front-panel power switch or severed wire; failed motherboard standby circuit.
        \item \textit{Immediate Check:} Test for $+5\text{VSB}$ standby voltage; verify wall socket with known-good device; perform the \textbf{ATX PSU Paperclip Test} (jumper Pin 16 \texttt{PS\_ON} [Green] to Pin 17 \texttt{COM} [Black]) to verify PSU fan spin.
    \end{itemize}
    \item \textbf{No POST:} System powers on (fans spin, LEDs light), but initialization halts before completing POST. No display output, no OEM splash screen, no boot progress.
    \begin{itemize}
        \item \textit{Probable Causes:} Unseated or defective RAM module; CPU socket pin damage; corrupted UEFI firmware; failed VRM phase; incompatible memory timing.
        \item \textit{Diagnostic Approach:} Record motherboard \textbf{Debug LEDs} (CPU, DRAM, VGA, BOOT) or 7-segment hex POST code display; listen for audio beep codes; execute a \textbf{CMOS Clear (CLRTC)} jumper reset to restore factory fail-safe timings; test with a single RAM stick in Slot 2.
    \end{itemize}
    \item \textbf{No Boot:} POST completes successfully (OEM splash screen appears, one short beep emitted), but the operating system fails to load.
    \begin{itemize}
        \item \textit{Error Messages:} \texttt{"No Bootable Device Found"}, \texttt{"Operating System Not Found"}, \texttt{"PXE-E61: Media Test Failure"}.
        \item \textit{Probable Causes:} Disconnected or dead NVMe/SATA drive; corrupted EFI bootloader partition; BIOS/UEFI boot mode mismatch (Legacy MBR selected for a GPT drive); incorrect boot order.
        \item \textit{Diagnostic Approach:} Enter UEFI Setup; verify if physical SSD is detected under SATA/NVMe drive lists; check boot order priorities; repair Windows BCD or GRUB2 bootloader via recovery USB.
    \end{itemize}
    \item \textbf{No Video:} System powers on and appears to boot normally (drive activity LED flashes, OS startup chimes play), but the monitor remains completely dark.
    \begin{itemize}
        \item \textit{Probable Causes:} Monitor switched off or incorrect input source selected (HDMI vs. DisplayPort); display cable loose/damaged; monitor plugged into motherboard video port instead of dedicated discrete GPU; dead GPU fans/power connectors.
        \item \textit{Diagnostic Approach:} Verify monitor power light; test with another video cable; ensure video cable is plugged directly into the discrete GPU backplate.
    \end{itemize}
\end{enumerate}

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Diagnostic Matrix for Computer Startup Failures}
\label{tab:startup_troubleshooting_matrix}
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Failure Category} & \textbf{Observed Hardware Symptoms} & \textbf{Primary Probable Causes} & \textbf{First-Line Corrective Actions} \\
\midrule
\textbf{No Power} & Fans idle; LEDs completely off; zero mechanical response. & Mains disconnected; failed PSU; broken power switch wire. & Verify AC outlet; test $+5\text{VSB}$ standby; perform PSU paperclip test. \\
\textbf{No POST} & Fans spin at $100\%$; black screen; diagnostic beep/LED code. & RAM seating fault; CPU failure; VRM short; corrupted BIOS. & Read motherboard debug LEDs; reseat RAM; clear CMOS; minimum boot config. \\
\textbf{No Boot} & POST splash displays; halts with \texttt{"No Boot Device"}. & Dead SSD/HDD; corrupted bootloader; incorrect boot order. & Verify drive in UEFI; check MBR/GPT mode; rebuild BCD/GRUB via recovery media. \\
\textbf{No Video} & System starts; OS loads; monitor displays \texttt{"No Signal"}. & Cable loose; wrong monitor input; plugged into wrong port. & Reseat HDMI/DP cable; select active monitor input; connect to discrete GPU. \\
\bottomrule
\end{tabularx}
\end{table}
'''
