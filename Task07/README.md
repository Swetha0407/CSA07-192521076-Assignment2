# Task 7 – Design Challenge: Improving Campus IP Address Allocation

## 1. Problem Identification

The original campus network uses the address block `192.168.10.0/24` for four departments:

- Labs – 100 hosts
- Staff – 50 hosts
- Library – 25 hosts
- WAN link – 2 hosts

During Task 2, Variable Length Subnet Masking (VLSM) was used to allocate these networks.

An additional Hostel network requiring 60 hosts was introduced. However, the remaining address space in the original /24 allocation is insufficient to accommodate another /26 subnet.

This creates an IP address capacity limitation.

## 2. Measurable Objective

The redesign aims to:

1. Support all five networks, including the additional Hostel network.
2. Accommodate at least 60 Hostel hosts.
3. Preserve the existing four subnet allocations without renumbering.
4. Avoid overlapping subnet ranges.
5. Verify network connectivity in Cisco Packet Tracer.

The main measurable target is to support all 237 required host addresses across the five networks while maintaining valid subnet boundaries.

## 3. Original Design

The original allocation is `192.168.10.0/24`.

| Department | Network | Prefix | Usable Hosts |
|---|---|---:|---:|
| Labs | 192.168.10.0 | /25 | 126 |
| Staff | 192.168.10.128 | /26 | 62 |
| Library | 192.168.10.192 | /27 | 30 |
| WAN | 192.168.10.224 | /30 | 2 |

The four subnets consume 228 addresses out of the 256 addresses in the /24 block.

The remaining 28 addresses are insufficient for the Hostel network, which requires a /26 subnet containing 64 total addresses and 62 usable host addresses.

## 4. Redesigned Address Allocation

The address block is expanded to `192.168.10.0/23`.

The original four subnet allocations are preserved, and the Hostel network is added using `192.168.11.0/26`.

| Department | Network | Prefix | Usable Hosts |
|---|---|---:|---:|
| Labs | 192.168.10.0 | /25 | 126 |
| Staff | 192.168.10.128 | /26 | 62 |
| Library | 192.168.10.192 | /27 | 30 |
| WAN | 192.168.10.224 | /30 | 2 |
| Hostel | 192.168.11.0 | /26 | 62 |

The new /23 block provides 512 total addresses and accommodates all five networks without overlapping the existing allocations.

## 5. Topology Redesign

The redesigned topology contains:

- One router connecting the campus networks.
- Separate LAN segments for the departments.
- Dedicated address ranges for each department.
- A separate Hostel LAN using the newly allocated /26 subnet.

The Packet Tracer implementation uses representative Labs and Hostel LANs to validate communication between the preserved and newly added subnets.

## 6. Predicted Results

| Parameter | Original Design | Redesigned Design |
|---|---|---|
| Address block | /24 | /23 |
| Total addresses | 256 | 512 |
| Existing networks | 4 | 4 |
| Hostel network | Cannot fit | Supported |
| Hostel usable capacity | Insufficient | 62 hosts |
| Existing subnet changes | Not required | Not required |
| Subnet overlap | None in existing plan | None in redesigned plan |

The redesigned allocation is expected to support the additional Hostel network while maintaining the original department addresses.

## 7. Implementation and Validation

The original and redesigned address plans are documented separately.

- [Original Design](Original/)
- [Redesigned Design](Redesigned/)
- [Router Configurations](Configurations/device_configurations.txt)
- [Redesign Calculations](Calculations/redesign_analysis.md)

Cisco Packet Tracer is used to verify connectivity between representative LANs in the redesigned network.

The following tests are performed:

1. Verify the IP addresses and subnet masks.
2. Check the router interfaces.
3. Ping between the Labs and Hostel networks.
4. Verify the routing table.
5. Confirm that the new subnet does not overlap existing networks.

Simulation screenshots and validation evidence are stored in:

- [Task 7 Evidence](Evidence/)

## 8. Trade-off Analysis

**Advantages:**

- Supports the additional Hostel network.
- Preserves the original department addresses.
- Provides room for future network expansion.
- Avoids subnet overlap.
- Reduces the need for renumbering existing devices.

**Limitations:**

- Requires an approved larger address allocation.
- A larger address block does not automatically improve network performance.
- Additional subnetworks require appropriate routing and network configuration.
- The expanded address block increases the amount of reserved address space.

## Conclusion

The original /24 address block cannot accommodate the additional 60-host Hostel network while preserving the existing subnet allocations. Expanding the allocation to /23 solves this limitation. The redesigned plan supports all five networks, preserves existing addresses and provides sufficient host capacity for the Hostel. Packet Tracer validation is used to demonstrate connectivity between representative networks.