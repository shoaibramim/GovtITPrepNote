# -*- coding: utf-8 -*-
"""
Module 3 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Contains:
- Section 15: Electronic Components: Passive versus Active Devices
- Section 16: Resistors, Thermistors, and Power Dissipation
- Section 17: Capacitors, Dielectric Physics, Reactance, and ESR
- Section 18: Inductors, Magnetic Storage, and Inductive Reactance
- Section 19: Comparative Synthesis: Resistor versus Capacitor versus Inductor
- Section 20: PN Junction Diodes and Semiconductor Conduction Physics
- Section 21: Specialized Diodes (Zener, Schottky, LED, Photodiode, Varactor)
- Section 22: AC-to-DC Rectification and Capacitive Smoothing Filters
"""

def get_mod3_tex():
    return r'''
\section{Electronic Components: Passive versus Active Devices}
\label{sec:components_overview}

All electronic circuitry is assembled from two fundamental physical categories of discrete components:

\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Passive Components:} Devices that cannot deliver net power gain, inject electrical energy into a circuit, or electronically control current flow without an external stimulus.
    \begin{itemize}
        \item \textit{Primary Roles:} Storing energy in electric/magnetic fields, dissipating power as heat, establishing bias voltages, and filtering frequencies.
        \item \textit{Examples:} Resistors, Capacitors, Inductors, Transformers.
    \end{itemize}
    \item \textbf{Active Components:} Devices capable of electronically controlling the flow of electric charge, providing power amplification, performing high-speed switching, or exhibiting non-linear transfer characteristics.
    \begin{itemize}
        \item \textit{Primary Roles:} Signal amplification, digital logic gate switching, voltage regulation, oscillators.
        \item \textit{Examples:} Bipolar Junction Transistors (BJT), Field-Effect Transistors (MOSFET), Diodes, Operational Amplifiers, Microprocessors.
    \end{itemize}
\end{enumerate}


\section{Resistors, Thermistors, and Power Dissipation}
\label{sec:resistors}

A \textbf{Resistor} is a passive two-terminal component that implements electrical resistance as a circuit element.

\subsection{Standard Resistor Classifications}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Fixed Resistors:} Manufactured to maintain a specified, constant resistance value within a defined tolerance band (e.g., carbon film, metal oxide film, precision wirewound).
    \item \textbf{Variable Resistors:}
    \begin{itemize}
        \item \textbf{Potentiometer:} Three-terminal variable resistor functioning as an adjustable \textbf{Voltage Divider}:
        \[ V_{\text{out}} = V_{\text{in}} \cdot \left( \frac{R_2}{R_1 + R_2} \right) \]
        Used for analog calibration, sensor positioning, and audio gain control.
        \item \textbf{Rheostat:} Two-terminal variable resistor configured to adjust continuous current flow.
    \end{itemize}
    \item \textbf{Thermistors (Temperature-Dependent Resistors):}
    \begin{itemize}
        \item \textbf{NTC (Negative Temperature Coefficient):} Resistance decreases exponentially as temperature rises. Used as \textbf{Inrush Current Limiters} on PSU inputs (high resistance when cold limits capacitor charging surges; drops to near-zero once warmed by operational current).
        \item \textbf{PTC (Positive Temperature Coefficient):} Resistance increases sharply as temperature rises. Used as self-resetting polymer fuses (\textbf{Polyswitches}) for USB port overcurrent protection.
    \end{itemize}
    \item \textbf{Light Dependent Resistors (LDR / Photoresistor):} Cadmium sulfide (CdS) cells whose resistance drops from megohms in darkness to a few hundred ohms under illumination.
\end{enumerate}

\subsection{Thermal Power Dissipation Limits}
Resistors convert electrical energy into heat at rate $P = I^2 R = V^2 / R$. Exceeding a resistor's physical thermal wattage rating ($1/8\text{ W}$, $1/4\text{ W}$, $1\text{ W}$, $5\text{ W}$) causes physical scorching, value drift, and open-circuit burnout.


\section{Capacitors, Dielectric Physics, Reactance, and ESR}
\label{sec:capacitors}

A \textbf{Capacitor} is a passive component consisting of two conducting plates separated by a non-conducting dielectric layer, storing potential energy in an internal electrostatic field.

\subsection{Fundamental Capacitance Equations}
\begin{equation}
\label{eq:capacitance_def}
\boxed{C = \frac{Q}{V} = \varepsilon \frac{A}{d} = \varepsilon_r \varepsilon_0 \frac{A}{d}}
\end{equation}
where $C$ is capacitance in \textbf{Farads (F)}, $A$ is plate area, $d$ is dielectric thickness, and $\varepsilon_r$ is the relative permittivity (dielectric constant).
\begin{itemize}
    \item \textbf{Dynamic $i$--$v$ Characteristic:}
    \begin{equation}
    \label{eq:capacitor_iv}
    \boxed{i(t) = C \frac{dv(t)}{dt}}
    \end{equation}
    Under steady-state DC ($dv/dt = 0$), ideal capacitor current is zero ($i = 0$, acts as an \textbf{open circuit}).
    \item \textbf{Electrostatic Stored Energy:}
    \begin{equation}
    \label{eq:capacitor_energy}
    \boxed{E = \frac{1}{2} C V^2 = \frac{1}{2} \frac{Q^2}{C} = \frac{1}{2} Q V}
    \end{equation}
\end{itemize}

\subsection{Capacitive Reactance ($X_C$)}
In sinusoidal AC circuits, a capacitor opposes current flow with an imaginary impedance termed \textbf{Capacitive Reactance}:
\begin{equation}
\label{eq:capacitive_reactance}
\boxed{X_C = \frac{1}{2\pi f C} = \frac{1}{\omega C}}
\end{equation}
As frequency $f \to \infty$, $X_C \to 0$ (acts as a short circuit to high-frequency AC noise). As $f \to 0$ (DC), $X_C \to \infty$ (blocks DC).

\subsection{Dielectric Capacitor Types}
\begin{itemize}
    \item \textbf{Ceramic Capacitors (MLCC):} Compact, non-polarized, ultra-low ESR; ideal for high-frequency CPU decoupling and motherboard noise bypass.
    \item \textbf{Aluminum Electrolytic Capacitors:} Polarized, high capacitance per volume; liquid electrolyte. Vulnerable to drying out, boiling, and venting under prolonged thermal stress.
    \item \textbf{Solid Polymer Capacitors:} Uses a solid conductive polymer electrolyte; eliminates liquid dry-out, delivering $>5\times$ lifespan and ultra-low ESR on modern server motherboards.
    \item \textbf{Tantalum Capacitors:} Exceptional volumetric efficiency and stability, but fails destructively (short-circuit fire) if reverse-polarized or subjected to overvoltage surges.
\end{itemize}

\subsection{Equivalent Series Resistance (ESR) and Motherboard Capacitor Plague}
Every real-world physical capacitor possesses an internal \textbf{Equivalent Series Resistance (ESR)} representing lead and electrolyte resistance. High ripple current through high ESR produces excessive internal $I^2 \cdot \text{ESR}$ heating:
\begin{itemize}
    \item \textit{Failure Symptoms:} Swollen/bulging aluminum tops, crusty electrolyte leakage, high DC voltage ripple, random server reboots, and failure to complete POST.
\end{itemize}


\section{Inductors, Magnetic Storage, and Inductive Reactance}
\label{sec:inductors}

An \textbf{Inductor} (choke / coil) consists of an insulated wire wound around a magnetic core (ferrite or laminated iron), storing energy in an electromagnetic field.

\subsection{Governing Equations}
\begin{equation}
\label{eq:inductor_iv}
\boxed{v(t) = L \frac{di(t)}{dt}}
\end{equation}
where $L$ is inductance in \textbf{Henrys (H)}.
\begin{itemize}
    \item \textbf{Lenz's Law:} An inductor opposes any sudden change in electric current by inducing a counter-electromotive force (back-EMF). Under steady-state DC ($di/dt = 0$), an ideal inductor behaves as a \textbf{short circuit} ($v = 0$).
    \item \textbf{Magnetic Stored Energy:}
    \begin{equation}
    \label{eq:inductor_energy}
    \boxed{E = \frac{1}{2} L I^2}
    \end{equation}
    \item \textbf{Inductive Reactance ($X_L$):}
    \begin{equation}
    \label{eq:inductive_reactance}
    \boxed{X_L = 2\pi f L = \omega L}
    \end{equation}
    Passes steady DC ($X_L = 0$ at $f = 0$) and blocks high-frequency AC ($X_L \to \infty$).
\end{itemize}


\section{Comparative Synthesis: Resistor versus Capacitor versus Inductor}
\label{sec:rlc_comparison}

\begin{table}[htbp]
\centering
\small
\caption{Comprehensive Synthesis: Resistor, Capacitor, and Inductor Characteristics}
\label{tab:rlc_comparison}
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Property} & \textbf{Resistor ($R$)} & \textbf{Capacitor ($C$)} & \textbf{Inductor ($L$)} \\
\midrule
\textbf{Defining Equation} & $v(t) = i(t) \cdot R$ & $i(t) = C \cdot \frac{dv(t)}{dt}$ & $v(t) = L \cdot \frac{di(t)}{dt}$ \\
\textbf{SI Unit} & Ohm ($\Omega$) & Farad ($\text{F}$) & Henry ($\text{H}$) \\
\textbf{Physical Storage} & None (Dissipates heat). & Electrostatic field ($E = \frac{1}{2}CV^2$). & Electromagnetic field ($E = \frac{1}{2}LI^2$). \\
\textbf{DC Steady State} & Limits current: $I = V/R$. & Open circuit ($I = 0$). & Short circuit ($V = 0$). \\
\textbf{AC Opposition} & Resistance $R$ (frequency independent). & Reactance $X_C = \frac{1}{2\pi f C}$ (decreases with $f$). & Reactance $X_L = 2\pi f L$ (increases with $f$). \\
\textbf{Phase Relationship} & Voltage and current in phase ($0^{\circ}$). & Current leads voltage by $90^{\circ}$. & Voltage leads current by $90^{\circ}$. \\
\textbf{Primary IT Roles} & Pull-up/pull-down bus logic. & DC filtering, transient bypass. & VRM buck converter filtering. \\
\bottomrule
\end{tabularx}
\end{table}


\section{PN Junction Diodes and Semiconductor Conduction Physics}
\label{sec:pn_junction}

\subsection{Semiconductor Materials and Doping}
\begin{itemize}
    \item \textbf{Silicon ($Si$):} Group IV element with 4 valence electrons; bandgap $E_g \approx 1.1\text{ eV}$ at $300\text{ K}$; standard material for digital electronics.
    \item \textbf{N-Type Doping:} Doped with pentavalent donor atoms (Phosphorus, Arsenic). Free electrons are \textbf{majority carriers}; holes are minority carriers.
    \item \textbf{P-Type Doping:} Doped with trivalent acceptor atoms (Boron, Gallium). Holes are \textbf{majority carriers}; electrons are minority carriers.
\end{itemize}

\subsection{The Depletion Region and Potential Barrier}
When P-type and N-type silicon are metallurgically joined, majority electrons diffuse into the P-region and holes diffuse into the N-region, recombining at the metallurgical interface.
\begin{itemize}
    \item This leaves uncompensated, fixed ionized donor ions ($+$) in the N-region and fixed acceptor ions ($-$) in the P-region, creating a space-charge \textbf{Depletion Region}.
    \item The resulting internal electric field establishes a \textbf{Built-in Potential Barrier ($V_0$)}:
    \[ V_{0,\text{Silicon}} \approx 0.7\text{ V}, \qquad V_{0,\text{Germanium}} \approx 0.3\text{ V} \]
\end{itemize}

\subsection{Biasing Configurations}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Forward Bias ($V_D > 0$):} Positive terminal connected to Anode (P-type), negative to Cathode (N-type). The external field opposes the built-in barrier, narrowing the depletion region. Once $V_D \ge 0.7\text{ V}$, heavy forward conduction occurs.
    \item \textbf{Reverse Bias ($V_D < 0$):} Positive connected to Cathode (N-type), negative to Anode (P-type). The external field widens the depletion region, preventing majority carrier flow. Only a tiny minority \textbf{Reverse Saturation Current ($I_S \sim 10^{-12}\text{ A}$)} flows.
\end{enumerate}

\subsection{The Shockley Diode Equation}
\begin{equation}
\label{eq:shockley_diode}
\boxed{I_D = I_S \left( e^{\frac{V_D}{n V_T}} - 1 \right)}
\end{equation}
where $n$ is the ideality factor ($1 \le n \le 2$), and $V_T = \frac{k T}{q}$ is the \textbf{Thermal Voltage} ($\approx 26\text{ mV}$ at room temperature $300\text{ K}$).


\section{Specialized Diodes and Their Applications}
\label{sec:specialized_diodes}

\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Zener Diode:} Heavily doped PN junction designed specifically to operate safely in continuous \textbf{Reverse Breakdown}:
    \begin{itemize}
        \item Below breakdown, acts as an open switch. When reverse voltage reaches the calibrated \textbf{Zener Voltage ($V_Z$)}, current increases sharply while voltage remains clamped precisely at $V_Z$.
        \item Used as precision shunt voltage references and overvoltage clamps.
    \end{itemize}
    \item \textbf{Schottky Barrier Diode:} Formed by a metal-to-semiconductor (e.g., gold-to-n-type silicon) junction:
    \begin{itemize}
        \item \textit{Key Advantages:} Very low forward voltage drop ($V_F \approx 0.2\text{ to } 0.35\text{ V}$) minimizing conduction losses; zero minority carrier storage time, enabling ultra-fast reverse recovery ($<1\text{ ns}$).
        \item Essential in high-efficiency switched-mode power supplies (SMPS) and high-frequency clamping.
    \end{itemize}
    \item \textbf{Light Emitting Diode (LED):} Direct bandgap semiconductor (Gallium Arsenide, Gallium Nitride). When forward-biased, electron-hole recombination releases energy as photons rather than heat.
    \item \textbf{Photodiode:} Reverse-biased PN junction with an optical aperture. Incident photons generate electron-hole pairs in the depletion region, producing reverse photocurrent proportional to light intensity. Used in fiber-optic optical transceivers.
    \item \textbf{Varactor Diode:} Reverse-biased diode operating as a voltage-variable capacitor ($C_T \propto 1/\sqrt{V_R}$), used in RF voltage-controlled oscillators (VCO).
\end{enumerate}


\section{AC-to-DC Rectification and Capacitive Smoothing Filters}
\label{sec:rectifiers}

\subsection{Rectifier Circuit Topologies}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Half-Wave Rectifier:} Uses 1 diode; conducts during positive half-cycles only.
    \begin{equation}
    \label{eq:hwr_vdc}
    V_{\text{DC}} = \frac{V_m}{\pi} \approx 0.318 \cdot V_m, \qquad f_{\text{ripple}} = f_{\text{in}}
    \end{equation}
    Extremely high ripple, poor transformer utilization factor (TUF).
    \item \textbf{Center-Tapped Full-Wave Rectifier:} Uses 2 diodes and a center-tapped transformer winding.
    \begin{equation}
    \label{eq:fwr_vdc}
    V_{\text{DC}} = \frac{2 V_m}{\pi} \approx 0.636 \cdot V_m, \qquad f_{\text{ripple}} = 2 f_{\text{in}}
    \end{equation}
    Each diode must withstand a Peak Inverse Voltage of $\text{PIV} = 2 V_m$.
    \item \textbf{Full-Wave Bridge Rectifier:} Uses 4 diodes in a diamond bridge arrangement. Converts both AC half-cycles with non-center-tapped transformers:
    \begin{equation}
    \label{eq:bridge_vdc}
    V_{\text{DC}} = \frac{2 (V_m - 2 V_D)}{\pi}, \qquad \text{PIV} = V_m, \qquad f_{\text{ripple}} = 2 f_{\text{in}}
    \end{equation}
    Standard input stage in computer PSUs and battery chargers.
\end{enumerate}

\subsection{Capacitive Smoothing Filter and Ripple Formulation}
A high-value electrolytic capacitor connected in parallel with the load charges to the peak voltage $V_m$ and discharges slowly into the load during inter-crest troughs:
\begin{equation}
\label{eq:ripple_voltage}
\boxed{V_{r(pp)} \approx \frac{I_{\text{load}}}{f_{\text{ripple}} \cdot C} = \frac{V_{\text{DC}}}{2 f_{\text{AC}} \cdot R_L \cdot C}}
\end{equation}
where $V_{r(pp)}$ is the peak-to-peak ripple voltage, $I_{\text{load}}$ is load current, $f_{\text{ripple}}$ is ripple frequency ($100\text{ Hz}$ for $50\text{ Hz}$ full-wave), and $C$ is capacitance in Farads.
\begin{itemize}
    \item Larger filter capacitors or higher AC frequencies reduce ripple voltage directly.
\end{itemize}
'''
