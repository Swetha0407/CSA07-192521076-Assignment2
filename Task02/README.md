# Task 2 – Subnet a Campus That Keeps Growing

## Objective
To design equal-size and variable-length subnets for a college campus, implement VLSM using Python, analyse future network expansion and calculate route summarisation.

## 1. Equal-Size Subnetting

The college requires networks for laboratories (100 hosts), staff (50 hosts), library (25 hosts) and a WAN link (2 hosts).

The largest network requires 100 usable host addresses.

2^7 - 2 = 126 usable addresses.

Therefore, the required prefix is /25.

Four /25 subnets require:

4 × 128 = 512 total addresses.

However, the available 192.168.10.0/24 block contains only 256 addresses.

Hence, equal-size subnetting is not possible within the given /24. A /23 block is required to create four equal /25 subnets.

## 2. Variable-Length Subnet Masking (VLSM)

VLSM allocates subnet sizes according to the number of hosts required.

| Department | Hosts Required | Prefix | Subnet Mask |
|---|---:|---|---|
| Laboratories | 100 | /25 | 255.255.255.128 |
| Staff | 50 | /26 | 255.255.255.192 |
| Library | 25 | /27 | 255.255.255.224 |
| WAN link | 2 | /30 | 255.255.255.252 |

### VLSM Allocation

| Department | Network | First Host | Last Host | Broadcast |
|---|---|---|---|---|
| Labs | 192.168.10.0/25 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128/26 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192/27 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN link | 192.168.10.224/30 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |

The next free address is 192.168.10.228.

## 3. Hostel Network Expansion

The hostel requires 60 hosts.

2^6 - 2 = 62 usable addresses.

Therefore, a /26 subnet is required.

The existing allocation ends at 192.168.10.227. The remaining addresses in the /24 are insufficient for a complete /26 block.

The hostel network cannot be added without changing the existing address allocation.

A practical solution is to obtain an additional aligned /26 block, such as 192.168.11.0/26. Alternatively, the overall address allocation can be expanded to a /23, subject to availability.

## 4. Route Summarisation

The four networks are:

- 172.16.8.0/24
- 172.16.9.0/24
- 172.16.10.0/24
- 172.16.11.0/24

These four contiguous networks can be summarised as:

172.16.8.0/22

The /22 summary covers 172.16.8.0 to 172.16.11.255.

If 172.16.12.0/24 is added, the five networks cannot be represented exactly by a single /22 summary. Using 172.16.8.0/21 would cover the range from 172.16.8.0 to 172.16.15.255.

This would also advertise unused networks 172.16.13.0/24, 172.16.14.0/24 and 172.16.15.0/24. Traffic for these networks may be incorrectly attracted to the summarising router.

## 5. Python Implementation

The VLSM allocation program is provided in the Python folder.

It calculates the smallest suitable subnet for each department, displays the network and host ranges, and identifies the next free address.

## Result

Equal-size subnetting was found unsuitable for the given /24 address block. VLSM successfully allocated all four original networks without overlap. The hostel expansion was found to require additional address space. The four city-campus networks were correctly summarised as 172.16.8.0/22.