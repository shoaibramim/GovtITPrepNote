# -*- coding: utf-8 -*-
"""
Module 1 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Contains:
- Chapter Title and Introductory Overview
- Section 1: Introduction to Electrical and Electronics Engineering
- Section 2: Fundamental Electrical Quantities and Units
- Section 3: Direct Current (DC) versus Alternating Current (AC) Systems
- Section 4: Ohm's Law and Linear/Non-Linear Circuit Behavior
- Section 5: Series and Parallel Circuit Analysis
- Section 6: Kirchhoff's Current and Voltage Laws
"""

def get_mod1_tex():
    return r'''
\chapter{Electronics, Electrical Engineering, and Computer Hardware}
\label{ch:electronics_electrical_hardware}

This chapter bridges the physical foundations of electrical circuit theory, solid-state electronics, power infrastructure, enterprise computer hardware, structured network cabling, and industrial maintenance engineering. It is systematically organized to address the operational and recruitment requirements for \textbf{Maintenance Engineers, Network Engineers, IT Support Engineers, Hardware Technicians, and Assistant Engineers}.

\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Electrical Engineering Fundamentals and Circuit Theory:} Electric charge, potential, resistance, conductance, Ohm's law, series-parallel configurations, Kirchhoff's laws (KCL/KVL), and AC/DC waveforms.
    \item \textbf{Electrical Protection and Personnel Safety:} Overload vs. short-circuit phenomena, fuses (HRC, cartridge, thermal), MCBs, MCCBs, RCCB/RCD residual current protection, RCBOs, earthing systems (TT, TN-S, TN-C-S), surge protective devices (SPD), and Lockout/Tagout (LOTO) protocols.
    \item \textbf{Solid-State Electronic Components:} PN junction physics, forward/reverse bias, Zener breakdown, Schottky diodes, rectifiers (half-wave, full-wave, bridge) with capacitive filtering, BJTs, MOSFETs, operational amplifiers, and electromechanical relays/contactors.
    \item \textbf{Power Systems and Backup Infrastructure:} Electromagnetic induction, transformer turns/losses, AC alternators, three-phase induction motors (speed and slip), power factor correction, UPS topologies (offline, line-interactive, online double-conversion), batteries (lead-acid, Li-ion, BMS), and ATX power supplies (VRMs, rails, 80 PLUS efficiency).
    \item \textbf{Computer Hardware Architecture and Maintenance:} Motherboards, chipsets, PCIe lane allocation, CPU thermal management, thermal throttling, RAM channels, storage technologies (SATA vs. NVMe SSDs, S.M.A.R.T., RAID), BIOS/UEFI firmware, and MBR vs. GPT partition schemes.
    \item \textbf{Startup Diagnostics and Boot Troubleshooting:} Step-by-step POST initialization, hardware diagnostic categorization (No Power, No POST, No Boot, No Video), diagnostic LEDs, and systematic fault isolation.
    \item \textbf{Network Hardware and Physical Infrastructure:} NICs, switches (managed vs. unmanaged), routers, ONTs, copper twisted-pair categories (Cat5e through Cat8), T568A/B termination, single-mode vs. multi-mode optical fibre, transceivers (SFP/QSFP), Power over Ethernet (802.3af/at/bt), and rack cabling.
    \item \textbf{Instrumentation, Maintenance Engineering, and Reliability:} Multimeters, clamp meters, oscilloscopes, insulation/earth resistance testing, power quality disturbances (sags, swells, harmonics, THD), maintenance paradigms (corrective, preventive, predictive, condition-based), ESD mitigation, and reliability metrics (MTBF, MTTR, Availability $A$).
\end{enumerate}


\section{Introduction to Electrical and Electronics Engineering}
\label{sec:intro_electrical_electronics}

The physical infrastructure of modern enterprise computing relies entirely on the disciplined generation, distribution, conditioning, and semiconductor control of electrical energy.

\subsection{Scope of Electrical Engineering}
\textbf{Electrical Engineering} encompasses the generation, high-voltage transmission, substational distribution, protection, and physical utilization of bulk electrical power. For IT infrastructure and maintenance engineers, electrical engineering governs:
\begin{itemize}
    \item Mains electrical service entrances, distribution panels, and busbar networks.
    \item Three-phase power distribution to server racks and precision air-handling units.
    \item Transformers, standby diesel generators, and automatic transfer switches (ATS).
    \item Centralized battery banks, inverters, and Uninterruptible Power Supply (UPS) systems.
    \item Earthing, lightning dissipation grids, and equipotential ground bonding.
    \item Overcurrent, short-circuit, and residual earth-leakage protective coordination.
\end{itemize}

\subsection{Scope of Electronics Engineering}
\textbf{Electronics Engineering} focuses on the precise manipulation, switching, and amplification of low-power electrical signals using non-linear semiconductor components. Key domains include:
\begin{itemize}
    \item Discrete semiconductor devices: diodes, bipolar transistors, power MOSFETs.
    \item Integrated circuits (ICs): microprocessors, microcontrollers, memory arrays, operational amplifiers.
    \item Switched-mode power supplies (SMPS) and motherboard Voltage Regulator Modules (VRMs).
    \item Analog-to-digital (ADC) and digital-to-analog (DAC) signal conditioning interfaces.
    \item Printed Circuit Board (PCB) layout design, signal integrity, and electromagnetic shielding.
\end{itemize}

\begin{table}[htbp]
\centering
\small
\caption{Comparative Analysis: Electrical Engineering versus Electronics Engineering}
\label{tab:electrical_vs_electronics}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Dimension} & \textbf{Electrical Engineering} & \textbf{Electronics Engineering} \\
\midrule
\textbf{Primary Objective} & Generation, transmission, and delivery of bulk electrical energy. & Processing, transmission, and computation of electrical information/signals. \\
\textbf{Operating Power Levels} & High power (Kilowatts to Megawatts; $230\text{ V}$, $400\text{ V}$, $11\text{ kV}$). & Low power (Milliwatts to Watts; $0.8\text{ V}$, $1.8\text{ V}$, $3.3\text{ V}$, $5\text{ V}$, $12\text{ V}$). \\
\textbf{Fundamental Components} & Generators, transformers, motors, switchgear, heavy cables, contactors. & Diodes, transistors (BJT/MOSFET), operational amplifiers, microchips. \\
\textbf{Conduction Mechanism} & Metallic conductors (electrons) and magnetic fields (flux in steel cores). & Semiconductors (electrons and holes) and dielectric displacement currents. \\
\textbf{Physical Manifestation} & Data center power panels, substation transformers, generator plants. & Server motherboard VRMs, CPU microarchitecture, transceiver modules. \\
\bottomrule
\end{tabularx}
\end{table}


\section{Fundamental Electrical Quantities and Units}
\label{sec:electrical_quantities}

Quantitative electrical engineering models physical phenomena through rigorously standardized SI units and mathematical relationships.

\subsection{Electric Charge ($Q$)}
\textbf{Electric Charge} is the fundamental physical property of subatomic particles that governs their electromagnetic interactions.
\begin{itemize}
    \item Unit: \textbf{Coulomb (C)}.
    \item Elementary charge of an electron: $e^- \approx -1.602 \times 10^{-19}\text{ C}$.
    \item Elementary charge of a proton: $p^+ \approx +1.602 \times 10^{-19}\text{ C}$.
    \item A net charge of $1\text{ C}$ corresponds to the combined charge of approximately $6.242 \times 10^{18}$ electrons.
\end{itemize}

\subsection{Electric Current ($I$)}
\textbf{Electric Current} is the time rate of flow of electric charge through a cross-sectional area of a conducting medium:
\begin{equation}
\label{eq:current_def}
\boxed{I = \frac{dQ}{dt} \quad \xrightarrow{\text{steady state}} \quad I = \frac{Q}{t}}
\end{equation}
where $I$ is current in \textbf{Amperes (A)}, $Q$ is charge in coulombs, and $t$ is time in seconds.
\begin{itemize}
    \item By definition, $1\text{ Ampere} = 1\text{ Coulomb per second } (1\text{ A} = 1\text{ C/s})$.
    \item \textbf{Conventional Current:} Flows from higher electrical potential ($+$) to lower electrical potential ($-$) through the external load circuit.
    \item \textbf{Electron Drift:} In metallic conductors (copper, aluminum), physical electrons drift from negative potential to positive potential (opposite to conventional current).
\end{itemize}

\subsection{Voltage / Electric Potential Difference ($V$)}
\textbf{Voltage} represents the work done or energy transferred per unit charge in moving an infinitesimal test charge between two points in an electric field:
\begin{equation}
\label{eq:voltage_def}
\boxed{V = \frac{dW}{dQ} \quad \xrightarrow{\text{uniform}} \quad V = \frac{W}{Q}}
\end{equation}
where $V$ is electric potential in \textbf{Volts (V)}, $W$ is work/energy in Joules (J), and $Q$ is charge in coulombs.
\begin{itemize}
    \item $1\text{ Volt} = 1\text{ Joule per Coulomb } (1\text{ V} = 1\text{ J/C})$.
    \item Voltage provides the electromotive force (EMF) that drives current through a closed circuit loop.
\end{itemize}

\subsection{Resistance ($R$) and Conductor Resistivity ($\rho$)}
\textbf{Resistance} is the opposition offered by a physical material or component to the flow of electric current, converting electrical energy irreversibly into thermal heat.
\begin{itemize}
    \item Unit: \textbf{Ohm ($\Omega$)}.
    \item For a uniform homogeneous conductor of length $L$ and cross-sectional area $A$:
    \begin{equation}
    \label{eq:resistance_resistivity}
    \boxed{R = \rho \frac{L}{A}}
    \end{equation}
    where $\rho$ is the material's \textbf{Resistivity} (measured in $\Omega\cdot\text{m}$).
    \item \textit{Engineering Implications:}
    \begin{enumerate}[label=\bfseries\alph*.]
        \item Resistance is directly proportional to conductor length $L$ (longer distribution cable runs incur higher voltage drops).
        \item Resistance is inversely proportional to cross-sectional area $A$ (thicker cables with higher gauge/cross-section minimize resistive heating and voltage drops).
        \item Resistivity increases with temperature in pure metals ($\alpha > 0$, positive temperature coefficient of resistance).
    \end{enumerate}
\end{itemize}

\subsection{Electrical Conductance ($G$)}
\textbf{Conductance} quantifies the ease with which electric current flows through a conducting element, defined as the mathematical reciprocal of resistance:
\begin{equation}
\label{eq:conductance_def}
\boxed{G = \frac{1}{R}}
\end{equation}
\begin{itemize}
    \item Unit: \textbf{Siemens (S)} (historically termed mho, $\mho$).
    \item A resistor with $R = 4\ \Omega$ has a conductance of $G = \frac{1}{4} = 0.25\text{ S}$.
\end{itemize}

\subsection{Electric Power ($P$) and Joule Heating}
\textbf{Electric Power} is the time rate at which electrical energy is transferred, dissipated, or converted into work:
\begin{equation}
\label{eq:power_def}
\boxed{P = \frac{dW}{dt} = V \cdot I}
\end{equation}
Substituting Ohm's Law ($V = IR$ or $I = V/R$) yields the classic Joule heating equations for purely resistive loads:
\begin{equation}
\label{eq:power_joule}
\boxed{P = V \cdot I = I^2 R = \frac{V^2}{R}}
\end{equation}
\begin{itemize}
    \item Unit: \textbf{Watt (W)} ($1\text{ W} = 1\text{ J/s} = 1\text{ V}\cdot\text{A}$).
    \item \textit{Practical Example:} An enterprise rack server operates at $230\text{ V}$ and draws $3.5\text{ A}$ of steady-state current. The active power consumption is:
    \[ P = 230\text{ V} \times 3.5\text{ A} = 805\text{ W} \]
\end{itemize}

\subsection{Electrical Energy ($E$) and Commercial Utility Billing}
Electrical energy is the total integral of power consumed over a temporal duration:
\begin{equation}
\label{eq:energy_def}
E = \int_{0}^{t} P(t)\,dt \quad \xrightarrow{\text{constant power}} \quad \boxed{E = P \cdot t = V \cdot I \cdot t}
\end{equation}
\begin{itemize}
    \item SI Unit: \textbf{Joule (J)} ($1\text{ J} = 1\text{ W}\cdot\text{s}$).
    \item \textbf{Commercial Utility Unit (Kilowatt-Hour, kWh):}
    \begin{equation}
    \label{eq:kwh_def}
    1\text{ kWh} = 1000\text{ W} \times 3600\text{ s} = 3.6 \times 10^6\text{ J} = 3.6\text{ MJ}
    \end{equation}
    \begin{equation}
    \label{eq:energy_kwh_formula}
    \text{Energy (kWh)} = \frac{\text{Power (Watts)} \times \text{Operating Time (Hours)}}{1000}
    \end{equation}
\end{itemize}

\textbf{Worked Utility Billing Example:} A data center telecommunications room operates ten 48-port PoE switches, each dissipating $350\text{ W}$, continuously for 30 days ($24\text{ hours/day}$). If the commercial tariff is Tk.~$12.50$ per kWh:
\begin{align*}
\text{Total Power} &= 10 \times 350\text{ W} = 3500\text{ W} = 3.5\text{ kW} \\
\text{Total Operating Hours} &= 30\text{ days} \times 24\text{ hours/day} = 720\text{ hours} \\
\text{Total Energy Consumed} &= 3.5\text{ kW} \times 720\text{ hours} = \mathbf{2520\text{ kWh}} \\
\text{Total Monthly Electricity Cost} &= 2520\text{ kWh} \times \text{Tk. } 12.50/\text{kWh} = \mathbf{\text{Tk. } 31,500}
\end{align*}

\subsection{Frequency ($f$) and Time Period ($T$)}
Periodic alternating signals cycle continuously through symmetrical positive and negative polarities:
\begin{equation}
\label{eq:frequency_period}
\boxed{f = \frac{1}{T} \quad \Longleftrightarrow \quad T = \frac{1}{f}}
\end{equation}
where $f$ is frequency in \textbf{Hertz (Hz)} (cycles per second) and $T$ is the period in seconds.
\begin{itemize}
    \item Standard utility mains in Bangladesh, the UK, Europe, and India operates at $f = 50\text{ Hz}$.
    \[ T = \frac{1}{50\text{ Hz}} = 0.02\text{ s} = \mathbf{20\text{ ms}} \]
    \item North American utility systems operate at $f = 60\text{ Hz}$ ($T \approx 16.67\text{ ms}$).
\end{itemize}

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Summary of Fundamental Electrical Quantities}
\label{tab:electrical_quantities_summary}
\begin{tabularx}{\textwidth}{l c c l X}
\toprule
\textbf{Quantity} & \textbf{Symbol} & \textbf{SI Unit} & \textbf{Unit Symbol} & \textbf{Defining Equation} \\
\midrule
\textbf{Electric Charge} & $Q$ & Coulomb & $\text{C}$ & $Q = \int I\,dt = I \cdot t$ \\
\textbf{Electric Current} & $I$ & Ampere & $\text{A}$ & $I = dQ/dt = V/R$ \\
\textbf{Voltage / Potential} & $V$ & Volt & $\text{V}$ & $V = W/Q = I \cdot R$ \\
\textbf{Resistance} & $R$ & Ohm & $\Omega$ & $R = V/I = \rho L/A$ \\
\textbf{Conductance} & $G$ & Siemens & $\text{S}$ & $G = 1/R = \sigma A/L$ \\
\textbf{Electric Power} & $P$ & Watt & $\text{W}$ & $P = VI = I^2R = V^2/R$ \\
\textbf{Electrical Energy} & $E$ & Joule / kWh & $\text{J}$ & $E = P \cdot t$ \\
\textbf{Frequency} & $f$ & Hertz & $\text{Hz}$ & $f = 1/T = \omega / (2\pi)$ \\
\textbf{Time Period} & $T$ & Second & $\text{s}$ & $T = 1/f$ \\
\bottomrule
\end{tabularx}
\end{table}


\section{Direct Current (DC) versus Alternating Current (AC) Systems}
\label{sec:ac_vs_dc}

\subsection{Direct Current (DC)}
\textbf{Direct Current (DC)} is the unidirectional flow of electric charge. The voltage polarity remains strictly invariant over time.
\begin{itemize}
    \item \textit{Physical Sources:} Chemical galvanic cells (batteries), solar photovoltaic panels, DC generators (dynamos), and AC-to-DC switched-mode power supplies.
    \item \textit{Role in IT Systems:} Powering microprocessors ($0.8$--$1.2\text{ V}$), memory DIMMs ($1.1$--$1.5\text{ V}$), cooling fans ($12\text{ V}$), and telecom backup battery plants ($-48\text{ V DC}$).
\end{itemize}

\subsection{Alternating Current (AC)}
\textbf{Alternating Current (AC)} periodically reverses its direction of flow and continuously varies its magnitude as a sinusoidal function of time:
\begin{equation}
\label{eq:sinusoidal_ac}
\boxed{v(t) = V_m \sin(\omega t + \phi) = V_m \sin(2\pi f t + \phi)}
\end{equation}
where:
\begin{itemize}
    \item $V_m$ is the \textbf{Peak Voltage} (maximum amplitude).
    \item $\omega = 2\pi f$ is the \textbf{Angular Frequency} in radians per second ($\text{rad/s}$).
    \item $f$ is the cyclical frequency in Hertz ($\text{Hz}$).
    \item $\phi$ is the initial phase angle in radians or degrees.
\end{itemize}

\begin{table}[htbp]
\centering
\small
\caption{System Comparison: Alternating Current (AC) versus Direct Current (DC)}
\label{tab:ac_vs_dc}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Feature} & \textbf{Alternating Current (AC)} & \textbf{Direct Current (DC)} \\
\midrule
\textbf{Current Direction} & Reverses direction periodically (50 or 60 times/sec). & Flows strictly in a single, constant direction. \\
\textbf{Voltage Transformation} & Extremely efficient using static electromagnetic transformers. & Requires complex power-electronic DC-DC boost/buck converters. \\
\textbf{Long-Distance Transmission} & Stepped up to ultra-high voltages ($132\text{ kV}$, $400\text{ kV}$) to minimize $I^2R$ line losses. & Used in specialized High Voltage Direct Current (HVDC) undersea links. \\
\textbf{Circuit Interruptibility} & Natural zero-crossing every half cycle aids arc extinction in breakers. & Lacks natural zero-crossing; circuit breaker arcs are difficult to extinguish. \\
\textbf{Primary Domain} & Grid power generation, commercial building distribution. & Microelectronics, internal computer rails, battery storage. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Peak, Peak-to-Peak, and Root-Mean-Square (RMS) Values}
For a sinusoidal voltage waveform:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Peak Voltage ($V_m$):} Maximum instantaneous amplitude measured from the zero axis.
    \item \textbf{Peak-to-Peak Voltage ($V_{pp}$):} Total voltage span between positive and negative crests:
    \begin{equation}
    \label{eq:vpp}
    V_{pp} = 2 V_m
    \end{equation}
    \item \textbf{Root-Mean-Square (RMS / Effective) Voltage ($V_{\text{RMS}}$):} The effective DC equivalent value that delivers the exact same average thermal heating power into an identical resistive load:
    \begin{equation}
    \label{eq:vrms_integral}
    V_{\text{RMS}} = \sqrt{\frac{1}{T} \int_{0}^{T} [v(t)]^2\,dt}
    \end{equation}
    For a pure mathematical sinusoid:
    \begin{equation}
    \label{eq:vrms_sinusoid}
    \boxed{V_{\text{RMS}} = \frac{V_m}{\sqrt{2}} \approx 0.7071 \cdot V_m \quad \Longleftrightarrow \quad V_m = \sqrt{2} \cdot V_{\text{RMS}} \approx 1.4142 \cdot V_{\text{RMS}}}
    \end{equation}
    Similarly, for sinusoidal current: $I_{\text{RMS}} = I_m / \sqrt{2}$.
\end{enumerate}

\textbf{Worked Examination Example:} The single-phase AC utility mains in a server room is specified as $230\text{ V RMS}$ at $50\text{ Hz}$. Calculate the peak voltage and peak-to-peak voltage.
\begin{align*}
V_m &= \sqrt{2} \times V_{\text{RMS}} = 1.4142 \times 230\text{ V} = \mathbf{325.27\text{ V}} \\
V_{pp} &= 2 \times V_m = 2 \times 325.27\text{ V} = \mathbf{650.54\text{ V}}
\end{align*}
\textit{Critical Engineering Trap:} Semiconductor rectifiers and surge protective devices (SPDs) must be rated to withstand the \textbf{Peak Voltage ($>325\text{ V}$)}, not merely the nominal RMS rating.

\subsection{Single-Phase versus Three-Phase Power Supply}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Single-Phase Supply (1-Phase):} Employs one alternating phase conductor ($L$) and one return neutral conductor ($N$). Typically delivers $230\text{ V}$ nominal voltage. Powers workstation PCs, office lighting, and standard $13\text{ A}/16\text{ A}$ wall sockets.
    \item \textbf{Three-Phase Supply (3-Phase):} Employs three separate line conductors ($L_1, L_2, L_3$) delivering sinusoidal voltages of identical amplitude and frequency, but mutually displaced in phase by exactly \textbf{$120^{\circ}$ electrical}:
    \begin{align*}
    v_1(t) &= V_m \sin(\omega t) \\
    v_2(t) &= V_m \sin(\omega t - 120^{\circ}) \\
    v_3(t) &= V_m \sin(\omega t - 240^{\circ}) = V_m \sin(\omega t + 120^{\circ})
    \end{align*}
    \begin{itemize}
        \item In a 400 V three-phase system:
        \begin{itemize}
            \item \textbf{Line-to-Neutral Voltage ($V_{LN}$ / Phase Voltage):} $V_{LN} = 230\text{ V}$.
            \item \textbf{Line-to-Line Voltage ($V_{LL}$):} $V_{LL} = \sqrt{3} \times V_{LN} = \sqrt{3} \times 230\text{ V} \approx 400\text{ V}$.
        \end{itemize}
        \item \textit{Advantages:} Delivers continuous, non-pulsating instantaneous power to balanced loads; requires significantly less copper mass than three equivalent single-phase circuits; natively generates a rotating magnetic field in three-phase induction motors without auxiliary start capacitors.
    \end{itemize}
\end{enumerate}


\section{Ohm's Law and Linear/Non-Linear Circuit Behavior}
\label{sec:ohms_law}

\subsection{Mathematical Formulation}
Formulated by Georg Simon Ohm in 1827, \textbf{Ohm's Law} states that the current flowing through an idealized conducting material between two points is directly proportional to the potential difference across the two points, provided physical conditions (notably temperature) remain constant:
\begin{equation}
\label{eq:ohms_law}
\boxed{V = I \cdot R \quad \Longleftrightarrow \quad I = \frac{V}{R} \quad \Longleftrightarrow \quad R = \frac{V}{I}}
\end{equation}

\subsection{Limitations of Ohm's Law: Non-Ohmic Components}
Ohm's Law applies strictly to \textbf{Ohmic conductors} (e.g., pure metals, carbon resistors) exhibiting a straight-line, linear $V$--$I$ characteristic passing through the origin.
\begin{itemize}
    \item It fails completely for \textbf{Non-Ohmic Devices} whose dynamic resistance $r_d = dV/dI$ varies with operating point, voltage polarity, or temperature:
    \begin{enumerate}[label=\bfseries\alph*.]
        \item \textbf{Semiconductor Diodes:} Current increases exponentially with forward voltage ($I \propto e^{V/V_T}$); zero conduction below barrier potential ($\approx 0.7\text{ V}$).
        \item \textbf{Transistors (BJT / MOSFET):} Current saturates at constant levels independent of collector-emitter or drain-source voltage.
        \item \textbf{Thermistors:} Resistance shifts dramatically non-linearly with temperature (NTC thermistors drop resistance exponentially).
        \item \textbf{Electric Arcs and Gas-Discharge Lamps:} Exhibit \textbf{negative differential resistance} where voltage decreases as current increases.
    \end{enumerate}
\end{itemize}


\section{Series and Parallel Circuit Analysis}
\label{sec:series_parallel}

\subsection{Series Circuits}
In a \textbf{Series Circuit}, electrical elements are chained end-to-end along a single conducting branch:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item Current is identical across all series elements:
    \begin{equation}
    \label{eq:series_current}
    I_{\text{total}} = I_1 = I_2 = \dots = I_n
    \end{equation}
    \item Total equivalent resistance is the direct arithmetic sum of individual resistances:
    \begin{equation}
    \label{eq:series_res}
    \boxed{R_{\text{total}} = R_1 + R_2 + \dots + R_n}
    \end{equation}
    \item Total voltage drops divide across elements (\textbf{Voltage Divider Rule}):
    \begin{equation}
    \label{eq:voltage_divider}
    \boxed{V_k = V_{\text{total}} \cdot \left( \frac{R_k}{R_1 + R_2 + \dots + R_n} \right)}
    \end{equation}
\end{enumerate}

\subsection{Parallel Circuits}
In a \textbf{Parallel Circuit}, all components are connected across the exact same two common electrical nodes:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item Voltage is identical across all parallel branches:
    \begin{equation}
    \label{eq:parallel_voltage}
    V_{\text{total}} = V_1 = V_2 = \dots = V_n
    \end{equation}
    \item The reciprocal of the equivalent resistance equals the sum of individual reciprocals:
    \begin{equation}
    \label{eq:parallel_res}
    \boxed{\frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n} \quad \Longleftrightarrow \quad G_{\text{total}} = \sum_{k=1}^{n} G_k}
    \end{equation}
    For two resistors in parallel:
    \begin{equation}
    \label{eq:two_res_parallel}
    \boxed{R_{\text{total}} = \frac{R_1 \cdot R_2}{R_1 + R_2}}
    \end{equation}
    \item Total branch currents sum to the total supply current (\textbf{Current Divider Rule}):
    \begin{equation}
    \label{eq:current_divider}
    \boxed{I_1 = I_{\text{total}} \cdot \left( \frac{R_2}{R_1 + R_2} \right), \qquad I_2 = I_{\text{total}} \cdot \left( \frac{R_1}{R_1 + R_2} \right)}
    \end{equation}
\end{enumerate}

\begin{table}[htbp]
\centering
\small
\caption{Systemic Comparison: Series versus Parallel Circuit Topologies}
\label{tab:series_vs_parallel}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Parameter} & \textbf{Series Circuit} & \textbf{Parallel Circuit} \\
\midrule
\textbf{Current Path} & Single path; identical current flows through every component. & Multiple independent paths; current divides across branches. \\
\textbf{Voltage Distribution} & Total voltage divides proportionally to resistances ($V_k \propto R_k$). & Identical full supply voltage appears across every branch. \\
\textbf{Equivalent Resistance} & $R_{\text{total}} > \max(R_i)$ (Increases as more loads are added). & $R_{\text{total}} < \min(R_i)$ (Decreases as more loads are added). \\
\textbf{Consequence of Open Fault} & An open circuit anywhere halts all current through the entire chain. & An open branch disconnects only that branch; other branches operate. \\
\textbf{Standard Application} & Sensor loops, fuse links in series with equipment. & Building distribution, server power sockets, motherboard buses. \\
\bottomrule
\end{tabularx}
\end{table}


\section{Kirchhoff's Current and Voltage Laws}
\label{sec:kirchhoffs_laws}

Formulated by Gustav Kirchhoff in 1845, Kirchhoff's laws provide the universal mathematical framework for analyzing complex multi-loop networked circuits.

\subsection{Kirchhoff's Current Law (KCL)}
\textbf{KCL (Nodal Law):} The algebraic sum of all electric currents entering and exiting any circuit node (junction) is identically zero:
\begin{equation}
\label{eq:kcl_formula}
\boxed{\sum_{k=1}^{n} I_k = 0 \quad \Longleftrightarrow \quad \sum I_{\text{entering}} = \sum I_{\text{exiting}}}
\end{equation}
\begin{itemize}
    \item \textbf{Physical Conservation Law:} KCL is a direct mathematical consequence of the \textbf{Law of Conservation of Electric Charge}. Because charge cannot accumulate at an infinitesimal node in steady state, the rate of charge entering must equal the rate of charge departing.
\end{itemize}

\subsection{Kirchhoff's Voltage Law (KVL)}
\textbf{KVL (Loop Law):} The algebraic sum of all electrical potential differences (voltage sources and IR drops) around any closed loop in a circuit network is identically zero:
\begin{equation}
\label{eq:kvl_formula}
\boxed{\sum_{k=1}^{m} V_k = 0 \quad \Longleftrightarrow \quad \sum V_{\text{rises}} = \sum V_{\text{drops}}}
\end{equation}
\begin{itemize}
    \item \textbf{Physical Conservation Law:} KVL is a direct mathematical consequence of the \textbf{Law of Conservation of Energy}. Because an electrostatic field is conservative, moving a unit charge around any complete closed circuit path returns it to its original potential, resulting in zero net work done.
\end{itemize}

\begin{table}[htbp]
\centering
\small
\caption{Comparative Synthesis: Kirchhoff's Current Law versus Kirchhoff's Voltage Law}
\label{tab:kcl_vs_kvl}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Feature} & \textbf{Kirchhoff's Current Law (KCL)} & \textbf{Kirchhoff's Voltage Law (KVL)} \\
\midrule
\textbf{Governing Equation} & $\sum I_{\text{node}} = 0$. & $\sum V_{\text{loop}} = 0$. \\
\textbf{Circuit Location} & Evaluated at a node, junction, or closed boundary. & Evaluated around any closed path, loop, or mesh. \\
\textbf{Physical Foundation} & \textbf{Conservation of Electric Charge}. & \textbf{Conservation of Energy}. \\
\textbf{Circuit Analysis Technique} & Forms the mathematical foundation of \textbf{Nodal Analysis}. & Forms the mathematical foundation of \textbf{Mesh / Loop Analysis}. \\
\bottomrule
\end{tabularx}
\end{table}
'''
