# Computer Networks – Assignment 2

<p align="center">

**CSA07 | CO2 | Network Design, Routing and Protocol Analysis**

</p>

---

## Project Overview

This repository contains the implementation and analysis of Computer Networks Assignment 2. It covers IPv4 addressing, subnetting, routing protocols, IPv6, multicast communication, Software Defined Networking (SDN), and network redesign.

The assignment combines theoretical calculations, Python programming, Cisco Packet Tracer simulations, router configurations, and performance analysis.

**Objective:** To understand and apply computer networking concepts through practical implementation, simulation, and analysis.

---

## Assignment Details

| Detail | Information |
|---|---|
| Course | Computer Networks |
| Course Code | CSA07 |
| Assignment | Assignment 2 |
| Course Outcome | CO2 |
| Total Marks | 50 |
| Register Number | 192521076 |
| Student Name | Swetha S |
| Simulation Tool | Cisco Packet Tracer |
| Programming Language | Python |
| Version Control | Git and GitHub |

---

## Tasks and Navigation

Each task contains its own README, calculations, implementation files, configurations, and evidence wherever applicable.

### Task 1 – IPv4 Addressing, NAT and Packet Switching

**Topics covered:**
- IPv4 address validation
- Network and broadcast address identification
- NAT and PAT
- Datagram switching vs virtual circuit switching
- Public IP address allocation

**Files and resources:**
- [Task 1 – README](Task01/README.md)
- [Address Analysis](Task01/Calculations/address_analysis.md)
- [NAT Translation Table](Task01/NAT/nat_table.csv)
- [Packet Switching Analysis](Task01/NAT/packet_switching.md)
- [Evidence](Task01/Evidence/)

### Task 2 – Subnetting and Route Summarisation

**Topics covered:**
- Equal-size subnetting
- Variable Length Subnet Masking (VLSM)
- Subnet allocation for campus departments
- Address capacity analysis
- Route summarisation

**Files and resources:**
- [Task 2 – README](Task02/README.md)
- [Subnetting Calculations](Task02/Calculations/subnetting.md)
- [Route Summarisation](Task02/Calculations/route_summarisation.md)
- [VLSM Python Program](Task02/Python/vlsm.py)
- [Evidence](Task02/Evidence/)

### Task 3 – Longest Prefix Match and Static Routing

**Topics covered:**
- Longest Prefix Match (LPM)
- Static routing
- Floating static routes
- Administrative distance
- Static routing vs OSPF

**Files and resources:**
- [Task 3 – README](Task03/README.md)
- [Longest Prefix Match Calculations](Task03/Calculations/longest_prefix_match.md)
- [R1 Configuration](Task03/Configurations/R1.txt)
- [R2 Configuration](Task03/Configurations/R2.txt)
- [Packet Tracer Simulation](Task03/PacketTracer/static_routing_floating_route.pkt)
- [Evidence](Task03/Evidence/)

### Task 4 – Distance Vector Routing

**Topics covered:**
- Distance Vector Routing
- Bellman-Ford algorithm
- Distance table calculations
- Count-to-infinity problem
- Split horizon and poison reverse
- RIP Version 2

**Files and resources:**
- [Task 4 – README](Task04/README.md)
- [Distance Vector Calculations](Task04/Calculations/distance_tables.md)
- [Count-to-Infinity Analysis](Task04/Calculations/count_to_infinity.md)
- [Distance Vector Python Program](Task04/Python/distance_vector.py)
- [RIP Configuration](Task04/Configurations/RIP.txt)
- [Evidence](Task04/Evidence/)

### Task 5 – Open Shortest Path First (OSPF)

**Topics covered:**
- OSPF cost calculation
- Reference bandwidth
- Dijkstra's shortest-path algorithm
- OSPF areas
- OSPF configuration
- OSPF vs EIGRP vs IS-IS

**Files and resources:**
- [Task 5 – README](Task05/README.md)
- [Dijkstra Calculations](Task05/Calculations/dijkstra.md)
- [OSPF Configuration](Task05/Configurations/OSPF.txt)
- [Packet Tracer Simulation](Task05/PacketTracer/ospf_six_router.pkt)
- [Evidence](Task05/Evidence/)

### Task 6 – IPv6, ICMP, Multicast and SDN

**Topics covered:**
- IPv6 address compression
- EUI-64 interface identifier generation
- ICMP and traceroute
- IPv4 multicast MAC address calculation
- Software Defined Networking
- OpenFlow flow rules
- IPv6 transition mechanisms
- 6in4 tunnelling overhead

