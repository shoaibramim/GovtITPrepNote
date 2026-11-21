# -*- coding: utf-8 -*-
"""
Module 5 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Contains:
- Section 28: Transformers, Electromagnetic Losses, and Turns Ratios
- Section 29: Electrical Generators and Standby Emergency Systems
- Section 30: AC Induction Motors, Synchronous Speed, Slip, and Single-Phasing
- Section 31: AC Power Triangle, Power Factor Correction, and Three-Phase Power
- Section 32: Uninterruptible Power Supplies (UPS): Topologies, Sizing, and Runtime
- Section 33: Secondary Battery Chemistries (Lead-Acid, Li-ion) and BMS Protection
- Section 34: Switched-Mode Power Supplies (ATX PSU), Rails, VRMs, and 80 PLUS
"""

def get_mod5_tex():
    return r'''
\section{Transformers, Electromagnetic Losses, and Turns Ratios}
\label{sec:transformers}

A \textbf{Transformer} is a static electromagnetic device that transfers alternating electrical energy between two or more coupled circuits via mutual induction, altering voltage and current amplitudes while preserving frequency.

\subsection{Working Principle and the Ideal Transformer Law}
Operating according to \textbf{Faraday's Law of Electromagnetic Induction}, alternating current in the primary winding produces a time-varying magnetic flux $\Phi(t)$ in a high-permeability laminated silicon steel core. This flux links the secondary winding, inducing an electromotive force:
\begin{equation}
\label{eq:transformer_ratio}
\boxed{\frac{V_p}{V_s} = \frac{N_p}{N_s} = a \quad \Longleftrightarrow \quad \frac{I_p}{I_s} = \frac{N_s}{N_p} = \frac{1}{a}}
\end{equation}
where $V_p, V_s$ are primary/secondary voltages, $N_p, N_s$ are turn counts, and $a$ is the turns ratio.
\begin{itemize}
    \item \textbf{Step-Down Transformer ($N_s < N_p \implies V_s < V_p$):} Secondary voltage decreases, while secondary current capacity increases proportionally ($V_p I_p \approx V_s I_s$). Standard in building substations ($11\text{ kV} \to 400\text{ V}/230\text{ V}$) and power supplies.
    \item \textbf{Step-Up Transformer ($N_s > N_p \implies V_s > V_p$):} Increases voltage for high-voltage grid transmission to reduce $I^2R$ transmission line heating.
\end{itemize}

\subsection{Transformer Efficiency and Internal Energy Losses}
The real efficiency of a power transformer is:
\begin{equation}
\label{eq:transformer_eff}
\eta = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\% = \frac{P_{\text{out}}}{P_{\text{out}} + P_{\text{losses}}} \times 100\%
\end{equation}
Internal energy losses fall into two primary physical categories:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Copper Loss (Winding Loss, $P_{\text{Cu}}$):} Ohmic resistance heating in the copper windings:
    \begin{equation}
    \label{eq:copper_loss}
    P_{\text{Cu}} = I_p^2 R_p + I_s^2 R_s
    \end{equation}
    Copper losses are variable and scale quadratically with the load current ($P_{\text{Cu}} \propto I^2$).
    \item \textbf{Core Losses (Iron Losses, $P_{\text{iron}}$):} Occur in the magnetic core and are independent of load:
    \begin{itemize}
        \item \textbf{Hysteresis Loss:} Energy dissipated due to the molecular friction of re-orienting magnetic dipoles every AC cycle. Minimized by using cold-rolled grain-oriented (CRGO) silicon steel.
        \item \textbf{Eddy Current Loss:} Circulating currents induced within the bulk conductive iron core ($P_e \propto f^2 B_m^2 t^2$). Minimized by assembling the core from \textbf{thin laminated sheets} ($0.27$--$0.35\text{ mm}$ thick) coated with insulating varnish.
    \end{itemize}
\end{enumerate}

\subsection{Specialized Transformer Types}
\begin{itemize}
    \item \textbf{Autotransformer:} Uses a single continuous tapped copper winding shared between primary and secondary. Compact, higher efficiency, lower cost; however, it lacks galvanic isolation (a high-voltage primary short propagates directly to the secondary).
    \item \textbf{Galvanic Isolation Transformer ($1:1$ Ratio):} Magnetically couples two electrically isolated circuits, eliminating ground loops and isolating IT equipment from incoming neutral-to-ground noise.
\end{itemize}


\section{Electrical Generators and Standby Emergency Systems}
\label{sec:generators}

An \textbf{Electrical Generator} converts mechanical torque (derived from a diesel engine, gas turbine, or water turbine) into electrical energy via electromagnetic induction.

\subsection{AC Alternator Architecture}
Industrial alternators utilize a \textbf{Rotating Field and Stationary Armature} design:
\begin{itemize}
    \item \textbf{Rotor:} Electromagnet driven by a DC exciter, spun by the diesel prime mover at synchronous speed.
    \item \textbf{Stator (Armature):} Heavy three-phase stationary copper windings embedded in laminated steel slots. Generating high voltages in stationary stator windings avoids transferring large currents through sliding mechanical slip rings.
    \item \textbf{Automatic Voltage Regulator (AVR):} Dynamically adjusts DC rotor field excitation to maintain stable $400\text{ V} \pm 1\%$ output under varying loads.
\end{itemize}

\subsection{Data Center Generator Backup and the Automatic Transfer Switch (ATS)}
In enterprise infrastructure, emergency diesel generators (EDGs) provide prolonged backup during grid blackouts:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item When grid utility power fails, the \textbf{Automatic Transfer Switch (ATS)} detects under-voltage and signals the diesel generator to crank.
    \item The generator starts, reaches operating temperature, and synchronizes voltage/frequency within \textbf{$10$ to $30\text{ seconds}$}.
    \item During this $30$-second startup window, the \textbf{UPS system} carries the entire critical IT load seamlessly from its internal battery reserves.
    \item Once generator output stabilizes, the ATS switches input feeds, and the generator sustains the facility and recharges the UPS batteries.
\end{enumerate}


\section{AC Induction Motors, Synchronous Speed, Slip, and Single-Phasing}
\label{sec:electric_motors}

Electric motors convert electrical energy into mechanical rotation to drive HVAC chillers, server cooling fans, and water pumps.

\subsection{Three-Phase Induction Motor Operation}
The \textbf{Three-Phase Squirrel-Cage Induction Motor} is the universal industrial prime mover:
\begin{itemize}
    \item When balanced three-phase currents enter the stator windings, they establish a \textbf{Rotating Magnetic Field (RMF)} of constant magnitude revolving at \textbf{Synchronous Speed ($N_s$)}:
    \begin{equation}
    \label{eq:synchronous_speed}
    \boxed{N_s = \frac{120 \cdot f}{P}}
    \end{equation}
    where $N_s$ is speed in RPM, $f$ is supply frequency in Hz, and $P$ is the number of magnetic poles.
    \item The RMF sweeps across the rotor bars, inducing heavy currents that interact with the field to generate Lorentz driving torque.
\end{itemize}

\subsection{Rotor Slip ($s$)}
An induction motor can \textbf{never run at synchronous speed} ($N_r < N_s$); if the rotor matched the RMF speed, relative velocity would be zero, inducing zero rotor current and producing zero torque.
The normalized fractional difference in speed is the \textbf{Rotor Slip ($s$)}:
\begin{equation}
\label{eq:motor_slip}
\boxed{s = \frac{N_s - N_r}{N_s} \quad \Longleftrightarrow \quad s\% = \left( \frac{N_s - N_r}{N_s} \right) \times 100\%}
\end{equation}
\begin{equation}
\label{eq:rotor_speed}
\boxed{N_r = N_s (1 - s)}
\end{equation}
where $N_r$ is actual mechanical rotor shaft speed in RPM. (Typical full-load slip ranges from $2\%$ to $5\%$).

\subsection{The Single-Phasing Hazard in Three-Phase Motors}
\textbf{Single-Phasing} occurs when one of the three supply lines to an operating three-phase motor is inadvertently opened (due to a blown fuse, loose terminal, or open contactor pole):
\begin{itemize}
    \item \textit{Operational Result:} The motor cannot generate a rotating field from rest (will not start and hums loudly). If already running, it continues to spin under single-phase pulsating torque, but the remaining two phases must carry \textbf{$\sqrt{3} \times \text{normal current}$ (a $73\%$ current surge)}.
    \item \textit{Thermal Destruction:} Stator winding temperature escalates rapidly; if not disconnected by a thermal overload relay within $30$--$60$ seconds, winding insulation burns out completely.
\end{itemize}


\section{AC Power Triangle, Power Factor Correction, and Three-Phase Power}
\label{sec:power_factor}

In alternating current circuits with reactive components (capacitors and inductors), voltage and current waveforms are displaced by a phase angle $\phi$.

\subsection{The AC Power Triangle}
AC power is resolved into three vector components:
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Real / Active Power ($P$):} The actual average rate of energy converted into mechanical work or heat:
    \begin{equation}
    \label{eq:real_power}
    \boxed{P = V_{\text{RMS}} \cdot I_{\text{RMS}} \cdot \cos\phi \quad \text{[Watts, W]}}
    \end{equation}
    \item \textbf{Reactive Power ($Q$):} The rate of energy stored and returned alternately by inductive and capacitive fields without doing useful work:
    \begin{equation}
    \label{eq:reactive_power}
    \boxed{Q = V_{\text{RMS}} \cdot I_{\text{RMS}} \cdot \sin\phi \quad \text{[Volt-Amperes Reactive, VAR]}}
    \end{equation}
    \item \textbf{Apparent Power ($S$):} The total geometric vector sum of real and reactive power:
    \begin{equation}
    \label{eq:apparent_power}
    \boxed{S = V_{\text{RMS}} \cdot I_{\text{RMS}} \quad \text{[Volt-Amperes, VA]}}
    \end{equation}
    \begin{equation}
    \label{eq:power_triangle_pythagoras}
    \boxed{S^2 = P^2 + Q^2 \quad \Longleftrightarrow \quad S = \sqrt{P^2 + Q^2}}
    \end{equation}
\end{enumerate}

\subsection{Power Factor ($PF$)}
The \textbf{Power Factor} is the dimensionless ratio of real power to apparent power:
\begin{equation}
\label{eq:power_factor_def}
\boxed{PF = \frac{P}{S} = \cos\phi \quad (0 \le PF \le 1.0)}
\end{equation}
\begin{itemize}
    \item \textbf{Lagging Power Factor:} Current lags voltage (inductive loads: motors, transformers, fluorescent ballasts).
    \item \textbf{Leading Power Factor:} Current leads voltage (capacitive loads: long unloaded underground cables).
    \item \textit{Penalties of Low Power Factor:} For an identical useful wattage $P$, drawing current at low $PF$ (e.g., $0.65$) increases line current dramatically ($I = P / (V \cdot PF)$), causing heavy $I^2R$ distribution cable losses, severe voltage drop, and utility financial surcharge penalties.
\end{itemize}

\subsection{Power Factor Correction (PFC)}
Connecting a shunt \textbf{Capacitor Bank} in parallel with inductive loads supplies leading reactive power ($-Q_C$) locally, cancelling the lagging reactive power ($+Q_L$) demanded by induction motors. This raises the overall facility power factor to $\ge 0.95$ without altering motor mechanical output.

\subsection{Three-Phase Balanced Power Equations}
For a balanced three-phase load with line-to-line voltage $V_L$ and line current $I_L$:
\begin{equation}
\label{eq:three_phase_real}
\boxed{P_{3\phi} = \sqrt{3} \cdot V_L \cdot I_L \cdot \cos\phi \quad \text{[Watts]}}
\end{equation}
\begin{equation}
\label{eq:three_phase_apparent}
\boxed{S_{3\phi} = \sqrt{3} \cdot V_L \cdot I_L \quad \text{[VA]}}
\end{equation}


\section{Uninterruptible Power Supplies (UPS): Topologies, Sizing, and Runtime}
\label{sec:ups_systems}

An \textbf{Uninterruptible Power Supply (UPS)} provides conditioned, continuous electrical backup power to critical IT equipment when the incoming utility mains fluctuates or fails completely.

\subsection{The Three Standard UPS Topologies}
\begin{enumerate}[label=\bfseries\arabic*.]
    \item \textbf{Offline / Standby UPS:}
    \begin{itemize}
        \item Under normal conditions, utility AC passes directly to the load via a passive bypass path.
        \item When mains fails, a mechanical transfer switch transfers the load to the inverter.
        \item \textit{Drawback:} \textbf{Transfer Interruption Delay of $4$ to $12\text{ ms}$}. Inadequate for sensitive enterprise servers.
    \end{itemize}
    \item \textbf{Line-Interactive UPS:}
    \begin{itemize}
        \item Features an auto-transformer with an \textbf{Automatic Voltage Regulator (AVR)} tap-changer that corrects sags and swells without draining the battery.
        \item Transfer time: $2$ to $6\text{ ms}$. Standard for network switches and distributed wiring closets.
    \end{itemize}
    \item \textbf{Online Double-Conversion UPS (Enterprise Standard):}
    \begin{itemize}
        \item Continuously rectifies incoming AC mains into clean DC ($AC \to DC$), and a pulse-width-modulated (PWM) inverter converts DC back into pure sinusoidal AC ($DC \to AC$).
        \item \textbf{Zero Transfer Time ($0\text{ ms}$):} Because the inverter continuously supplies the critical load from the internal DC bus, utility failure incurs zero phase disruption.
        \item Completely isolates the IT load from all utility surges, frequency drift, sags, and harmonic distortion.
    \end{itemize}
\end{enumerate}

\subsection{UPS Capacity Sizing: VA versus Watt Sizing}
A critical engineering error in server room planning is conflating a UPS's \textbf{VA rating} with its \textbf{Watt rating}:
\begin{equation}
\label{eq:ups_watt_sizing}
\boxed{\text{Watt Rating (W)} = \text{VA Rating} \times \text{UPS Output Power Factor}}
\end{equation}
\textit{Example:} A $1000\text{ VA}$ UPS with a power factor rating of $0.8$ can support a maximum real load of only $800\text{ W}$. Connecting a modern server cluster drawing $900\text{ W}$ will cause the UPS to trip into overload shutdown, despite $900\text{ W} < 1000\text{ VA}$.

\subsection{Battery Runtime Formulations}
Realistic UPS battery backup runtime incorporates inverter conversion efficiency ($\eta$) and usable battery depth of discharge ($D$):
\begin{equation}
\label{eq:ups_runtime_formula}
\boxed{\text{Runtime (Hours)} \approx \frac{V_{\text{battery}} \times \text{Capacity (Ah)} \times \eta \times D}{\text{Connected Load (Watts)}}}
\end{equation}


\section{Secondary Battery Chemistries and BMS Protection}
\label{sec:batteries}

\subsection{Lead-Acid versus Lithium-Ion Chemistries}
\begin{table}[htbp]
\centering
\small
\caption{Comparative Analysis: Valve-Regulated Lead-Acid (VRLA) versus Lithium-Ion Batteries}
\label{tab:vrla_vs_liion}
\begin{tabularx}{\textwidth}{l X X}
\toprule
\textbf{Metric} & \textbf{VRLA Lead-Acid (AGM / Gel)} & \textbf{Lithium-Ion ($\text{LiFePO}_4$ / NMC)} \\
\midrule
\textbf{Energy Density} & Heavy and bulky ($30$--$50\text{ Wh/kg}$). & High energy density ($100$--$200\text{ Wh/kg}$). \\
\textbf{Service Lifespan} & $3$ to $5$ years before replacement. & $10$ to $15$ years (matches server lifecycle). \\
\textbf{Cycle Life} & $300$ to $500$ cycles at $80\%$ DoD. & $2000$ to $>5000$ cycles at $80\%$ DoD. \\
\textbf{Thermal Sensitivity} & Every $8^{\circ}\text{C}$ rise above $25^{\circ}\text{C}$ cuts lifespan in half. & Operates stably up to $35^{\circ}\text{C}$ with internal BMS. \\
\textbf{Footprint / Weight} & Heavy; requires reinforced data center floors. & $60$--$70\%$ lighter footprint. \\
\textbf{Maintenance} & Manual periodic impedance testing mandatory. & Automated continuous BMS telemetry reporting. \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Battery Management System (BMS)}
Lithium battery systems mandate an intelligent electronic \textbf{BMS} to prevent catastrophic thermal runaway:
\begin{itemize}
    \item Monitors individual cell voltages to within $\pm 1\text{ mV}$.
    \item \textbf{Active/Passive Cell Balancing:} Equalizes state of charge across series cells.
    \item Enforces strict Over-Charge Voltage Protection (OVP), Over-Discharge Protection (UVP), and High-Temperature Cutoff.
\end{itemize}


\section{Switched-Mode Power Supplies (ATX PSU), Rails, VRMs, and 80 PLUS}
\label{sec:psu_vrm}

\subsection{ATX Power Supply Direct Current Voltage Rails}
A computer \textbf{Power Supply Unit (PSU)} utilizes switched-mode power conversion (SMPS) operating at high frequencies ($50\text{ kHz}$ to $>200\text{ kHz}$) to generate tightly regulated DC outputs:
\begin{itemize}
    \item \textbf{$+12\text{ V}$ Rail (Primary Workhorse):} Delivers $>85\%$ of total PSU power; feeds high-current CPU VRMs, PCIe graphics card aux connectors, and cooling fan headers.
    \item \textbf{$+5\text{ V}$ Rail:} Supplies legacy motherboard logic, SATA SSD drive circuitry, and USB ports.
    \item \textbf{$+3.3\text{ V}$ Rail:} Powers motherboard chipsets, PCIe signaling circuitry, and DDR bus logic.
    \item \textbf{$+5\text{ VSB}$ (Standby Rail):} Continuously energized whenever the PSU is plugged into AC mains; powers the Super I/O chip and NIC for Wake-on-LAN (WoL) management.
\end{itemize}

\subsection{Motherboard Voltage Regulator Modules (VRM)}
Modern multi-core processors operate at very low voltages ($0.8\text{ V}$ to $1.3\text{ V}$) but consume massive current surges exceeding $150\text{ A}$ to $300\text{ A}$.
\begin{itemize}
    \item A motherboard \textbf{VRM} is a multi-phase synchronous buck converter that steps down the PSU's $+12\text{ V}$ rail to the exact millivolt-level Vcore demanded by the CPU.
    \item Splitting conversion across $8$ to $16$ interleaved phases reduces thermal stress per MOSFET and cancels input/output ripple current.
\end{itemize}

\subsection{80 PLUS Energy Efficiency Certification}
The \textbf{80 PLUS} standard rates PSU efficiency across $20\%$, $50\%$, and $100\%$ rated loads:
\begin{equation}
\label{eq:psu_efficiency}
\boxed{\eta = \frac{P_{\text{DC Output}}}{P_{\text{AC Input}}} \times 100\%}
\end{equation}
Tier ratings range from \textbf{80 PLUS Bronze} ($\approx 85\%$ efficiency at $50\%$ load) up to \textbf{80 PLUS Titanium} ($\ge 94\%$ efficiency at $50\%$ load). Higher efficiency directly reduces facility HVAC cooling overhead.
'''
