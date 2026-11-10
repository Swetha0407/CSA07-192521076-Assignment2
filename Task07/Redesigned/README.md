# Redesigned Network

## New Address Allocation

The redesigned network uses the expanded block `192.168.10.0/23`.

| Department | Network | Prefix |
|---|---|---:|
| Labs | 192.168.10.0 | /25 |
| Staff | 192.168.10.128 | /26 |
| Library | 192.168.10.192 | /27 |
| WAN | 192.168.10.224 | /30 |
| Hostel | 192.168.11.0 | /26 |

## Improvements

- All four original subnet allocations are preserved.
- The Hostel receives a separate /26 subnet.
- All five subnet ranges are non-overlapping.
- The Hostel receives 62 usable host addresses.
- The expanded address block leaves 220 addresses unallocated.

## Packet Tracer Validation

The representative Labs and Hostel LANs are connected through router R1.

The simulation should demonstrate:

1. Correct IP addressing on both LANs.
2. Correct subnet masks and default gateways.
3. Successful communication between the Labs and Hostel PCs.
4. Both networks appearing as directly connected routes on R1.

Save the redesigned Packet Tracer simulation as `redesigned_network.pkt` in this folder.