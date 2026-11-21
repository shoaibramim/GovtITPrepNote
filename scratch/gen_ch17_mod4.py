# -*- coding: utf-8 -*-
"""
Module 4 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Contains:
- Section 23: Bipolar Junction Transistors (BJT) and Switching Circuits
- Section 24: Field-Effect Transistors (MOSFET) and Power Switching
- Section 25: Integrated Circuit Architectures and Packaging
- Section 26: Operational Amplifiers (Op-Amps) and Analog Signal Conditioning
- Section 27: Electromechanical Relays, Contactors, and Control Interfacing
"""

def get_mod4_tex():
    return r'''
\section{Bipolar Junction Transistors (BJT) and Switching Circuits}
\label{sec:bjts}

A \textbf{Bipolar Junction Transistor (BJT)} is a three-terminal active semiconductor device in which conduction is governed by both electron and hole charge carriers.

\subsection{Physical Structure and Current Relationships}
A BJT consists of two back-to-back PN junctions sharing a microscopic central semiconductor region:
\begin{itemize}
    \item \textbf{Emitter ($E$):} Heavily doped to inject charge carriers into the base.
    \item \textbf{Base ($B$):} Extremely thin ($<1\ \mu\text{m}$) and lightly doped to minimize carrier recombination.
    \item \textbf{Collector ($C$):} Moderately doped, large physical area to collect carriers and dissipate heat.
\end{itemize}

\textbf{Fundamental BJT Current Equations:}
By Kirchhoff's Current Law:
\begin{equation}
\label{eq:bjt_currents}
\boxed{I_E = I_C + I_B}
\end{equation}
The common-emitter DC current gain ($\beta$ or $h_{FE}$) and common-base gain ($\alpha$) are defined as:
\begin{equation}
\label{eq:bjt_gains}
\boxed{\beta = \frac{I_C}{I_B}, \qquad \alpha = \frac{I_C}{I_E} = \frac{\beta}{\beta + 1}}
\end{equation}
A small base current ($I_B \sim \mu\text{A}$) controls a substantially larger collector current ($I_C \sim \text{mA}$ to $\text{A}$), establishing the BJT as a \textbf{Current-Controlled Device}.

\subsection{Operational Modes and Biasing Regions}
\begin{table}[htbp]
\centering
\small
\caption{BJT Operational Modes and Junction Biasing States}
\label{tab:bjt_modes}
\begin{tabularx}{\textwidth}{l c c X}
\toprule
\textbf{Mode / Region} & \textbf{Base-Emitter (BE)} & \textbf{Base-Collector (BC)} & \textbf{Circuit Function and Electrical Behavior} \\
\midrule
\textbf{Cut-off} & Reverse Biased & Reverse Biased & $I_B = 0, I_C \approx 0$; behaves as an \textbf{Open Switch (OFF)}. \\
\textbf{Active (Linear)} & Forward Biased & Reverse Biased & $I_C = \beta I_B$; linear signal amplification. \\
\textbf{Saturation} & Forward Biased & Forward Biased & Fully conducting; $V_{CE,\text{sat}} \approx 0.2\text{ V}$; \textbf{Closed Switch (ON)}. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{The BJT as an Electronic Saturated Switch}
In digital and control applications, a transistor is switched strictly between Cut-off and Saturation:
\begin{itemize}
    \item \textbf{Logic 0 Input ($V_{\text{in}} < 0.7\text{ V}$):} Transistor is in Cut-off; collector output pulls up to $V_{CC}$ via the pull-up load resistor.
    \item \textbf{Logic 1 Input ($V_{\text{in}} \ge 2.5\text{ V}$):} Adequate base current is injected such that $I_B > I_{C,\text{sat}} / \beta$, driving the transistor into hard Saturation. Output voltage collapses to $V_{CE,\text{sat}} \approx 0.2\text{ V}$.
\end{itemize}


\section{Field-Effect Transistors (MOSFET) and Power Switching}
\label{sec:mosfets}

A \textbf{Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET)} controls current conduction between its \textbf{Drain ($D$)} and \textbf{Source ($S$)} via an electric field established across an ultra-thin silicon dioxide ($\text{SiO}_2$) insulating dielectric gate layer.

\subsection{Enhancement-Mode versus Depletion-Mode MOSFETs}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Enhancement-Mode MOSFET (Normally-OFF):} Standard in digital electronics. At zero gate voltage ($V_{GS} = 0$), no conducting inversion channel exists ($I_D = 0$). When $V_{GS}$ exceeds the positive \textbf{Threshold Voltage ($V_{th}$)}, electrons are attracted under the gate oxide, inverting the p-substrate into an n-channel, permitting heavy drain current.
    \item \textbf{Depletion-Mode MOSFET (Normally-ON):} A physical conducting channel exists at $V_{GS} = 0$. Applying a reverse gate voltage depletes the channel of carriers to choke off current.
\end{enumerate}

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Comparison: BJT versus MOSFET Technologies}
\label{tab:bjt_vs_mosfet}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Characteristic} & \textbf{Bipolar Junction Transistor (BJT)} & \textbf{Field-Effect Transistor (MOSFET)} \\
\midrule
\textbf{Control Parameter} & \textbf{Current-controlled}: $I_C = \beta I_B$. & \textbf{Voltage-controlled}: $I_D \propto (V_{GS} - V_{th})^2$. \\
\textbf{Carrier Physics} & Bipolar: both electrons and holes participate. & Unipolar: majority carriers exclusively. \\
\textbf{Gate Input Impedance} & Low to moderate ($\sim \text{k}\Omega$). & Ultra-high ($>10^{12}\ \Omega$, dielectric insulation). \\
\textbf{Static Control Power} & Continuous DC base current consumed. & Near-zero DC gate current in steady state. \\
\textbf{Switching Speed} & Slower (minority carrier storage time). & Extremely fast (nanoseconds; capacitive charging). \\
\textbf{Thermal Stability} & Negative thermal coefficient (risks \textbf{thermal runaway}). & Positive thermal coefficient ($R_{DS,\text{on}}$ rises with heat; shares current safely in parallel). \\
\textbf{Modern Role} & Analog audio, linear regulators, RF circuits. & Microprocessor logic (CMOS), SMPS, VRMs. \\
\bottomrule
\end{tabularx}
\end{table}


\section{Integrated Circuit Architectures and Packaging}
\label{sec:integrated_circuits}

An \textbf{Integrated Circuit (IC)} integrates millions or billions of microscopic transistors, diodes, resistors, and interconnections onto a single monolithic semiconductor silicon die.

\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Analog ICs:} Process continuous electrical signals (e.g., linear voltage regulators, operational amplifiers, audio preamplifiers).
    \item \textbf{Digital ICs:} Process discrete binary states ($0$ and $1$) (e.g., microprocessors, FPGA logic, NAND flash, DDR SDRAM).
    \item \textbf{Mixed-Signal ICs:} Combine precision analog conditioning with digital DSP engines on the same substrate (e.g., Audio Codecs, ADCs/DACs, Ethernet PHY transceivers).
    \item \textbf{Standard IC Packages:}
    \begin{itemize}
        \item \textbf{DIP (Dual In-line Package):} Through-hole legacy packaging with two parallel rows of pins.
        \item \textbf{QFP / TQFP (Quad Flat Package):} Surface-mount packaging with gull-wing leads on all four perimeters.
        \item \textbf{BGA (Ball Grid Array):} High-density packaging utilizing an array of microscopic solder balls on the underside of the package; standard for modern CPUs, GPUs, and chipsets.
    \end{itemize}
\end{enumerate}


\section{Operational Amplifiers (Op-Amps) and Analog Signal Conditioning}
\label{sec:op_amps}

An \textbf{Operational Amplifier (Op-Amp)} is a high-gain, direct-coupled differential voltage amplifier equipped with two input terminals: an \textbf{Inverting Input ($-$, $V_-$)} and a \textbf{Non-Inverting Input ($+$, $V_+$)}.

\subsection{Ideal Op-Amp Characteristics (The Golden Rules)}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item Infinite Open-Loop Gain: $A_{OL} \to \infty$.
    \item Infinite Input Impedance: $R_{\text{in}} \to \infty \implies$ \textbf{Input Currents are Zero} ($I_+ = I_- = 0$).
    \item Zero Output Impedance: $R_{\text{out}} = 0$.
    \item Infinite Bandwidth and Zero Input Offset Voltage ($V_{\text{out}} = 0$ when $V_+ = V_-$).
    \item \textbf{Virtual Short / Virtual Ground Concept:} In negative feedback, the op-amp actively drives its output to force the differential input voltage to zero:
    \begin{equation}
    \label{eq:virtual_short}
    V_+ \approx V_-
    \end{equation}
\end{enumerate}

\subsection{Standard Linear Op-Amp Configurations}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Inverting Amplifier:} Input applied through resistor $R_{\text{in}}$ to inverting terminal with feedback resistor $R_f$:
    \begin{equation}
    \label{eq:inverting_opamp}
    \boxed{A_v = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_f}{R_{\text{in}}}}
    \end{equation}
    \item \textbf{Non-Inverting Amplifier:} Input applied directly to non-inverting terminal:
    \begin{equation}
    \label{eq:noninverting_opamp}
    \boxed{A_v = \frac{V_{\text{out}}}{V_{\text{in}}} = 1 + \frac{R_f}{R_1}}
    \end{equation}
    \item \textbf{Voltage Follower (Buffer):} $R_f = 0, R_1 \to \infty \implies A_v = 1$. High input impedance isolates sensitive sensor circuits from heavy load loading.
    \item \textbf{Voltage Comparator (Open-Loop):} Operates without negative feedback. Drives the output into positive or negative saturation depending on whether $V_+ > V_-$ or $V_+ < V_-$.
\end{enumerate}


\section{Electromechanical Relays, Contactors, and Control Interfacing}
\label{sec:relays_contactors}

\subsection{Electromechanical Relays}
A \textbf{Relay} is an electrically operated switch where an electrical control current energizes an internal electromagnetic coil, producing magnetic flux that pulls a mechanical armature to close or open electrical contacts.
\begin{itemize}
    \item \textbf{Galvanic Isolation:} Provides complete physical, electrical, and optical isolation ($>2.5\text{ kV}$) between a low-voltage microcontroller logic circuit ($3.3\text{ V} / 5\text{ V}$) and a high-voltage mains AC load ($230\text{ V AC}$).
    \item \textbf{Flyback Diode Requirement:} When the relay coil is de-energized, the collapsing magnetic field generates a massive inductive reverse-voltage spike ($v = -L di/dt > 100\text{ V}$). A \textbf{Flyback Diode} (freewheeling diode) must be connected anti-parallel across the coil to clamp this spike, protecting the driver transistor.
\end{itemize}

\subsection{Contact Classifications}
\begin{itemize}
    \item \textbf{NO (Normally Open):} Contacts remain physically open (non-conducting) when the coil is de-energized; closes when energized.
    \item \textbf{NC (Normally Closed):} Contacts remain closed when de-energized; opens when energized.
    \item \textbf{SPDT (Single Pole Double Throw):} Features a common terminal ($C$) that toggles between an $NC$ contact and an $NO$ contact.
\end{itemize}

\subsection{Power Contactors}
A \textbf{Contactor} is a heavy-duty electromechanical switch specifically engineered for high-current power circuit switching (e.g., $10\text{ A}$ to $>1000\text{ A}$ at $400\text{ V AC}$):
\begin{itemize}
    \item Features heavy silver-alloy contact tips and integrated \textbf{magnetic arc-quenching chutes} to extinguish heavy inductive arcs during contact separation.
    \item Used to control large industrial induction motors, data center backup generators, and UPS automatic transfer switches (ATS).
\end{itemize}
'''
