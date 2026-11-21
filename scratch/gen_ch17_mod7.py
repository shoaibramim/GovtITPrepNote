# -*- coding: utf-8 -*-
"""
Module 7 for Chapter 17: Electronics, Electrical Engineering, and Computer Hardware
Covers Part 6: Network Hardware and Physical Infrastructure (Sections 42 to 48)
"""

content = r'''
\section{Network Hardware Fundamentals}

A computer network requires physical devices and transmission media to interconnect workstations, enterprise servers, multi-function printers, wireless access points, IP surveillance cameras, and perimeter security appliances. For Maintenance Engineers, Network Engineers, and IT Support Specialists, understanding the operational layer, physical interfaces, power requirements, status indicators, and common failure modes of each hardware device is essential for rapid triage and root-cause fault isolation.

\subsection{Network Interface Card (NIC)}
A \textbf{Network Interface Card (NIC)}, also termed a Network Adapter or LAN controller, provides the physical and data-link layer interface enabling a computing device to transmit and receive frames over a communication channel.

\begin{keyconcept}[Core Architectural Functions of a NIC]
\begin{itemize}[leftmargin=*]
    \item \textbf{Unique Physical Identification (MAC Address):} Houses a burned-in 48-bit (6-octet) Media Access Control address assigned by the IEEE, structured as a 24-bit Organizationally Unique Identifier (OUI) followed by a 24-bit Network Interface Controller specific identifier.
    \item \textbf{Physical Layer Transceiver (PHY):} Converts parallel digital data from the internal system bus (e.g., PCIe Gen~3/4) into serial electrical voltages, differential signals, or modulated optical pulses compliant with IEEE 802.3 or 802.11 standards.
    \item \textbf{Data Link Framing and MAC Sublayer:} Performs frame encapsulation/decapsulation, preamble generation, Cyclic Redundancy Check (CRC-32) calculation for Frame Check Sequence (FCS) error verification, and collision detection / avoidance.
    \item \textbf{Link Auto-Negotiation:} Dynamically negotiates the highest mutually supported transmission speed (10/100/1000/10000~Mbps) and duplex mode (Half vs. Full Duplex) with the link partner via Fast Link Pulse (FLP) bursts.
    \item \textbf{Hardware Stateless Offloading:} High-performance enterprise NICs offload computationally intensive tasks from the host CPU, including TCP/IP Checksum Offload, Large Send Offload (LSO) / TCP Segmentation Offload (TSO), Receive Side Scaling (RSS), and SR-IOV (Single Root I/O Virtualization) for virtual machine direct hardware access.
\end{itemize}
\end{keyconcept}

\subsubsection{NIC Classification}
\begin{itemize}[leftmargin=*]
    \item \textbf{Wired Copper NICs:} Interface via 8P8C (RJ45) modular connectors over balanced unshielded/shielded twisted pair copper wiring (10BASE-T, 100BASE-TX, 1000BASE-T, 10GBASE-T).
    \item \textbf{Wired Optical Transceiver NICs:} Utilize modular SFP/SFP+/QSFP cages to interface with single-mode or multi-mode optical fibre cables for high-speed, long-distance, and low-latency backbone connections.
    \item \textbf{Wireless NICs (WLAN):} Integrate baseband RF modems and internal/external antenna arrays operating on 2.4~GHz, 5~GHz, and 6~GHz ISM/UNII bands compliant with IEEE 802.11a/b/g/n/ac/ax (Wi-Fi 6/6E) and 802.11be (Wi-Fi 7).
\end{itemize}

\subsubsection{NIC Failure Symptoms and Diagnostics}
\begin{itemize}[leftmargin=*]
    \item \textbf{Total Absence of Link LEDs:} Physical layer dead. Potential causes: disconnected/broken patch cord, blown PHY chip on the NIC, defective switch port, or absence of transceiver power.
    \item \textbf{Missing Adapter in Operating System:} PCIe slot contact oxidation, loose seating, missing motherboard PCIe lane power, corrupted device driver, or hardware controller failure.
    \item \textbf{Intermittent Flapping Links:} Cable length exceeding 100~meters, severe electromagnetic interference (EMI) from adjacent power conduits, loose RJ45 latch, failing switch port, or marginal solder joints on the NIC PHY chip.
    \item \textbf{Duplex / Speed Mismatch:} One side locked at 100~Mbps Full Duplex while the other is set to Auto-Negotiation, resulting in excessive collisions, late collisions, runt frames, and severe throughput collapse.
    \item \textbf{Elevated CRC / FCS Errors:} Indicated by \texttt{netstat -e} or \texttt{ifconfig / ip -s link}; caused by damaged copper pairs, excessive near-end crosstalk (NEXT), or unshielded cables routed near heavy electrical motors or fluorescent ballasts.
\end{itemize}

\subsection{Network Hub}
A \textbf{Hub} is a legacy Layer~1 (Physical Layer) multiport repeater. When an electrical signal arrives at one port, the hub regenerates and broadcasts the signal out of all other ports, regardless of the intended destination.
\begin{itemize}[leftmargin=*]
    \item \textbf{Single Collision Domain:} All connected devices share the same physical bandwidth and compete for media access using CSMA/CD. Only one node can transmit at any instant; simultaneous transmissions cause collisions.
    \item \textbf{Single Broadcast Domain:} All broadcast, multicast, and unicast traffic traverses every segment.
    \item \textbf{Half-Duplex Only:} Nodes cannot transmit and receive simultaneously.
    \item \textbf{Security Vulnerability:} Network traffic can be intercepted by any host on the hub using a passive packet sniffer in promiscuous mode.
    \item \textbf{Maintenance Verdict:} Completely obsolete. Must be replaced immediately with managed Layer~2 switches in modern enterprise environments.
\end{itemize}

\subsection{Network Switch}
A \textbf{Switch} is a Layer~2 (Data Link Layer) multiport bridge that inspects incoming Ethernet frames, extracts the destination MAC address, and forwards the frame specifically to the egress physical port connected to that destination node.

\begin{keyconcept}[MAC Address Table (CAM) Operation]
A switch maintains a Content Addressable Memory (CAM) table:
\begin{enumerate}[leftmargin=*]
    \item \textbf{Learning:} Upon receiving a frame, the switch records the \textit{source MAC address} and the ingress port ID into its CAM table, resetting an aging timer (typically 300 seconds).
    \item \textbf{Flooding (Unknown Unicast):} If the \textit{destination MAC address} is not present in the CAM table, the switch floods the frame out of all active ports within the VLAN except the ingress port.
    \item \textbf{Forwarding (Known Unicast):} If the destination MAC is found in the CAM table, the frame is directed strictly to the corresponding switch port.
    \item \textbf{Broadcast / Multicast Handling:} Broadcast frames (\texttt{FF:FF:FF:FF:FF:FF}) and multicast frames are flooded to all ports in that broadcast domain (VLAN).
    \item \textbf{Filtering:} If the source and destination nodes reside on the same segment/port, the frame is dropped to prevent redundant traffic.
\end{enumerate}
\end{keyconcept}

\subsubsection{Managed vs. Unmanaged Switches}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l X X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Feature} & \textbf{Unmanaged Switch} & \textbf{Managed Switch} \\
\midrule
\textbf{Configuration} & Plug-and-play; zero administrative interface. & Accessible via CLI (SSH, Console), SNMP, Web GUI, or NETCONF. \\
\textbf{VLAN Support} & None; all ports belong to one single broadcast domain. & Full IEEE 802.1Q tagging, port-based, voice, and private VLANs. \\
\textbf{Loop Prevention} & No STP; network loops cause catastrophic broadcast storms. & IEEE 802.1D STP, 802.1w RSTP, 802.1s MSTP, BPDU Guard, Loop Guard. \\
\textbf{Traffic Prioritization} & Best-effort; no traffic differentiation. & IEEE 802.1p Quality of Service (QoS), DSCP mapping, queue scheduling. \\
\textbf{Port Security} & Open; any device can connect to any port. & 802.1X Network Access Control, sticky MAC limiting, DAI, DHCP Snooping. \\
\textbf{Diagnostics} & Limited to front panel physical LEDs. & Port mirroring (SPAN/RSPAN), sFlow, NetFlow, SNMP traps, cable diagnostics. \\
\textbf{Link Aggregation} & Unsupported. & IEEE 802.3ad / 802.1AX LACP for aggregated bandwidth and fault tolerance. \\
\bottomrule
\end{tabularx}
\caption{Technical Comparison: Unmanaged vs. Managed Switches}
\end{table}

\subsection{Network Router}
A \textbf{Router} is a Layer~3 (Network Layer) internetworking device that examines IP packet headers, looks up routing tables, and forwards packets across distinct logical subnets and autonomous systems.
\begin{itemize}[leftmargin=*]
    \item \textbf{Broadcast Domain Boundary:} Routers do not forward Layer~2 broadcasts by default. Each router interface defines an independent broadcast domain.
    \item \textbf{Routing Table Lookup:} Utilizes longest-prefix matching algorithms to select the optimal egress interface based on static routes or dynamic routing protocols (OSPF, EIGRP, BGP, IS-IS).
    \item \textbf{Network Address Translation (NAT):} Translates RFC~1918 private IPv4 addresses to globally routable public IPv4 addresses, mitigating IPv4 exhaustion.
    \item \textbf{Packet Modification:} At each hop, the router decrements the IP header Time-to-Live (TTL) field by 1, recalculates the IP header checksum, strips the incoming Layer~2 frame header/trailer, and encapsulates the packet in a new Layer~2 frame appropriate for the outbound media.
\end{itemize}

\subsection{Modem vs. Optical Network Terminal (ONT)}
\begin{itemize}[leftmargin=*]
    \item \textbf{Modem (Modulator-Demodulator):} Converts digital bitstreams from a computer or router into analog carrier waves for transmission over legacy telephone copper pairs (DSL / VDSL) or coaxial cables (DOCSIS), and demodulates incoming analog signals back into digital data.
    \item \textbf{ONT (Optical Network Terminal) / ONU (Optical Network Unit):} Deployed at the customer premises in Gigabit Passive Optical Networks (GPON / XGS-PON). Converts optical pulses transmitted over a Single-Mode Optical Fibre (SMF) via downstream Time Division Multiplexing (TDM, 1490~nm) and upstream Time Division Multiple Access (TDMA, 1310~nm) into standard Ethernet frames. An ONT does not perform analog carrier modulation; it performs optoelectronic conversion and optical frame framing.
\end{itemize}

\subsection{Wireless Access Point (AP) vs. Wireless Router}
\begin{itemize}[leftmargin=*]
    \item \textbf{Standalone Access Point (AP):} A dedicated Layer~2 bridging device that converts 802.3 Ethernet frames into 802.11 wireless RF signals. Does not perform routing, NAT, or DHCP services; operates under a centralized Wireless LAN Controller (WLC) or cloud controller in enterprise fabrics.
    \item \textbf{Consumer Wireless Router:} An all-in-one integrated appliance combining a 4-port unmanaged Layer~2 switch, a wireless AP, an IPv4/IPv6 router, a DHCP server, a stateful firewall, and a NAT gateway.
\end{itemize}

\subsection{Hardware Firewall Appliance}
A \textbf{Hardware Firewall} is a dedicated perimeter security appliance deployed inline between network security zones (e.g., WAN, DMZ, Internal LAN).
\begin{itemize}[leftmargin=*]
    \item \textbf{Stateful Packet Inspection (SPI):} Tracks the state of active network connections (TCP 3-way handshakes, sequence numbers, UDP pseudo-states) and automatically permits return traffic associated with recognized outbound sessions.
    \item \textbf{Next-Generation Firewall (NGFW):} Operates up to Layer~7 (Application Layer). Integrates Intrusion Prevention Systems (IPS), deep packet inspection (DPI), SSL/TLS decryption, application identification (App-ID), URL filtering, and antivirus sandbox inspection.
\end{itemize}

\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l l l l X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Device} & \textbf{OSI Layer} & \textbf{PDU Handled} & \textbf{Collision Domains} & \textbf{Broadcast Domains} \\
\midrule
\textbf{Repeater / Hub} & Layer 1 (Physical) & Bits & Single (shared by all ports) & Single \\
\textbf{Bridge / Switch} & Layer 2 (Data Link) & Frames & One per physical port & Single (per VLAN) \\
\textbf{Router} & Layer 3 (Network) & Packets & One per physical port & One per interface (blocks broadcasts) \\
\textbf{Firewall (Routed)} & Layer 3--7 & Packets / Streams & One per physical port & One per routed interface \\
\bottomrule
\end{tabularx}
\caption{Comprehensive Comparison of Core Network Infrastructure Devices}
\end{table}

\section{Ethernet and Network Cabling}

\subsection{Twisted-Pair Copper Cabling}
Twisted-pair cabling consists of color-coded copper conductors twisted together in pairs. Twisting induces electromagnetic cancellation: external electromagnetic interference (EMI) and radio frequency interference (RFI) induce approximately equal noise voltages in both conductors of the pair. Because receiver circuits utilize differential signaling (measuring $V_{\text{diff}} = V^+ - V^-$), common-mode noise is rejected ($CMRR$).

\begin{keyconcept}[UTP vs. STP]
\begin{itemize}[leftmargin=*]
    \item \textbf{UTP (Unshielded Twisted Pair):} No metallic shielding. Flexible, inexpensive, easy to terminate. Dominant in commercial office horizontal runs.
    \item \textbf{STP / FTP (Shielded / Foiled Twisted Pair):} Incorporates metallic foil or braided shielding around individual pairs (U/FTP) or around the outer bundle (F/UTP, S/FTP). Must be bonded to a low-impedance telecommunications ground at both ends; an improperly grounded shield acts as an antenna, worsening noise susceptibility. Essential in industrial plants, elevator shafts, and server rooms running near 400V power conduits.
\end{itemize}
\end{keyconcept}

\subsection{Ethernet Cable Categories and Specifications}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l l l l X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Category} & \textbf{Max Frequency} & \textbf{Max Data Rate} & \textbf{Max Distance} & \textbf{Application \& Construction} \\
\midrule
\textbf{Cat 5e} & 100 MHz & 1 Gbps (1000BASE-T) & 100 meters & 4 pairs, improved crosstalk specs; standard office voice/data. \\
\textbf{Cat 6} & 250 MHz & 1 Gbps / 10 Gbps & 100m (1G), 37--55m (10G) & Longitudinal physical spline separator to minimize NEXT. \\
\textbf{Cat 6A} & 500 MHz & 10 Gbps (10GBASE-T) & 100 meters & Augmented specs; eliminates Alien Crosstalk (ANEXT); data centers. \\
\textbf{Cat 7} & 600 MHz & 10 Gbps & 100 meters & S/FTP (individually shielded pairs + overall braid); GG45/TERA. \\
\textbf{Cat 8} & 2000 MHz & 25 Gbps / 40 Gbps & 30 meters & 2-connector channel; data center Top-of-Rack (ToR) switch links. \\
\bottomrule
\end{tabularx}
\caption{TIA/EIA-568 Twisted-Pair Cable Category Specifications}
\end{table}

\subsection{Modular Connectors and Wiring Standards (T568A vs. T568B)}
Twisted-pair cables terminate in \textbf{8P8C} (8 Position, 8 Contact) modular plugs, commonly called RJ45. The TIA/EIA-568 standard defines two color-code pinouts:

\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{c l l l}
\toprule
\rowcolor{tableheadercolor}
\textbf{Pin} & \textbf{T568A Color Code} & \textbf{T568B Color Code} & \textbf{10/100BASE-TX Function} \\
\midrule
\textbf{1} & White / Green & White / Orange & Transmit Data + ($\text{Tx}+$) \\
\textbf{2} & Green & Orange & Transmit Data -- ($\text{Tx}-$) \\
\textbf{3} & White / Orange & White / Green & Receive Data + ($\text{Rx}+$) \\
\textbf{4} & Blue & Blue & Unused in 10/100 (Used in 1000BASE-T) \\
\textbf{5} & White / Blue & White / Blue & Unused in 10/100 (Used in 1000BASE-T) \\
\textbf{6} & Orange & Green & Receive Data -- ($\text{Rx}-$) \\
\textbf{7} & White / Brown & White / Brown & Unused in 10/100 (Used in 1000BASE-T) \\
\textbf{8} & Brown & Brown & Unused in 10/100 (Used in 1000BASE-T) \\
\bottomrule
\end{tabularx}
\caption{TIA/EIA-568A and T568B Pinout Color Codes}
\end{table}

\begin{notebox}[Straight-Through vs. Crossover Cables]
\begin{itemize}[leftmargin=*]
    \item \textbf{Straight-Through Cable:} Same wiring standard on both ends (either T568A--T568A or T568B--T568B). Connects unlike devices (PC to Switch, Switch to Router).
    \item \textbf{Crossover Cable:} One end terminated as T568A, opposite end as T568B (swapping Pin~1 with Pin~3, and Pin~2 with Pin~6). Historically required to connect like devices (Switch to Switch, PC to PC, PC to Router).
    \item \textbf{Auto-MDIX (Automatic Medium-Dependent Interface Crossover):} Modern PHY transceivers automatically detect transmit/receive wire assignments and reverse them internally if necessary, rendering physical crossover cables unnecessary in Gigabit and 10G networks.
\end{itemize}
\end{notebox}

\section{Optical Fibre Communication}

\subsection{Physical Construction and Wave Propagation}
Optical fibre transmits information as pulses of modulated infrared light through a transparent dielectric waveguide.
\begin{itemize}[leftmargin=*]
    \item \textbf{Core:} Ultra-pure silica glass ($\text{SiO}_2$) with refractive index $n_1$.
    \item \textbf{Cladding:} Surrounding glass layer with lower refractive index $n_2$ ($n_2 < n_1$).
    \item \textbf{Buffer Coating \& Aramid Strength Yarn:} Protective polymer coating (250~$\mu$m to 900~$\mu$m) and Kevlar fibers providing tensile strength.
    \item \textbf{Outer Jacket:} Flame-retardant PVC, LSZH (Low Smoke Zero Halogen), or plenum-rated polyurethane.
\end{itemize}

\begin{keyconcept}[Total Internal Reflection and Acceptance Angle]
Light remains guided within the core via \textbf{Total Internal Reflection (TIR)}. TIR occurs when light travels from a medium of higher refractive index ($n_1$) toward a medium of lower refractive index ($n_2$) at an angle of incidence $\theta_i$ exceeding the critical angle $\theta_c$:
\[
\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)
\]
The \textbf{Numerical Aperture (NA)} represents the light-gathering capability of the fibre:
\[
\text{NA} = \sqrt{n_1^2 - n_2^2} = \sin \theta_{\text{max}}
\]
where $\theta_{\text{max}}$ is the half-angle of the maximum acceptance cone.
\end{keyconcept}

\subsection{Single-Mode Fibre (SMF) vs. Multi-Mode Fibre (MMF)}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l X X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Parameter} & \textbf{Single-Mode Fibre (SMF)} & \textbf{Multi-Mode Fibre (MMF)} \\
\midrule
\textbf{Core Diameter} & $8\text{ to }10~\mu\text{m}$ (typically $9~\mu\text{m}$). & $50~\mu\text{m}\text{ (OM2/OM3/OM4/OM5) or }62.5~\mu\text{m}\text{ (OM1)}$. \\
\textbf{Cladding Diameter} & $125~\mu\text{m}$ (standard OS1/OS2). & $125~\mu\text{m}$. \\
\textbf{Light Source} & Solid-state Lasers (Fabry-Perot, DFB). & VCSELs (850~nm) or legacy LEDs. \\
\textbf{Wavelengths} & 1310~nm, 1550~nm, 1625~nm. & 850~nm, 1300~nm. \\
\textbf{Modal Dispersion} & \textbf{Zero} (only one fundamental mode propagates). & \textbf{High} (multiple rays traverse different path lengths). \\
\textbf{Attenuation} & Extremely low ($0.2\text{ to }0.4\text{ dB/km}$ at 1550~nm). & Moderate ($2.5\text{ to }3.5\text{ dB/km}$ at 850~nm). \\
\textbf{Max Reach} & Up to 10~km, 40~km, or 80+~km without repeaters. & Up to 300~m (OM3 at 10G) to 550~m (OM4 at 10G). \\
\textbf{Cost} & Cable is inexpensive; transceivers are costly. & Cable is slightly higher; transceivers are inexpensive. \\
\textbf{Standard Jacket Color} & \textbf{Yellow} (OS1/OS2). & \textbf{Orange} (OM1/OM2), \textbf{Aqua} (OM3/OM4), \textbf{Lime Green} (OM5). \\
\bottomrule
\end{tabularx}
\caption{Technical Comparison: Single-Mode vs. Multi-Mode Fibre}
\end{table}

\subsection{Optical Connectors and Transceivers}
\begin{itemize}[leftmargin=*]
    \item \textbf{LC (Lucent Connector):} Small Form Factor (SFF) with 1.25~mm ferrule, push-pull latching mechanism. Dominant standard in high-density enterprise patch panels and SFP/SFP+ transceivers.
    \item \textbf{SC (Subscriber Connector):} Push-pull connector with 2.5~mm ferrule. Common in telecom demarcation, GPON ONTs, and legacy patch fields.
    \item \textbf{ST (Straight Tip):} Round bayonet twist-lock connector with 2.5~mm ferrule. Common in legacy industrial MMF networks.
    \item \textbf{MPO / MTP:} Multi-fibre push-on connector housing 12, 24, or 32 fibres in a single rectangular ferrule; used in 40G/100G/400G spine-leaf backbone fabrics.
    \item \textbf{Modular Transceivers:} SFP (1~Gbps), SFP+ (10~Gbps), SFP28 (25~Gbps), QSFP+ (40~Gbps, $4\times 10\text{G}$), QSFP28 (100~Gbps, $4\times 25\text{G}$).
\end{itemize}

\section{Power over Ethernet (PoE)}

\subsection{PoE Operating Principles and Terminology}
\textbf{Power over Ethernet (PoE)} delivers direct-current electrical power alongside Ethernet data over standard Cat5e/Cat6 balanced twisted-pair cabling.
\begin{itemize}[leftmargin=*]
    \item \textbf{Power Sourcing Equipment (PSE):} The device supplying DC electrical power (e.g., PoE-enabled switch, midspan injector).
    \item \textbf{Powered Device (PD):} The terminal device drawing power from the cable (e.g., VoIP telephone, wireless access point, pan-tilt-zoom PTZ IP camera, access control badge reader).
    \item \textbf{Signaling Methods:}
    \begin{itemize}
        \item \textbf{Alternative A (Endspan):} Power is superimposed on the active data pairs (Pins 1-2 and 3-6) using center-tapped phantom transformers.
        \item \textbf{Alternative B (Midspan):} Power is delivered over the spare copper pairs (Pins 4-5 positive, Pins 7-8 negative) in 10/100BASE-TX networks.
        \item \textbf{4-Pair Delivery:} In 802.3bt, power is injected across all 8 conductors simultaneously.
    \end{itemize}
\end{itemize}

\subsection{PoE IEEE Standards and Power Classifications}
\begin{table}[H]
\centering
\small
\rowcolors{2}{tablelight}{white}
\begin{tabularx}{\linewidth}{l l l l l X}
\toprule
\rowcolor{tableheadercolor}
\textbf{Standard} & \textbf{Common Name} & \textbf{Type} & \textbf{PSE Output} & \textbf{PD Input} & \textbf{Pairs Used} \\
\midrule
\textbf{IEEE 802.3af} & PoE (Type 1) & Type 1 & 15.4 W & 12.95 W & 2 pairs (44.0--57.0 VDC) \\
\textbf{IEEE 802.3at} & PoE+ (Type 2) & Type 2 & 30.0 W & 25.5 W & 2 pairs (50.0--57.0 VDC) \\
\textbf{IEEE 802.3bt} & 4PPoE / PoE++ & Type 3 & 60.0 W & 51.0 W & 4 pairs (50.0--57.0 VDC) \\
\textbf{IEEE 802.3bt} & High-Power PoE++ & Type 4 & 90.0 W & 71.3 W & 4 pairs (52.0--57.0 VDC) \\
\bottomrule
\end{tabularx}
\caption{IEEE Power over Ethernet (PoE) Standards Summary}
\end{table}

\begin{examtip}[PoE Power Budget Calculation]
When deploying PoE switches, an engineer must calculate the aggregate power budget:
\[
P_{\text{total\_load}} = \sum_{k=1}^{N} P_{\text{allocated}}(k) \le P_{\text{PSE\_budget}} \times \text{Safety Factor (0.80)}
\]
If an unmanaged or misconfigured PoE switch exceeds its maximum internal power supply capacity, lower-priority ports are abruptly shut down, causing intermittent reboot cycles on security cameras or APs.
\end{examtip}

\section{Patch Panels, Network Racks, and Structured Cabling}

\subsection{Hierarchical Structured Cabling Subsystems (ANSI/TIA-568)}
\begin{enumerate}[leftmargin=*]
    \item \textbf{Entrance Facility (EF):} The telecommunications service entrance where external ISP cables penetrate the building envelope and connect to building surge protection units.
    \item \textbf{Equipment Room (ER):} Centralized room housing core enterprise switches, routers, PBX servers, and Main Cross-Connect (MC) frames.
    \item \textbf{Backbone Cabling (Vertical / Riser):} Interconnects Entrance Facilities, Equipment Rooms, and telecommunications rooms across floors. Typically implemented with high-strand SMF/MMF optical cables or Cat6A copper.
    \item \textbf{Telecommunications Room (TR) / Enclosure (TE):} Intermediate distribution frames (IDF) housing edge access switches and patch panels serving a specific floor.
    \item \textbf{Horizontal Cabling:} Cabling extending from the TR patch panel to individual work area telecommunications outlets. Maximum permanent link distance: \textbf{90 meters}.
    \item \textbf{Work Area:} The space between the wall outlet faceplate and the user terminal. Incorporates equipment patch cords. Total channel length (Permanent Link + Work Area Patch Cord + TR Patch Cord) must \textbf{not exceed 100 meters}.
\end{enumerate}

\subsection{19-Inch Equipment Racks and Rack Units}
Standard IT server and network cabinets adhere to EIA-310-D / IEC 60297 specifications:
\begin{itemize}[leftmargin=*]
    \item \textbf{Rack Width:} 19~inches ($482.6~\text{mm}$) measured between outer mounting hole centers.
    \item \textbf{Rack Unit (U or RU):} The standard unit of vertical height measurement:
    \[
    1\text{U} = 1.75\text{ inches} = 44.45\text{ mm}
    \]
    Each 1U height contains 3 hole pairs spaced vertically at $0.625\text{ in} - 0.625\text{ in} - 0.5\text{ in}$.
    \item \textbf{Standard Cabinet Height:} 42U ($73.5\text{ in} \approx 1.867\text{ m}$ of usable rail space) or 48U.
\end{itemize}

\section{Network Cabling Troubleshooting}

\subsection{Common Copper Physical Layer Faults}
\begin{itemize}[leftmargin=*]
    \item \textbf{Open Circuit:} One or more conductors severed or improperly seated in the 8P8C crimp or 110 punch-down IDC block.
    \item \textbf{Short Circuit:} Copper conductors touching, creating a zero-resistance DC path.
    \item \textbf{Reversed Pair:} Pins reversed at one end (e.g., Pin 1 wired to Pin 2 and Pin 2 to Pin 1).
    \item \textbf{Crossed Pair:} Entire pair terminated onto the wrong pins at the opposite connector.
    \item \textbf{Split Pair:} A severe installation error where conductors from two different twisted pairs are placed onto pins intended for a single pair (e.g., Pin 1 from Pair 2 and Pin 2 from Pair 3). While DC continuity tests pass 1-to-1, electromagnetic cancellation is lost, resulting in massive Near-End Crosstalk (NEXT) and packet collapse.
    \item \textbf{Excessive Untwist at Termination:} Standard TIA-568 allows a maximum untwist of only \textbf{0.5 inches (12.7 mm)} at the RJ45/keystone termination. Exceeding this introduces catastrophic return loss and NEXT.
\end{itemize}

\subsection{Cable Testing Instrumentation}
\begin{itemize}[leftmargin=*]
    \item \textbf{Wiremap Tester:} Inexpensive handheld device verifying basic DC pin-to-pin continuity and checking for opens, shorts, and reversals. Cannot detect high-frequency signal degradation or split pairs.
    \item \textbf{Certification Cable Analyzer (e.g., Fluke DSX):} High-frequency instrument testing parametric standards up to 2~GHz: NEXT, PS-NEXT, FEXT, Return Loss, Insertion Loss (Attenuation), Propagation Delay, and Cable Length via Time Domain Reflectometry (TDR).
    \item \textbf{Optical Power Meter (OPM) and Light Source (OLS):} Measures absolute optical power (in dBm) and total channel insertion loss (in dB) by comparing injected power with received power.
    \item \textbf{Optical Time Domain Reflectometer (OTDR):} Injects high-power laser pulses down an optical fibre and analyzes Rayleigh backscattering and Fresnel reflections to locate splice losses, connector defects, macrobends, and precise distance to cable breaks.
\end{itemize}

\section{Practical Network Hardware Troubleshooting Scenarios}

\begin{tcolorbox}[colback=white,colframe=titleblue,title=\textbf{Scenario 1: Single PC Completely Unable to Connect to Local Network}]
\textbf{Symptoms:} User workstation displays ``Network Cable Unplugged''. NIC link LED is completely dark. \\
\textbf{Diagnostic Steps:}
\begin{enumerate}[leftmargin=*]
    \item Verify physical connection at both the PC NIC port and the wall outlet faceplate. Check for damaged RJ45 plastic retention clip.
    \item Inspect switch port LED on the corresponding IDF switch.
    \item Replace patch cord with a known good, certified Cat6 patch cord.
    \item Connect a portable cable tester to the wall port and TR patch panel to verify permanent link continuity.
    \item Connect an alternate known-working laptop to the wall jack. If the laptop links up, the original PC NIC or driver is defective. If it remains dead, investigate the switch port (admin shut, err-disabled, or blown port ASIC).
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=titleblue,title=\textbf{Scenario 2: Entire Floor Loses Network Connectivity Simultaneously}]
\textbf{Symptoms:} 48 workstations on Floor 3 lose IP connectivity simultaneously. Gateway cannot be pinged. \\
\textbf{Diagnostic Steps:}
\begin{enumerate}[leftmargin=*]
    \item Check physical power to the Floor 3 IDF rack. Verify rack PDU and switch power supply status LEDs (Amber/Red vs. Green).
    \item Inspect the uplink port (copper or fibre SFP+) interconnecting the IDF switch to the core switch.
    \item If the uplink LED is dark, check the SFP+ optical transceiver status and test optical receive power ($P_{\text{rx}}$) using an optical power meter.
    \item If all switch LEDs are rapidly blinking in synchrony at maximum rate, suspect a \textbf{Layer 2 Broadcast Storm} caused by an accidental network loop where STP was disabled or misconfigured. Disconnect redundant links immediately.
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[colback=white,colframe=titleblue,title=\textbf{Scenario 3: Outdoor IP Surveillance Camera Repeatedly Reboots}]
\textbf{Symptoms:} A high-power PTZ outdoor camera operates normally during daylight, but repeatedly reboots in an endless loop at dusk. \\
\textbf{Root Cause Analysis:} At dusk, the camera activates its high-power infrared (IR) LED illumination array and internal heater element, increasing power demand from 12~W to 28~W. If the switch port is only provisioned for 802.3af (15.4~W max) or the switch has depleted its total PoE power budget, the PSE cuts power to prevent circuit overload. \\
\textbf{Resolution:} Reconfigure the switch port for IEEE 802.3at (PoE+, 30~W) or install an external 802.3at/bt midspan PoE injector.
\end{tcolorbox}
'''

with open('scratch/ch17_mod7.tex', 'w', encoding='utf-8') as f:
    f.write(content.strip() + '\n')
print('ch17_mod7.tex written successfully!')
