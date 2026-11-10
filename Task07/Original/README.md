# Original Network Design

## Address Allocation

The original campus network uses `192.168.10.0/24`.

| Department | Network | Prefix |
|---|---|---:|
| Labs | 192.168.10.0 | /25 |
| Staff | 192.168.10.128 | /26 |
| Library | 192.168.10.192 | /27 |
| WAN | 192.168.10.224 | /30 |

## Identified Limitation

The original four allocations consume 228 addresses out of 256.

Only 28 addresses remain, whereas the additional Hostel network requires a /26 subnet containing 64 addresses.

Therefore, the original allocation cannot support the Hostel network without modifying the existing subnet plan.

## Baseline Validation

The original address plan is the baseline for comparison. Its existing subnet allocations are retained in the redesigned plan.

The original Packet Tracer topology, if created, should be saved in this folder as `original_topology.pkt`.