**Files and resources:**
- [Task 6 – README](Task06/README.md)
- [IPv6 Calculations](Task06/IPv6/ipv6_calculations.md)
- [Multicast Analysis](Task06/Multicast/multicast.md)
- [OpenFlow Analysis](Task06/SDN/openflow_analysis.md)
- [Evidence](Task06/Evidence/)

### Task 7 – Design Challenge: Campus Network Redesign

**Topics covered:**
- Identification of network limitations
- Address capacity analysis
- Original network design
- Redesigned network architecture
- VLSM-based address allocation
- Network connectivity validation
- Design trade-off analysis

**Files and resources:**
- [Task 7 – README](Task07/README.md)
- [Redesign Calculations](Task07/Calculations/redesign_analysis.md)
- [Original Network Design](Task07/Original/README.md)
- [Redesigned Network](Task07/Redesigned/README.md)
- [Router Configurations](Task07/Configurations/device_configurations.txt)
- [Evidence](Task07/Evidence/)

---

## Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | VLSM and distance vector simulations |
| Cisco Packet Tracer | Network topology design and routing simulations |
| IPv4 / IPv6 | Addressing and network configuration |
| RIP v2 | Distance vector routing |
| OSPF | Link-state routing |
| OpenFlow | SDN flow-rule analysis |
| Git | Version control |
| GitHub | Repository hosting and project documentation |

---

## System Requirements

| Component | Environment |
|---|---|
| Operating System | Windows 11 |
| Processor | AMD Ryzen 5 5500U |
| RAM | 16 GB |
| Programming Language | Python 3 |
| Network Simulator | Cisco Packet Tracer |
| Version Control | Git |

### Software Versions

Record the actual installed versions before submission.

| Software | Version |
|---|---|
| Python | Add output of `python --version` |
| Cisco Packet Tracer | Add version from Help → About |
| Git | Add output of `git --version` |

---

## How to Run the Python Programs

### Prerequisites

- Python 3 installed.
- Repository cloned or downloaded.
- Terminal opened in the repository's root directory.

### 1. Run the VLSM Program

```bash
python Task02/Python/vlsm.py
```

This program calculates subnet allocations based on host requirements and displays the next available address.

### 2. Run the Distance Vector Program

```bash
python Task04/Python/distance_vector.py
```

This program simulates distance vector routing using the Bellman-Ford algorithm and displays the final routing cost table.

---

## Cisco Packet Tracer Simulations

The Packet Tracer files are organised within their respective task folders.

| Task | Simulation |
|---|---|
| Task 3 | [Static Routing and Floating Route](Task03/PacketTracer/static_routing_floating_route.pkt) |
| Task 4 | [Distance Vector and RIP](Task04/PacketTracer/distance_vector_rip.pkt) |
| Task 5 | [Six-Router OSPF Network](Task05/PacketTracer/ospf_six_router.pkt) |
| Task 7 | [Redesigned Network](Task07/Redesigned/redesigned_network.pkt) |

Open the `.pkt` files using Cisco Packet Tracer to inspect the network topologies and configurations.

---

## Repository Structure

```text
CSA07-192521076-Assignment2/
│
├── README.md
│
├── Task01/
│   ├── README.md
│   ├── NAT/
│   └── address_analysis.md
│
├── Task02/
│   ├── README.md
│   ├── Calculations/
│   └── Evidence/
│
├── Task03/
│   ├── README.md
│   ├── Calculations/
│   ├── Configurations/
|   ├── vlsm.py
│   └── Evidence/
│
├── Task04/
│   ├── README.md
│   ├── Calculations/
│   ├── distance_vector.py
│   ├── Configurations/
│   └── Evidence/
│
├── Task05/
│   ├── README.md
│   ├── Calculations/
│   ├── Configurations/
│   └── Evidence/
│
├── Task06/
│   ├── README.md
│   ├── IPv6/
│   ├── Multicast/
│   └── SDN/
│
└── Task07/
    ├── README.md
    ├── Original/
    ├── Redesigned/
    ├── Calculations/
    ├── Configurations/
    └── Evidence/
```

---

## Version Control

Git is used to track project progress and maintain separate commits for individual tasks.

The repository contains progressive commits documenting the completion of each assignment task.

Example commands:

```bash
git status
git add .
git commit -m "Update assignment documentation and implementations"
git push origin main
```

---

## Conclusion

This project demonstrates the application of computer networking concepts through theoretical analysis, subnet calculations, Python programming, routing configurations, network simulation, and design improvements.

The seven tasks provide practical exposure to addressing, routing, switching, IPv6, multicast, SDN, and network architecture redesign.

---

**Course:** Computer Networks – CSA07

**Assignment:** Assignment 2

**Student:** Swetha S

**Register Number:** 192521076