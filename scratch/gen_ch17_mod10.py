# -*- coding: utf-8 -*-
"""
Module 10 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Covers Parts 9 & 10:
- Part 9: Examination Numerical Problem Bank (Section 58, 12 Worked Problems)
- Part 10: Theoretical Viva & Recruitment Question Bank (Section 59, 30 Questions),
  Master Cross-Domain Comparison Tables (Section 60), and
  Formula Cheat Sheet with 35 Golden Maintenance Rules/Traps (Section 61).
"""

content = r'''
\section{Comprehensive Worked Numerical Problems}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 1: DC Series-Parallel Circuit Analysis and Power Dissipation}]
\textbf{Problem Statement:} In an industrial control board, three resistors are interconnected. Resistors $R_2 = 30\,\Omega$ and $R_3 = 60\,\Omega$ are connected in parallel with each other. This parallel combination is placed in series with resistor $R_1 = 10\,\Omega$. The entire network is connected across a regulated $V_{\text{DC}} = 60\text{ V}$ power supply. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The total equivalent circuit resistance ($R_{\text{eq}}$).
    \item The total current delivered by the power supply ($I_{\text{total}}$).
    \item The voltage drop across resistor $R_1$ ($V_1$) and across the parallel bank ($V_p$).
    \item The individual branch currents through $R_2$ ($I_2$) and $R_3$ ($I_3$).
    \item The total electrical power dissipated by the circuit ($P_{\text{total}}$).
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The equivalent resistance of the parallel branch ($R_2 \parallel R_3$) is:
    \[
    R_p = \frac{R_2 \times R_3}{R_2 + R_3} = \frac{30 \times 60}{30 + 60} = \frac{1800}{90} = 20\,\Omega
    \]
    Adding series resistor $R_1$:
    \[
    R_{\text{eq}} = R_1 + R_p = 10\,\Omega + 20\,\Omega = \mathbf{30\,\Omega}
    \]
    \item By Ohm's law, total source current is:
    \[
    I_{\text{total}} = \frac{V_{\text{DC}}}{R_{\text{eq}}} = \frac{60\text{ V}}{30\,\Omega} = \mathbf{2.0\text{ A}}
    \]
    \item Voltage drop across $R_1$:
    \[
    V_1 = I_{\text{total}} \times R_1 = 2.0\text{ A} \times 10\,\Omega = \mathbf{20\text{ V}}
    \]
    Voltage drop across the parallel network:
    \[
    V_p = V_{\text{DC}} - V_1 = 60\text{ V} - 20\text{ V} = \mathbf{40\text{ V}} \quad (\text{or } V_p = I_{\text{total}} \times R_p = 2\text{ A} \times 20\,\Omega = 40\text{ V})
    \]
    \item Branch currents through $R_2$ and $R_3$:
    \[
    I_2 = \frac{V_p}{R_2} = \frac{40\text{ V}}{30\,\Omega} = \mathbf{1.333\text{ A}}
    \]
    \[
    I_3 = \frac{V_p}{R_3} = \frac{40\text{ V}}{60\,\Omega} = \mathbf{0.667\text{ A}}
    \]
    \textit{KCL Verification:} $I_2 + I_3 = 1.333 + 0.667 = 2.0\text{ A} = I_{\text{total}}$.
    \item Total power dissipated:
    \[
    P_{\text{total}} = V_{\text{DC}} \times I_{\text{total}} = 60\text{ V} \times 2.0\text{ A} = \mathbf{120\text{ W}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 2: Data Center Server Rack Energy Consumption and Billing}]
\textbf{Problem Statement:} An enterprise server rack contains 10 dual-socket virtualization servers each drawing an average of $450\text{ W}$, two top-of-rack (ToR) 10GbE switches each consuming $120\text{ W}$, and one hardware storage array drawing $660\text{ W}$. The equipment operates continuously 24 hours per day, 30 days per month. The commercial electricity tariff is 8.50 BDT per kilowatt-hour (kWh). Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The total connected power load in kilowatts (kW).
    \item Total electrical energy consumed per 30-day month in kilowatt-hours (kWh).
    \item The total monthly electrical energy cost in BDT.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Total instantaneous power load:
    \[
    P_{\text{servers}} = 10 \times 450\text{ W} = 4,500\text{ W}
    \]
    \[
    P_{\text{switches}} = 2 \times 120\text{ W} = 240\text{ W}
    \]
    \[
    P_{\text{storage}} = 660\text{ W}
    \]
    \[
    P_{\text{total}} = 4,500 + 240 + 660 = 5,400\text{ W} = \mathbf{5.4\text{ kW}}
    \]
    \item Total monthly operational hours:
    \[
    t = 24\text{ hours/day} \times 30\text{ days} = 720\text{ hours}
    \]
    Total energy consumed ($E$):
    \[
    E = P_{\text{total}} \times t = 5.4\text{ kW} \times 720\text{ h} = \mathbf{3,888\text{ kWh}}
    \]
    \item Total monthly electricity bill:
    \[
    \text{Cost} = 3,888\text{ kWh} \times 8.50\text{ BDT/kWh} = \mathbf{33,048\text{ BDT}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 3: AC Waveform Parameter Calculations}]
\textbf{Problem Statement:} A True-RMS multimeter records a single-phase AC mains voltage of $V_{\text{RMS}} = 230\text{ V}$ at $f = 50\text{ Hz}$. Assuming a pure sinusoidal waveform, determine:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Peak voltage ($V_{\text{peak}}$ or $V_m$).
    \item Peak-to-peak voltage ($V_{\text{p-p}}$).
    \item Average voltage over one positive half-cycle ($V_{\text{avg}}$).
    \item Time period ($T$) of one complete AC cycle in milliseconds.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Peak voltage for a sinusoidal wave:
    \[
    V_{\text{peak}} = \sqrt{2} \times V_{\text{RMS}} = 1.4142 \times 230\text{ V} \approx \mathbf{325.27\text{ V}}
    \]
    \item Peak-to-peak voltage:
    \[
    V_{\text{p-p}} = 2 \times V_{\text{peak}} = 2 \times 325.27\text{ V} \approx \mathbf{650.54\text{ V}}
    \]
    \item Average voltage of a half-cycle sine wave:
    \[
    V_{\text{avg}} = \frac{2}{\pi} \times V_{\text{peak}} \approx 0.637 \times 325.27\text{ V} \approx \mathbf{207.20\text{ V}}
    \]
    \item Time period of $50\text{ Hz}$ supply:
    \[
    T = \frac{1}{f} = \frac{1}{50\text{ s}^{-1}} = 0.02\text{ s} = \mathbf{20.0\text{ ms}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 4: Capacitive and Inductive Reactance at Power and High Frequencies}]
\textbf{Problem Statement:} In an electromagnetic filter circuit, a capacitor $C = 10\,\mu\text{F}$ and an inductor $L = 50\text{ mH}$ are utilized. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The capacitive reactance ($X_C$) and inductive reactance ($X_L$) at mains power frequency ($f_1 = 50\text{ Hz}$).
    \item The reactances $X_C$ and $X_L$ at a high switching frequency ($f_2 = 100\text{ kHz}$).
    \item Explain the physical implications for DC blocking and RF filtering based on the results.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item At $f_1 = 50\text{ Hz}$:
    \[
    X_C(50\text{Hz}) = \frac{1}{2\pi f_1 C} = \frac{1}{2 \times \pi \times 50 \times 10 \times 10^{-6}} = \frac{1}{3.1416 \times 10^{-3}} \approx \mathbf{318.31\,\Omega}
    \]
    \[
    X_L(50\text{Hz}) = 2\pi f_1 L = 2 \times \pi \times 50 \times 50 \times 10^{-3} = 314.16 \times 0.05 \approx \mathbf{15.71\,\Omega}
    \]
    \item At $f_2 = 100\text{ kHz} = 10^5\text{ Hz}$:
    \[
    X_C(100\text{kHz}) = \frac{1}{2\pi \times 10^5 \times 10 \times 10^{-6}} = \frac{1}{2\pi} \approx \mathbf{0.159\,\Omega}
    \]
    \[
    X_L(100\text{kHz}) = 2\pi \times 10^5 \times 50 \times 10^{-3} = 2\pi \times 5000 \approx \mathbf{31,415.93\,\Omega} \approx 31.42\text{ k}\Omega
    \]
    \item \textbf{Engineering Significance:} As frequency escalates from $50\text{ Hz}$ to $100\text{ kHz}$, $X_C$ collapses from $318.3\,\Omega$ to almost zero ($0.159\,\Omega$), acting as a direct short-circuit bypass for high-frequency noise. Conversely, $X_L$ surges from $15.7\,\Omega$ to $31.4\text{ k}\Omega$, effectively blocking high-frequency RF ripple from entering the DC circuit.
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 5: Full-Wave Bridge Rectifier and Filter Ripple Voltage}]
\textbf{Problem Statement:} A full-wave bridge rectifier is fed by a transformer secondary delivering $V_{\text{RMS}} = 15\text{ V}$ at $f = 50\text{ Hz}$. The output is smoothed by a reservoir capacitor $C = 4,700\,\mu\text{F}$ and delivers a steady DC load current of $I_{\text{load}} = 2.0\text{ A}$. Assuming silicon diodes with $V_D = 0.7\text{ V}$ forward drop each, calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Peak secondary voltage ($V_m$) and peak rectified DC voltage ($V_{\text{dc,peak}}$).
    \item The ripple frequency ($f_r$) of the bridge rectifier.
    \item The peak-to-peak ripple voltage ($V_{r(pp)}$).
    \item The average DC output voltage ($V_{\text{DC}}$).
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Peak secondary voltage:
    \[
    V_m = \sqrt{2} \times 15\text{ V} \approx 21.21\text{ V}
    \]
    In a bridge rectifier, two diodes conduct simultaneously in series:
    \[
    V_{\text{dc,peak}} = V_m - 2 V_D = 21.21\text{ V} - 2(0.7\text{ V}) = 21.21 - 1.4 = \mathbf{19.81\text{ V}}
    \]
    \item In a full-wave rectifier, ripple frequency is double the line frequency:
    \[
    f_r = 2 \times f = 2 \times 50\text{ Hz} = \mathbf{100\text{ Hz}}
    \]
    \item Peak-to-peak ripple voltage formula:
    \[
    V_{r(pp)} \approx \frac{I_{\text{load}}}{f_r \times C} = \frac{2.0\text{ A}}{100\text{ s}^{-1} \times 4700 \times 10^{-6}\text{ F}} = \frac{2.0}{0.47} \approx \mathbf{4.26\text{ V}}
    \]
    \item Average DC output voltage under load:
    \[
    V_{\text{DC}} = V_{\text{dc,peak}} - \frac{V_{r(pp)}}{2} = 19.81\text{ V} - \frac{4.26\text{ V}}{2} = 19.81 - 2.13 = \mathbf{17.68\text{ V}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 6: Step-Down Transformer Turns Ratio, Current, and Efficiency}]
\textbf{Problem Statement:} A single-phase step-down transformer rated at $2.3\text{ kVA}$ has a primary voltage of $V_p = 230\text{ V}$ and a secondary voltage of $V_s = 24\text{ V}$ at $50\text{ Hz}$. At rated full load with unity power factor ($\cos\phi = 1.0$), the core loss (iron loss) is measured at $P_i = 35\text{ W}$ and full-load copper loss is $P_{cu} = 50\text{ W}$. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The transformer turns ratio ($a = N_p / N_s$).
    \item The rated full-load secondary current ($I_s$) and primary current ($I_p$).
    \item The full-load efficiency ($\eta$) of the transformer.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Turns ratio:
    \[
    a = \frac{N_p}{N_s} = \frac{V_p}{V_s} = \frac{230\text{ V}}{24\text{ V}} \approx \mathbf{9.583 : 1}
    \]
    \item Rated secondary current:
    \[
    I_s = \frac{S}{V_s} = \frac{2,300\text{ VA}}{24\text{ V}} \approx \mathbf{95.83\text{ A}}
    \]
    Rated primary current:
    \[
    I_p = \frac{S}{V_p} = \frac{2,300\text{ VA}}{230\text{ V}} = \mathbf{10.0\text{ A}}
    \]
    \item Full-load useful output power at unity power factor:
    \[
    P_{\text{out}} = S \times \cos\phi = 2,300\text{ VA} \times 1.0 = 2,300\text{ W}
    \]
    Total transformer internal losses:
    \[
    P_{\text{losses}} = P_i + P_{cu} = 35\text{ W} + 50\text{ W} = 85\text{ W}
    \]
    Total input power:
    \[
    P_{\text{in}} = P_{\text{out}} + P_{\text{losses}} = 2,300 + 85 = 2,385\text{ W}
    \]
    Full-load efficiency:
    \[
    \eta = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\% = \frac{2,300}{2,385} \times 100\% \approx \mathbf{96.44\%}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 7: 3-Phase AC Induction Motor Speed and Slip}]
\textbf{Problem Statement:} A 3-phase, 4-pole squirrel-cage induction motor driving a server room HVAC compressor is connected to a $400\text{ V}$, $50\text{ Hz}$ supply. An optical tachometer measures the rotor shaft speed at $N_r = 1,440\text{ RPM}$ under load. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The synchronous speed of the stator magnetic field ($N_s$).
    \item The percentage slip ($s$).
    \item The frequency of the induced rotor currents ($f_r$).
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Synchronous speed formula:
    \[
    N_s = \frac{120 \times f}{P} = \frac{120 \times 50\text{ Hz}}{4\text{ poles}} = \frac{6000}{4} = \mathbf{1,500\text{ RPM}}
    \]
    \item Percentage slip:
    \[
    s = \frac{N_s - N_r}{N_s} \times 100\% = \frac{1,500 - 1,440}{1,500} \times 100\% = \frac{60}{1,500} \times 100\% = \mathbf{4.0\%}
    \]
    \item Rotor induced frequency:
    \[
    f_r = s \times f = 0.04 \times 50\text{ Hz} = \mathbf{2.0\text{ Hz}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 8: Data Center Power Factor Correction}]
\textbf{Problem Statement:} A small enterprise computer facility draws an active real power of $P = 120\text{ kW}$ from a $400\text{ V}$, $50\text{ Hz}$ 3-phase supply at a low lagging power factor of $\cos\phi_1 = 0.72$. Management mandates installing a delta-connected capacitor bank to correct the power factor to $\cos\phi_2 = 0.95$ lagging to eliminate utility penalties. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The initial apparent power ($S_1$) and reactive power ($Q_1$).
    \item The new apparent power ($S_2$) and reactive power ($Q_2$) at $0.95$ power factor.
    \item The required rating of the capacitor bank in kilovars (kVAR).
    \item The reduction in total line current drawn from the main distribution transformer.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Initial state ($\cos\phi_1 = 0.72$):
    \[
    \phi_1 = \arccos(0.72) \approx 43.94^\circ \implies \tan\phi_1 = \tan(43.94^\circ) \approx 0.9637
    \]
    \[
    S_1 = \frac{P}{\cos\phi_1} = \frac{120\text{ kW}}{0.72} \approx \mathbf{166.67\text{ kVA}}
    \]
    \[
    Q_1 = P \times \tan\phi_1 = 120\text{ kW} \times 0.9637 \approx \mathbf{115.64\text{ kVAR}}
    \]
    \item Target state ($\cos\phi_2 = 0.95$):
    \[
    \phi_2 = \arccos(0.95) \approx 18.19^\circ \implies \tan\phi_2 = \tan(18.19^\circ) \approx 0.3287
    \]
    \[
    S_2 = \frac{P}{\cos\phi_2} = \frac{120\text{ kW}}{0.95} \approx \mathbf{126.32\text{ kVA}}
    \]
    \[
    Q_2 = P \times \tan\phi_2 = 120\text{ kW} \times 0.3287 \approx \mathbf{39.44\text{ kVAR}}
    \]
    \item Required capacitor bank rating ($Q_C$):
    \[
    Q_C = Q_1 - Q_2 = 115.64\text{ kVAR} - 39.44\text{ kVAR} = \mathbf{76.20\text{ kVAR}}
    \]
    \item Reduction in 3-phase line current ($I_L = S / (\sqrt{3} \times V_L)$):
    \[
    I_{L1} = \frac{166.67 \times 10^3}{\sqrt{3} \times 400\text{ V}} = \frac{166,670}{692.82} \approx 240.57\text{ A}
    \]
    \[
    I_{L2} = \frac{126.32 \times 10^3}{\sqrt{3} \times 400\text{ V}} = \frac{126,320}{692.82} \approx 182.33\text{ A}
    \]
    \[
    \Delta I_L = 240.57\text{ A} - 182.33\text{ A} = \mathbf{58.24\text{ A (24.2\% current reduction)}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 9: Online UPS Sizing and Battery Backup Runtime}]
\textbf{Problem Statement:} An IT facility houses server hardware demanding an aggregate real power of $P = 6.4\text{ kW}$ with an average power factor of $0.80$ lagging.
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Determine the minimum UPS kVA rating incorporating a $25\%$ engineering expansion headroom factor.
    \item If the UPS DC bus operates at $48\text{ V DC}$ with an inverter full-load efficiency of $\eta_{\text{inv}} = 90\%$, calculate the battery discharge current ($I_{\text{batt}}$) under full load.
    \item Calculate the backup autonomy runtime in minutes provided by a $48\text{ V}$, $100\text{ Ah}$ deep-cycle AGM battery bank assuming Peukert/discharge derating efficiency $\eta_{\text{batt}} = 80\%$.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Apparent power demanded by the load:
    \[
    S_{\text{load}} = \frac{P}{\text{PF}} = \frac{6.4\text{ kW}}{0.80} = 8.0\text{ kVA}
    \]
    Incorporating $25\%$ future headroom (multiplier 1.25):
    \[
    S_{\text{UPS}} = 8.0\text{ kVA} \times 1.25 = \mathbf{10.0\text{ kVA}}
    \]
    \item DC electrical power required by inverter to deliver $6.4\text{ kW}$ output:
    \[
    P_{\text{DC}} = \frac{P_{\text{load}}}{\eta_{\text{inv}}} = \frac{6,400\text{ W}}{0.90} \approx 7,111.11\text{ W}
    \]
    Battery discharge current at nominal $48\text{ V DC}$:
    \[
    I_{\text{batt}} = \frac{P_{\text{DC}}}{V_{\text{DC}}} = \frac{7,111.11\text{ W}}{48\text{ V}} \approx \mathbf{148.15\text{ A}}
    \]
    \item Total usable battery energy capacity:
    \[
    E_{\text{batt}} = V_{\text{DC}} \times \text{Capacity (Ah)} \times \eta_{\text{batt}} = 48\text{ V} \times 100\text{ Ah} \times 0.80 = 3,840\text{ Watt-hours}
    \]
    Runtime ($t$) under $6.4\text{ kW}$ load:
    \[
    t = \frac{E_{\text{batt}}}{P_{\text{DC}}} = \frac{3,840\text{ Wh}}{7,111.11\text{ W}} \approx 0.540\text{ hours} \times 60\text{ min/hour} \approx \mathbf{32.4\text{ minutes}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 10: 80 PLUS PSU Efficiency and Thermal Heat Dissipation}]
\textbf{Problem Statement:} An enterprise server incorporates an 80 PLUS Gold certified power supply. Under steady compute load, the motherboard and internal components draw exactly $P_{\text{DC}} = 540\text{ W}$ across internal $+12\text{V}$, $+5\text{V}$, and $+3.3\text{V}$ rails. At this load level, the PSU exhibits an efficiency of $\eta = 90.0\%$. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The total AC electrical input power drawn from the wall outlet ($P_{\text{AC}}$).
    \item The power dissipated internally as waste heat ($P_{\text{heat}}$) in Watts.
    \item The heat rejection rate in British Thermal Units per hour ($\text{BTU/hr}$), given $1\text{ W} \approx 3.412\text{ BTU/hr}$.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Input AC power:
    \[
    P_{\text{AC}} = \frac{P_{\text{DC}}}{\eta} = \frac{540\text{ W}}{0.90} = \mathbf{600.0\text{ W}}
    \]
    \item Waste heat dissipated by the PSU itself:
    \[
    P_{\text{heat}} = P_{\text{AC}} - P_{\text{DC}} = 600\text{ W} - 540\text{ W} = \mathbf{60.0\text{ W}}
    \]
    \textit{Note:} In an enclosed server chassis, the entire $540\text{ W}$ delivered to silicon components is also ultimately converted into thermal energy, resulting in total server heat generation of $600\text{ W}$.
    \item Total thermal heat rejection to the HVAC system:
    \[
    \text{Heat Rate} = 600\text{ W} \times 3.41214\text{ BTU/(hr}\cdot\text{W)} \approx \mathbf{2,047.3\text{ BTU/hr}}
    \]
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 11: Total Harmonic Distortion (THD) and IEEE 519 Assessment}]
\textbf{Problem Statement:} A power quality analyzer attached to the secondary of a server room isolation transformer records the following harmonic voltage spectrum:
Fundamental ($V_1$) = $230.0\text{ V}$, 3rd Harmonic ($V_3$) = $20.7\text{ V}$, 5th Harmonic ($V_5$) = $11.5\text{ V}$, 7th Harmonic ($V_7$) = $6.9\text{ V}$. All higher harmonics are below $0.5\text{ V}$ and can be ignored. Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The total RMS harmonic voltage ($V_{\text{harmonics}}$).
    \item The Total Harmonic Distortion of the voltage waveform ($\text{THD}_V$).
    \item State whether the system complies with IEEE 519 limits ($\text{THD}_V < 5.0\%$) and recommend engineering remedies if non-compliant.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Total RMS harmonic voltage:
    \[
    V_{\text{harmonics}} = \sqrt{V_3^2 + V_5^2 + V_7^2} = \sqrt{(20.7)^2 + (11.5)^2 + (6.9)^2}
    \]
    \[
    V_{\text{harmonics}} = \sqrt{428.49 + 132.25 + 47.61} = \sqrt{608.35} \approx \mathbf{24.66\text{ V}}
    \]
    \item Total Harmonic Distortion:
    \[
    \text{THD}_V = \frac{V_{\text{harmonics}}}{V_1} \times 100\% = \frac{24.66\text{ V}}{230.0\text{ V}} \times 100\% \approx \mathbf{10.72\%}
    \]
    \item \textbf{Assessment:} With $\text{THD}_V = 10.72\%$, the facility drastically violates the IEEE~519 low-voltage threshold of $5.0\%$. The elevated 3rd harmonic ($9.0\%$ of fundamental) indicates excessive non-linear single-phase SMPS loads overloading the neutral bus. \\
    \textbf{Remedies:} Install an \textbf{Active Power Filter (APF)} to inject anti-phase cancellation currents, utilize a Delta-Wye isolation transformer with a K-factor rating ($K \ge 13$), and double the cross-sectional area of neutral conductors.
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=navyblue,title=\textbf{Problem 12: Reliability Metrics: MTBF, MTTR, and System Availability}]
\textbf{Problem Statement:} A telecommunications data center operates a cluster of 50 access switches running 24 hours per day, 365 days per year ($8,760\text{ operational hours/year}$ per switch). Over a 2-year observation window:
\begin{itemize}
    \item Exactly 12 switch hardware failures occurred across the fleet.
    \item The cumulative downtime spent diagnosing, physically swapping, and reprogramming the failed switches totaled 36 hours.
\end{itemize}
Calculate:
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item The total operating device-hours accumulated by the fleet.
    \item The Mean Time Between Failures (MTBF) of a single switch in hours.
    \item The Mean Time to Repair (MTTR) in hours.
    \item The overall hardware operational availability ($A$) expressed as a percentage.
\end{enumerate}
\textbf{Step-by-Step Solution:}
\begin{enumerate}[label=(\alph*),leftmargin=*]
    \item Total operating device-hours:
    \[
    T_{\text{total}} = 50\text{ units} \times (2\text{ years} \times 8,760\text{ h/year}) = 50 \times 17,520\text{ h} = \mathbf{876,000\text{ operating hours}}
    \]
    \item Mean Time Between Failures (MTBF):
    \[
    \text{MTBF} = \frac{T_{\text{total}}}{\text{Total Failures}} = \frac{876,000\text{ device-hours}}{12\text{ failures}} = \mathbf{73,000\text{ hours}} \quad (\approx 8.33\text{ years per unit})
    \]
    \item Mean Time to Repair (MTTR):
    \[
    \text{MTTR} = \frac{\text{Total Downtime}}{\text{Number of Repairs}} = \frac{36\text{ hours}}{12\text{ repairs}} = \mathbf{3.0\text{ hours}}
    \]
    \item Operational Availability ($A$):
    \[
    A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\% = \frac{73,000}{73,000 + 3} \times 100\% = \frac{73,000}{73,003} \times 100\% \approx \mathbf{99.9959\%}
    \]
    This performance exceeds ``Four Nines'' ($99.99\%$) availability.
\end{enumerate}
\end{tcolorbox}

\section{Theoretical Viva and Interview Questions with Model Answers}

\begin{enumerate}[leftmargin=*,label=\textbf{Q\arabic*.}]
    \item \textbf{Explain the physical difference between an Overload and a Short Circuit, and how a thermal-magnetic MCB protects against both.} \\
    \textbf{Model Answer:} An \textbf{Overload} is an overcurrent condition occurring in an electrically sound circuit where excessive loads are connected, drawing $1.1\text{ to }3\times$ rated current. Heat builds up gradually over seconds or minutes. A \textbf{Short Circuit} occurs when phase conductors make direct contact with negligible impedance (Line-to-Neutral or Line-to-Earth), resulting in instantaneous fault currents of $10\text{ to }100\times$ rated current. \\
    A thermal-magnetic MCB incorporates two tripping elements:
    \begin{itemize}
        \item \textbf{Bimetallic Strip (Thermal Protection):} Two bonded metals with unequal thermal expansion coefficients bend when heated by prolonged overload current, mechanically releasing the trip latch with an inverse-time response ($t \propto 1/I^2$).
        \item \textbf{Electromagnetic Solenoid (Magnetic Protection):} Massive short-circuit currents generate an instantaneous intense magnetic flux, pulling a movable armature to trip the breaker in under $10\text{ to }20\text{ milliseconds}$, quenching the arc in the de-ion arc chute.
    \end{itemize}

    \item \textbf{Why does an RCCB (Residual Current Circuit Breaker) not trip during a standard electrical overload?} \\
    \textbf{Model Answer:} An RCCB contains a Core Balance Current Transformer (CBCT) monitoring the vector sum of currents flowing through the active conductors ($\sum \vec{I} = \vec{I}_L + \vec{I}_N$). Under normal operation or severe overload, current flowing out through the Line conductor returns fully through the Neutral conductor ($I_L - I_N = 0$). The net magnetic flux in the CBCT toroid is zero, inducing no secondary voltage. An RCCB trips \textbf{only} when residual leakage current escapes to earth ($I_L - I_N \ge I_{\Delta n}$, typically $30\text{ mA}$), producing a flux imbalance. To provide combined overload, short circuit, and earth leakage protection, an \textbf{RCBO} must be deployed.

    \item \textbf{Compare TT, TN-S, and TN-C-S earthing systems. Which is preferred for IT data centers and why?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{TT System:} Transformer neutral is grounded; consumer equipment metalwork is connected to an independent local ground rod with no metallic path back to the transformer. Fault loop impedance is high; RCCB is mandatory.
        \item \textbf{TN-S System:} Neutral ($N$) and Protective Earth ($PE$) conductors are \textbf{strictly separated throughout} the entire distribution from transformer to appliance. Preferred for data centers because zero normal load currents flow on the PE conductor, eliminating neutral-to-earth noise, circulating high-frequency ground currents, and RF interference.
        \item \textbf{TN-C-S System (PME):} Combined PEN conductor from utility, split into separate $PE$ and $N$ at consumer main distribution panel. Hazard: If the incoming neutral conductor breaks, all grounded equipment enclosures rise to mains phase potential.
    \end{itemize}

    \item \textbf{Why is an Online Double-Conversion UPS mandatory for enterprise servers, whereas Offline and Line-Interactive UPS units are unacceptable?} \\
    \textbf{Model Answer:} Enterprise server power supplies adhere to the CBEMA / ITIC power curve, tolerating a maximum AC loss of $16\text{ to }20\text{ ms}$ (hold-up time).
    \begin{itemize}
        \item \textbf{Offline UPS:} Exhibits a $4\text{ to }12\text{ ms}$ mechanical transfer switch delay, exposes servers directly to utility surges/sags during normal mode, and produces a stepped square wave on battery.
        \item \textbf{Line-Interactive UPS:} Regulates voltage via an autotransformer (AVR), but still requires $2\text{ to }6\text{ ms}$ transfer time.
        \item \textbf{Online Double-Conversion UPS:} Continuously converts incoming AC to DC, filtering all spikes, transients, and harmonics. The DC bus continuously powers an inverter that regenerates a brand-new, perfect pure sine wave. Because the inverter is permanently online, transfer time upon utility blackout is \textbf{strictly zero milliseconds ($0\text{ ms}$)}, completely isolating sensitive servers from power grid instability.
    \end{itemize}

    \item \textbf{What is the difference between real power (Watts) and apparent power (Volt-Amperes), and why does it matter when sizing a UPS?} \\
    \textbf{Model Answer:} Real power ($P = V \times I \times \cos\phi$) measured in \textbf{Watts (W)} represents actual useful thermodynamic work performed. Apparent power ($S = V \times I$) measured in \textbf{Volt-Amperes (VA)} represents total root-mean-square volt-amperes circulating in the circuit, including reactive power stored in inductors and capacitors. \\
    A UPS is constrained by two independent internal hardware limits: its inverter switching semiconductors (rated in \textbf{kW}) and its magnetic transformer/copper trace current capacity (rated in \textbf{kVA}). Exceeding either the Watt rating or the VA rating trips the internal protection. For example, a $1000\text{ VA}$ UPS with a $0.8$ power factor can only deliver $800\text{ W}$; connecting an $850\text{ W}$ server load with unity power factor will overload the UPS even though $850\text{ VA} < 1000\text{ VA}$.

    \item \textbf{Explain why a flyback diode must always be placed across a DC relay or contactor coil.} \\
    \textbf{Model Answer:} A relay coil is an inductor possessing inductance $L$. When current flows, energy is stored in its magnetic field ($E = \frac{1}{2} L I^2$). When the controlling transistor turns off to de-energize the coil, current attempts to collapse to zero instantly ($di/dt \to -\infty$). By Faraday's and Lenz's laws, the inductor generates a massive reverse back-EMF voltage:
    \[
    V_{\text{induced}} = -L \frac{di}{dt}
    \]
    This inductive kick often reaches $-500\text{ to }-1,000\text{ Volts}$. A flyback (freewheeling) diode is placed in reverse bias across the coil. During normal operation it does not conduct; upon switch opening, it becomes forward-biased by the induced back-EMF, providing a closed loop for the magnetic energy to recirculate and dissipate harmlessly across the coil's internal resistance, protecting the switching transistor from overvoltage breakdown.

    \item \textbf{Differentiate between a BJT and a MOSFET in high-power switching applications.} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{BJT (Bipolar Junction Transistor):} Current-controlled minority carrier device. Requires continuous base drive current ($I_B = I_C / \beta$) to maintain conduction. Suffers from base charge storage time, limiting high-speed switching frequencies. Possesses a negative temperature coefficient (susceptible to thermal runaway when paralleled).
        \item \textbf{MOSFET (Metal-Oxide-Semiconductor FET):} Voltage-controlled majority carrier device. Exhibits virtually infinite DC input gate impedance; current flows only to charge/discharge the gate-source capacitance ($C_{iss}$). Can switch at hundreds of kilohertz (ideal for SMPS). Possesses an on-state channel resistance ($R_{DS(\text{on})}$) with a positive temperature coefficient; as temperature rises, resistance increases, allowing multiple MOSFETs to be safely connected in parallel without current hogging.
    \end{itemize}

    \item \textbf{What is the function of the Voltage Regulator Module (VRM) on a modern motherboard, and why does it require multi-phase design?} \\
    \textbf{Model Answer:} The VRM is a high-frequency synchronous buck converter that steps down the $+12\text{V DC}$ input rail from the ATX power supply to the low core voltage required by modern microprocessors ($0.8\text{ to }1.4\text{ V DC}$), delivering massive transient currents exceeding $150\text{ to }300\text{ Amperes}$. \\
    A multi-phase design interweaves $N$ parallel buck converter phases operating $360^\circ / N$ out of phase:
    \begin{itemize}
        \item It divides total current equally ($I_{\text{phase}} = I_{\text{total}} / N$), dramatically reducing $I^2 R$ heat generation on individual MOSFETs.
        \item It multiplies the effective output ripple frequency by $N$, allowing smaller output capacitors while providing ultra-fast transient recovery during sudden CPU load transitions.
    \end{itemize}

    \item \textbf{Explain the four major startup failure classifications: No Power, No POST, No Boot, and No Video.} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{No Power:} System exhibits zero physical response when pressing the power button: chassis fans do not spin, no LEDs illuminate, PSU fan is stationary. Causes: unplugged cable, blown PSU, shorted motherboard rail, defective power button switch.
        \item \textbf{No POST:} System powers on (fans spin, LEDs light), but hardware initialization halts before firmware diagnostics complete. Diagnostic beep codes or hex debug LEDs freeze. Causes: unseated RAM, bent CPU socket pins, corrupted BIOS ROM.
        \item \textbf{No Boot:} POST passes successfully (single beep), but firmware cannot locate, access, or hand off control to a bootloader. Displays ``Operating System not found'' or ``No bootable device''. Causes: failed SSD/HDD, corrupted EFI system partition, misconfigured boot priority.
        \item \textbf{No Video:} System powers on and completes POST, but the display remains black or enters sleep mode. Causes: defective GPU, unseated PCIe card, faulty display cable, monitor set to wrong input source.
    \end{itemize}

    \item \textbf{Why does an ungrounded or poorly grounded STP cable perform worse than a standard UTP cable?} \\
    \textbf{Model Answer:} Shielded Twisted Pair (STP) relies on an outer metallic foil/braid to absorb external electromagnetic interference (EMI) and divert noise currents harmlessly to telecommunications ground. If the shield is left floating (ungrounded) or grounded only at one end in high-frequency environments, the metallic shield acts as a floating continuous antenna, coupling ambient RF noise into the underlying twisted pairs via capacitive coupling, resulting in worse signal-to-noise ratio (SNR) than an unshielded UTP cable.

    \item \textbf{What is a Split Pair in Ethernet cabling, and why can a basic wiremap tester fail to detect it?} \\
    \textbf{Model Answer:} A \textbf{Split Pair} occurs when individual conductors from two different physical twisted pairs are swapped during termination (e.g., using wire 3 from Pair 2 and wire 6 from Pair 3). In a basic DC continuity wiremap tester, pin-to-pin mapping is 1-to-1 ($1\to 1, 2\to 2, \dots, 8\to 8$), so the tester falsely reports a PASS. However, because differential signals ($\text{Tx}+ / \text{Tx}-$ or $\text{Rx}+ / \text{Rx}-$) are no longer physically twisted around each other, electromagnetic cancellation collapses. The cable suffers catastrophic Near-End Crosstalk (NEXT), causing severe packet loss and preventing Gigabit auto-negotiation.

    \item \textbf{Explain the difference between Single-Mode Fibre (SMF) and Multi-Mode Fibre (MMF) in terms of core diameter and modal dispersion.} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{Single-Mode Fibre (SMF):} Core diameter of $8\text{ to }10\,\mu\text{m}$ (comparable to the optical wavelength). Only one fundamental electromagnetic transverse mode propagates along the central axis. Result: \textbf{Zero modal dispersion}, permitting reaches of $10\text{ to }80+\text{ km}$ at $1310/1550\text{ nm}$.
        \item \textbf{Multi-Mode Fibre (MMF):} Core diameter of $50\,\mu\text{m}$ (OM2/OM3/OM4) or $62.5\,\mu\text{m}$ (OM1). Hundreds of light modes travel simultaneously along different paths at varying angles of reflection. Rays traveling near the core center traverse shorter distances than zigzagging rays near the cladding. This optical path difference creates \textbf{Modal Dispersion} (pulse broadening), restricting transmission reach to $\le 300\text{--}550\text{ meters}$ at $10\text{ Gbps}$.
    \end{itemize}

    \item \textbf{Why does a clamp meter read 0.0 Amperes when clamped around a standard two-conductor desktop power cord?} \\
    \textbf{Model Answer:} Ampère's Circuital Law dictates that the magnetic field measured by the clamp jaw is proportional to the net current passing through its enclosed aperture:
    \[
    \oint \vec{B} \cdot d\vec{\ell} = \mu_0 \sum I
    \]
    In a single-phase appliance power cord, the current flowing into the appliance through the Line wire ($I_L$) is equal in magnitude and opposite in direction to the returning current in the Neutral wire ($I_N$). Enclosing both conductors yields $\sum I = I_L - I_N = 0$. The magnetic fluxes cancel out. To measure load current, the clamp must encircle \textbf{only one isolated conductor} (Line or Neutral) or use an AC line splitter.

    \item \textbf{What are Triplen Harmonics, and why do they cause neutral conductors to burn out in three-phase IT distribution boards?} \\
    \textbf{Model Answer:} Triplen harmonics are odd integer multiples of the 3rd harmonic ($n = 3, 9, 15, 21, \dots$). In a balanced 3-phase system, fundamental currents are separated by $120^\circ$ and sum to zero in the neutral wire ($I_N = 0$). However, multiplying $120^\circ$ by 3 yields $360^\circ \equiv 0^\circ$. Therefore, triplen harmonics in all three phases are completely in phase with each other. Instead of canceling, they \textbf{add arithmetically} in the neutral conductor:
    \[
    I_{N(\text{triplen})} \approx I_{3A} + I_{3B} + I_{3C}
    \]
    In computer facilities with high concentrations of single-phase switch-mode power supplies, neutral current can reach up to $173\%$ of phase current, causing severe overheating and fires unless a $200\%$ double-sized neutral bus is installed.

    \item \textbf{What is the safety function of the $1\text{ M}\Omega$ resistor embedded in an anti-static ESD wrist strap?} \\
    \textbf{Model Answer:} The $1\text{ M}\Omega$ series resistor serves a vital life-safety purpose:
    \begin{itemize}
        \item \textbf{Static Discharge:} For high-voltage electrostatic charges ($10\text{ kV}$), discharging through $1\text{ M}\Omega$ yields an $RC$ time constant of microseconds ($t \approx RC \approx 10^6 \times 100 \times 10^{-12} = 100\,\mu\text{s}$), draining static safely without sparking.
        \item \textbf{Mains Shock Protection:} If a technician wearing the strap accidentally touches a live $230\text{ V AC}$ mains wire, the $1\text{ M}\Omega$ resistor limits the current passing through the human body to earth to:
        \[
        I = \frac{230\text{ V}}{1,000,000\,\Omega} = 0.23\text{ mA}
        \]
        This current is far below the human threshold of perception ($1\text{ mA}$) and orders of magnitude below the ventricular fibrillation threshold ($10\text{ to }50\text{ mA}$). A solid zero-ohm wire would cause lethal electrocution.
    \end{itemize}

    \item \textbf{Why does spinning a cooling fan with compressed air pose a severe danger to a motherboard?} \\
    \textbf{Model Answer:} A computer cooling fan contains a brushless DC permanent-magnet motor. Forcing the fan blades to rotate at extreme velocities using high-pressure compressed air turns the motor into an electrical \textbf{generator} (dynamo). The rapid change in magnetic flux induces a large reverse electromagnetic force (\textbf{Back-EMF}) voltage exceeding $+15\text{ to }24\text{ V}$. This voltage spike is fed directly back through the motherboard's 3-pin or 4-pin fan header, destroying the surface-mount speed-sensing circuitry, PWM controller, or Super I/O ASIC. Fan blades must always be mechanically immobilized during cleaning.

    \item \textbf{Explain the difference between Catastrophic and Latent ESD failures.} \\
    \textbf{Model Answer:} A \textbf{Catastrophic ESD failure} causes immediate, total, and permanent component breakdown (e.g., vaporized internal silicon trace or punctured gate oxide); the component fails to power on immediately. A \textbf{Latent ESD failure} occurs when electrostatic discharge causes partial microscopic damage (sub-micron cratering or lattice dislocation) without immediate operational failure. The device passes diagnostic tests and enters service. However, continuous electrical current and thermal expansion cycles accelerate electromigration across the weakened junction, causing random crashes, bit flips, or sudden complete failure weeks or months later.

    \item \textbf{What is the difference between MBR and GPT partition tables, and why is GPT mandatory for drives larger than 2 TiB?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{MBR (Master Boot Record):} Uses a 32-bit field to record sector addresses (Logical Block Addressing, LBA). With standard 512-byte sectors, the maximum addressable storage capacity is:
        \[
        2^{32} \times 512\text{ bytes} = 4,294,967,296 \times 512 = 2,199,023,255,552\text{ bytes} = \mathbf{2\text{ TiB}}
        \]
        Any storage capacity beyond $2\text{ TiB}$ is completely unaddressable. MBR is also limited to 4 primary partitions and stores a single partition table at Sector 0 with zero redundancy.
        \item \textbf{GPT (GUID Partition Table):} Uses 64-bit LBA addressing, supporting storage capacities up to $2^{64} \times 512\text{ bytes} \approx 9.4\text{ ZB}$ ($9.4 \times 10^{21}\text{ bytes}$). Supports up to 128 partitions in Windows, utilizes CRC32 checksums to detect table corruption, and stores a backup copy of the partition table at the end of the physical disk.
    \end{itemize}

    \item \textbf{Explain how Thermal Throttling protects a modern CPU from destruction.} \\
    \textbf{Model Answer:} Modern microprocessors incorporate embedded on-die digital thermal sensors (DTS) located directly inside high-power execution units. When core temperatures approach the maximum safe silicon junction threshold ($T_{j\text{,max}}$, typically $100^\circ\text{C}\text{ to }105^\circ\text{C}$), the CPU's internal power management controller triggers \textbf{Thermal Throttling}:
    \begin{itemize}
        \item It dynamically lowers the internal clock multiplier, reducing CPU operating frequency (e.g., dropping from $4.8\text{ GHz}$ down to $1.2\text{ GHz}$ or base clock).
        \item It lowers operating core voltage ($V_{\text{core}}$) via Dynamic Voltage and Frequency Scaling (DVFS).
        \item Because dynamic CMOS power dissipation scales as $P \approx C V^2 f$, reducing frequency and voltage causes power consumption and heat generation to plummet.
        \item If temperature continues rising past critical shutdown limits ($T_{\text{crit}} \approx 115^\circ\text{C}$), the processor asserts the \texttt{THERMTRIP\#} hardware signal, immediately cutting VRM power to prevent catastrophic silicon vaporization.
    \end{itemize}

    \item \textbf{Why does an NVMe SSD dramatically outperform a SATA SSD in enterprise database environments?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{Physical Interface and Bandwidth:} SATA~3.0 operates over a legacy serial bus capped at $6.0\text{ Gbps}$ ($600\text{ MB/s}$ theoretical, $\approx 550\text{ MB/s}$ practical). NVMe connects directly to the CPU via PCI Express (PCIe Gen~4 $\times4$ provides $\approx 8,000\text{ MB/s}$; Gen~5 $\times4$ provides $\approx 16,000\text{ MB/s}$).
        \item \textbf{Command Queues and Parallelism:} SATA uses the legacy AHCI protocol designed for rotating magnetic platters, limited to a single command queue holding up to 32 commands ($1\times 32$). NVMe supports up to \textbf{64,000 independent command queues}, each capable of holding \textbf{64,000 concurrent commands}, perfectly matching multi-core CPU architecture and parallel NAND flash channels.
        \item \textbf{Latency:} Direct memory-mapped registers over PCIe bypass the Southbridge/PCH SATA controller, reducing command overhead and latency from $\approx 20\text{--}30\,\mu\text{s}$ down to $<5\text{--}10\,\mu\text{s}$.
    \end{itemize}

    \item \textbf{What is the difference between a Straight-Through cable and a Crossover cable? Under what circumstances is a crossover cable still physically required?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{Straight-Through Cable:} Both ends terminated using the same wiring standard (T568A--T568A or T568B--T568B). Connects MDI devices to MDI-X devices (e.g., PC to Switch).
        \item \textbf{Crossover Cable:} One end terminated as T568A, the other as T568B. Transmit pairs (Pins 1 and 2) cross over to receive pairs (Pins 3 and 6). Connects like devices (Switch to Switch, PC to PC).
        \item \textbf{Requirement:} Virtually all modern 1000BASE-T (Gigabit) and 10GBASE-T transceivers incorporate \textbf{Auto-MDIX}, which detects and configures transmit/receive assignments in hardware automatically. A physical crossover cable is only required when interconnecting legacy 10/100BASE-TX devices that lack Auto-MDIX support.
    \end{itemize}

    \item \textbf{How does Power over Ethernet (PoE) deliver 48V DC power over twisted pairs without destroying non-PoE network cards?} \\
    \textbf{Model Answer:} IEEE 802.3af/at/bt incorporates an active \textbf{Hardware Resistive Handshake} protocol before applying full operating voltage:
    \begin{enumerate}
        \item \textbf{Detection Phase:} The PSE injects a harmless low voltage ($2.7\text{ to }10.1\text{ V DC}$) and measures the loop resistance. A valid Powered Device (PD) presents a specific characteristic signature resistance of exactly \textbf{$25.0\text{ k}\Omega \pm 5\%$}.
        \item If an ordinary non-PoE device or standard PC NIC is connected, it presents a short circuit ($0\,\Omega$) or open circuit ($\infty$), and the PSE \textbf{withholds power}, transmitting standard data signals safely.
        \item \textbf{Classification Phase:} If the $25\text{ k}\Omega$ signature is validated, the PSE steps voltage up to $15\text{ to }20\text{ V}$ to read the PD's classification current (Class 0 through Class 8), establishing the power budget.
        \item \textbf{Power Delivery:} Only after classification is verified does the PSE ramp voltage up to full operating level ($48\text{ to }57\text{ V DC}$).
    \end{enumerate}

    \item \textbf{Explain the formula for System Operational Availability ($A$) and calculate the annual downtime of a system with ``Five Nines'' availability.} \\
    \textbf{Model Answer:} System Availability ($A$) is:
    \[
    A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\%
    \]
    ``Five Nines'' availability corresponds to $A = 99.999\%$.
    In an operational year of 365 days ($8,760\text{ hours} = 525,600\text{ minutes}$):
    \[
    \text{Unavailability} = 100\% - 99.999\% = 0.001\% = 10^{-5}
    \]
    \[
    \text{Permitted Downtime} = 525,600\text{ minutes} \times 0.00001 = \mathbf{5.256\text{ minutes/year (5 minutes, 15 seconds)}}
    \]

    \item \textbf{What is the difference between an Isolation Transformer and an Autotransformer? When must an autotransformer never be used?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{Isolation Transformer:} Primary and secondary windings are physically and galvanically separated. Energy transfers exclusively through magnetic flux in the core. Breaks ground loops, blocks common-mode noise, and creates a newly derived neutral-earth reference for sensitive IT equipment.
        \item \textbf{Autotransformer:} Consists of a \textbf{single continuous winding} shared by both primary and secondary circuits; the secondary voltage is tapped off a portion of the single coil. Smaller, lighter, and more efficient.
        \item \textbf{Critical Prohibition:} An autotransformer provides \textbf{zero galvanic isolation}. The primary and secondary share a direct electrical conductor. It must \textbf{never} be used where galvanic isolation is required for life safety, in medical electronic applications, or where input and output earthing systems must remain isolated.
    \end{itemize}

    \item \textbf{Explain how a Time-Domain Reflectometer (TDR) detects the exact physical location of a copper cable break.} \\
    \textbf{Model Answer:} A TDR functions like radar for transmission lines. It injects a sharp, high-frequency electrical voltage pulse down the cable and monitors reflections caused by characteristic impedance discontinuities ($\Delta Z_0$).
    \begin{itemize}
        \item When the pulse encounters an \textbf{Open Circuit} ($Z_L = \infty$), the reflection coefficient is $\Gamma = +1$, reflecting an in-phase positive pulse.
        \item When it encounters a \textbf{Short Circuit} ($Z_L = 0$), $\Gamma = -1$, reflecting an inverted negative pulse.
        \item By measuring the elapsed round-trip transit time ($\Delta t$) and knowing the cable's Nominal Velocity of Propagation (NVP, typically $0.65\text{ to }0.72\times c$), the TDR computes distance:
        \[
        D = \frac{v \times \Delta t}{2} = \frac{(\text{NVP} \times c) \times \Delta t}{2}
        \]
    \end{itemize}

    \item \textbf{Why does an enterprise server motherboard use ECC (Error-Correcting Code) memory instead of standard non-ECC RAM?} \\
    \textbf{Model Answer:} Non-ECC memory cannot detect or correct single-bit memory corruptions caused by cosmic alpha particles, electromagnetic noise, or thermal instability. If a bit flips in operating system kernel space, the server immediately triggers a Kernel Panic or Blue Screen of Death (BSOD), causing catastrophic downtime. \\
    ECC memory adds 8 additional check bits per 64-bit data word (72 bits total). The memory controller uses \textbf{Single-Error Correction, Double-Error Detection (SECDED)} Hamming code algorithms:
    \begin{itemize}
        \item It detects and \textbf{transparently corrects} any single-bit error on the fly with zero performance impact and zero system downtime.
        \item It detects double-bit errors and alerts the operating system to initiate an orderly failover before corrupted data is written to persistent storage.
    \end{itemize}

    \item \textbf{What is the difference between an air-gap lightning arrestor and a Metal Oxide Varistor (MOV) based Surge Protective Device (SPD)?} \\
    \textbf{Model Answer:}
    \begin{itemize}
        \item \textbf{Spark Gap Arrestor (Type 1 SPD):} Consists of two electrodes separated by a dielectric air/gas gap. In response to massive direct lightning impulses ($10/350\,\mu\text{s}$ waveform), the air ionizes into a conductive plasma arc, diverting tens of kiloamperes to earth. Response time is relatively slow ($100\text{ ns}$), and it produces a power-frequency follow-through current that must be quenched.
        \item \textbf{MOV (Metal Oxide Varistor, Type 2/3 SPD):} Consists of a sintered zinc oxide (ZnO) ceramic semiconductor disk. Under normal operating voltages, it presents mega-ohms of resistance (leakage current microamperes). When voltage spikes exceed its clamping threshold, it transitions to a highly conductive state in \textbf{under 25 nanoseconds}, clamping transient voltage to a safe level ($V_{\text{clamp}}$). It degrades over time as repeated surges deplete its internal grain boundaries.
    \end{itemize}

    \item \textbf{Explain the physical meaning of S.M.A.R.T. Attribute 05 (Reallocated Sector Count) in mechanical HDDs and SSDs.} \\
    \textbf{Model Answer:} In mechanical HDDs, Attribute 05 records the number of damaged physical sectors that have been retired and remapped to spare reserve tracks by drive microcode after write/read verification failure. A value of zero indicates pristine platter surface. When this counter begins incrementing ($>0$), platter surface degradation is underway; head crashes or complete storage failure are statistically imminent. In SSDs, Attribute 05 represents flash memory blocks that have failed program/erase (P/E) cycles and been remapped to the over-provisioned reserve pool.

    \item \textbf{What is the function of the CMOS/RTC coin cell battery (CR2032) on a computer motherboard?} \\
    \textbf{Model Answer:} The CR2032 lithium coin cell ($3.0\text{ V}$, $\approx 220\text{ mAh}$) powers the Real-Time Clock (RTC) oscillator crystal ($32.768\text{ kHz}$) and maintains low-power complementary metal-oxide-semiconductor (CMOS) volatile configuration registers when main AC power is completely disconnected from the power supply. When the battery depletes below $\approx 2.4\text{ V}$, the system clock resets to factory epoch (e.g., January 1, 2000), triggering SSL/TLS certificate validation failures during HTTPS browsing, and BIOS prompts ``CMOS Checksum Error -- Press F1 to Run Setup''.

    \item \textbf{Why must single-phasing be immediately prevented in 3-phase induction motors?} \\
    \textbf{Model Answer:} \textbf{Single-phasing} occurs when one of the three supply lines to a running 3-phase motor is severed (e.g., due to a blown single fuse or broken conductor). The motor cannot produce a rotating magnetic field; it only produces a pulsating field.
    \begin{itemize}
        \item If running when single-phasing occurs, the motor continues rotating, but the remaining two phase windings must draw $\sqrt{3} \times I_{\text{normal}} \approx \mathbf{1.73\times}$ their rated operating current to deliver the mechanical shaft power.
        \item $I^2 R$ copper losses increase by a factor of 3 ($1.73^2 = 3.0$), causing winding insulation to overheat and burn out in under 1 to 2 minutes unless protected by a thermal overload relay equipped with phase-failure differential trip mechanisms.
    \end{itemize}
\end{enumerate}

\section{Master Cross-Domain Comparison Tables}

\subsection{Master Electrical Circuit Protection Comparison}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l l l l l X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Device} & \textbf{Overload} & \textbf{Short Circuit} & \textbf{Earth Leakage} & \textbf{Typical Range} & \textbf{Reset / Reusability} \\
\midrule
\textbf{HRC Fuse} & Yes (Thermal) & Yes (Magnetic/Arc) & No & $2\text{A to }1250\text{A}$ & One-time sacrificial; must replace link. \\
\textbf{MCB} & Yes (Bimetal) & Yes (Solenoid) & No & $0.5\text{A to }125\text{A}$ & Reusable; manual lever toggle. \\
\textbf{MCCB} & Yes (Adjustable) & Yes (Adjustable) & Optional module & $16\text{A to }2500\text{A}$ & Reusable; heavy toggle / motorized handle. \\
\textbf{RCCB / RCD} & \textbf{No} & \textbf{No} & \textbf{Yes (30--300mA)} & $16\text{A to }125\text{A}$ & Reusable; test pushbutton provided. \\
\textbf{RCBO} & \textbf{Yes} & \textbf{Yes} & \textbf{Yes (30--300mA)} & $6\text{A to }63\text{A}$ & Reusable; combines MCB + RCCB in 1 unit. \\
\bottomrule
\end{tabularx}
\caption{Comprehensive Comparison of Electrical Protection Devices}
\end{table}

\subsection{Enterprise Storage and Interface Technology Comparison}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l l l l X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Parameter} & \textbf{SATA III SSD} & \textbf{SAS 12G HDD} & \textbf{PCIe Gen 4 NVMe} & \textbf{PCIe Gen 5 NVMe} \\
\midrule
\textbf{Max Throughput} & $\approx 550\text{ MB/s}$ & $\approx 250\text{--}300\text{ MB/s}$ & $\approx 7,500\text{ MB/s}$ & $\approx 14,500\text{ MB/s}$ \\
\textbf{Protocol} & AHCI & SAS SCSI & NVMe 1.4/2.0 & NVMe 2.0 \\
\textbf{Queues / Depth} & $1\text{ queue} / 32$ & $1\text{ queue} / 254$ & $64,000\text{ queues} / 64\text{k}$ & $64,000\text{ queues} / 64\text{k}$ \\
\textbf{Random IOPS} & $\approx 95,000$ & $\approx 400$ & $\approx 1,000,000+$ & $\approx 2,500,000+$ \\
\textbf{Interface Bus} & SATA $6\text{ Gbps}$ & Serial Attached SCSI & PCIe $4.0 \times4$ & PCIe $5.0 \times4$ \\
\bottomrule
\end{tabularx}
\caption{Storage Technology Architectural Performance Matrix}
\end{table}

\section{Maintenance Engineer's Formula Cheat Sheet and 35 Golden Rules}

\subsection{Essential Engineering Formulas}
\begin{align*}
\text{Ohm's Law:} &\quad V = I \times R, \quad I = \frac{V}{R}, \quad R = \frac{V}{I} \\
\text{DC Power:} &\quad P = V \times I = I^2 R = \frac{V^2}{R} \\
\text{AC RMS \& Peak:} &\quad V_{\text{RMS}} = \frac{V_{\text{peak}}}{\sqrt{2}} \approx 0.7071 V_{\text{peak}}, \quad V_{\text{peak}} = \sqrt{2} V_{\text{RMS}} \approx 1.4142 V_{\text{RMS}} \\
\text{Capacitive Reactance:} &\quad X_C = \frac{1}{2\pi f C} \quad (\Omega) \\
\text{Inductive Reactance:} &\quad X_L = 2\pi f L \quad (\Omega) \\
\text{Transformer Turns Ratio:} &\quad \frac{V_p}{V_s} = \frac{N_p}{N_s} = \frac{I_s}{I_p} \\
\text{Motor Synchronous Speed:} &\quad N_s = \frac{120 f}{P} \quad (\text{RPM}), \quad \text{Slip: } s = \frac{N_s - N_r}{N_s} \times 100\% \\
\text{Single-Phase AC Power:} &\quad P = V \times I \times \cos\phi \quad (\text{W}), \quad S = V \times I \quad (\text{VA}) \\
\text{Three-Phase AC Power:} &\quad P = \sqrt{3} \times V_L \times I_L \times \cos\phi \quad (\text{W}) \\
\text{Total Harmonic Distortion:} &\quad \text{THD}_V = \frac{\sqrt{\sum_{n=2}^{\infty} V_n^2}}{V_1} \times 100\% \\
\text{System Availability:} &\quad A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\% \\
\text{FMEA Risk Priority:} &\quad \text{RPN} = S \times O \times D
\end{align*}

\subsection{35 Golden Maintenance Rules and Traps to Avoid}
\begin{enumerate}[leftmargin=*]
    \item \textbf{De-energize and Verify:} Never measure resistance or continuity on a live circuit. Always verify zero energy with a calibrated multimeter before touching terminals.
    \item \textbf{Ammeter Danger:} Never place multimeter current probes across a voltage source. An ammeter is a direct short circuit and will blow its fuse or cause an arc flash.
    \item \textbf{Single-Conductor Clamping:} Never clamp a current clamp meter around both Line and Neutral conductors simultaneously; the reading will be zero.
    \item \textbf{Capacitor Discharge:} Always discharge high-voltage electrolytic capacitors in power supplies using a $100\,\Omega\text{ to }1\text{ k}\Omega$ $10\text{ W}$ power resistor before servicing; never short with a screwdriver.
    \item \textbf{LOTO Compliance:} Always apply personal physical padlocks and danger tags (Lockout/Tagout) at the main circuit breaker before opening distribution panels.
    \item \textbf{ESD Wrist Strap Resistor:} Never use an ESD wrist strap with a zero-ohm connection; ensure it contains a healthy $1\text{ M}\Omega$ current-limiting safety resistor.
    \item \textbf{Immobilize Fan Blades:} Always hold fan blades stationary with a non-conductive tool when blowing compressed air; freewheeling generates destructive back-EMF into the motherboard.
    \item \textbf{Thermal Paste Application:} Thermal paste fills microscopic surface air imperfections; applying too thick a layer degrades thermal conduction and causes thermal throttling.
    \item \textbf{Never Replace Fuse with Higher Rating:} Replacing a blown $5\text{ A}$ fuse with a $15\text{ A}$ fuse or copper wire defeats circuit protection and causes electrical fires.
    \item \textbf{MCB Curve Selection:} Never use Type B MCBs for inductive motors or transformers; high inrush currents will cause nuisance tripping. Use Type C or D.
    \item \textbf{RCCB Overload Limitation:} Remember that an RCCB does not protect against overloads or short circuits; it must be backed up by an MCB or replaced by an RCBO.
    \item \textbf{Earthing Rod Resistance:} Keep data center earthing system impedance strictly below $1.0\,\Omega$ to ensure rapid circuit breaker clearing and transient dissipation.
    \item \textbf{Avoid Floating STP Shields:} Never leave the foil shield of an STP cable ungrounded; an unbonded shield acts as an RF antenna and degrades transmission.
    \item \textbf{Strict Cable Bend Radius:} Maintain minimum copper cable bend radius of $4\times$ outside diameter, and optical fibre bend radius of at least $10\text{ to }20\times$ outer diameter.
    \item \textbf{Limit Cable Untwist:} Never untwist twisted-pair conductors more than $0.5\text{ inches (12.7 mm)}$ at RJ45 / keystone terminations to prevent NEXT.
    \item \textbf{Permanent Link Limit:} Ensure copper horizontal structured cabling permanent links do not exceed 90~meters, with total channel length strictly $\le 100\text{ meters}$.
    \item \textbf{Do Not Mix Optical Fibres:} Never mate Single-Mode (yellow) with Multi-Mode (orange/aqua) fibre; massive core mismatch ($9\,\mu\text{m}$ vs. $50\,\mu\text{m}$) causes severe insertion loss ($>20\text{ dB}$).
    \item \textbf{Never Look into Fibre Ports:} Never inspect active optical transceivers or fibre patch cables with the naked eye; invisible infrared laser light causes permanent retinal burns.
    \item \textbf{PoE Power Budgeting:} Always derate PoE switches by $20\%$ to account for cable copper $I^2 R$ resistance heating losses over long 90-meter runs.
    \item \textbf{Neutral Conductor Sizing:} In environments dominated by single-phase computer SMPS loads, double the neutral conductor cross-section to handle triplen harmonic summation.
    \item \textbf{Online UPS for Servers:} Never deploy offline standby UPS units for enterprise virtualization servers; instantaneous transfer ($0\text{ ms}$) is mandatory.
    \item \textbf{Battery Float Voltage:} Check UPS VRLA battery string float voltage quarterly; a single shorted cell overcharges remaining batteries, leading to thermal runaway.
    \item \textbf{Positive Pressure Cooling:} Maintain positive static pressure inside server racks and chassis to force air out of cracks, preventing dust ingestion.
    \item \textbf{S.M.A.R.T. Alert Response:} Replace storage drives immediately when Reallocated Sector Count or Pending Sector Count begins incrementing; do not wait for total drive death.
    \item \textbf{RAID 5 Rebuild Vulnerability:} Avoid large RAID 5 arrays with $>4\text{ TB}$ HDDs; the probability of an Unrecoverable Read Error (URE) during rebuild exceeds $50\%$. Use RAID 6 or RAID 10.
    \item \textbf{Firmware Flashing Rule:} Never flash motherboard BIOS or RAID controller firmware during unstable weather or without clean online UPS battery power.
    \item \textbf{RAM Slot Seating:} When installing dual-channel RAM on 4-slot motherboards, always populate matching color channels (typically slots A2 and B2) according to the vendor manual.
    \item \textbf{CPU Socket Pin Caution:} Never touch exposed LGA motherboard pins with fingers or cleaning rags; a single bent pin can destroy dual-channel memory or PCIe lane communication.
    \item \textbf{CAT Rating Safety:} Never use a CAT II rated multimeter inside a main 3-phase commercial distribution panel (MDB); minimum CAT III or CAT IV is mandatory.
    \item \textbf{TDR Diagnostics:} Use Time Domain Reflectometry to pinpoint the exact meter distance to a cable fault instead of blindly pulling replacement cables through walls.
    \item \textbf{Air Gap Verification:} Ensure adequate clearance around server rack exhaust doors ($>3\text{ feet}$) to prevent thermal recirculation back into cold aisles.
    \item \textbf{Flyback Diode Polarity:} Always verify reverse-bias polarity when soldering flyback diodes across DC relay coils; connecting in forward bias causes a dead short across the driver transistor.
    \item \textbf{Cable Management Tension:} Avoid over-tightening plastic zip ties on network cable bundles; crushing cable jackets deforms internal pair geometry and induces return loss. Use hook-and-loop Velcro.
    \item \textbf{Verify Before Escalating:} Always execute the six-step troubleshooting method: question the user, check physical power, link lights, and cable seating before assuming chip failure.
    \item \textbf{Meticulous Documentation:} Always document root causes, replacement part serial numbers, and preventive remedies in the enterprise CMDB to build organizational knowledge.
\end{enumerate}
'''

with open('scratch/ch17_mod10.tex', 'w', encoding='utf-8') as f:
    f.write(content.strip() + '\n')
print('ch17_mod10.tex written successfully!')
