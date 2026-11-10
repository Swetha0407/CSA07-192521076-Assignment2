# Redesign Analysis – Campus IP Address Allocation

## 1. Original Address Requirements

| Network | Required Hosts |
|---|---:|
| Labs | 100 |
| Staff | 50 |
| Library | 25 |
| WAN | 2 |
| Hostel | 60 |
| **Total** | **237** |

Each subnet must have sufficient usable host addresses. Network and broadcast addresses cannot be assigned to ordinary devices in these IPv4 subnets.

## 2. Original VLSM Allocation

The original address block is:

`192.168.10.0/24`

| Network | Prefix | Total Addresses | Usable Hosts |
|---|---:|---:|---:|
| Labs | /25 | 128 | 126 |
| Staff | /26 | 64 | 62 |
| Library | /27 | 32 | 30 |
| WAN | /30 | 4 | 2 |
| **Total** | | **228** | **220** |

Remaining address count:

256 - 228 = **28 addresses**

The Hostel requires 60 usable host addresses. A /26 subnet is required because:

2⁶ = 64 total addresses

64 - 2 = **62 usable host addresses**

Since only 28 addresses remain, the Hostel network cannot be allocated within the original /24 block without changing the existing subnet plan.

## 3. Redesigned Address Block

The proposed address block is:

`192.168.10.0/23`

Subnet mask:

`255.255.254.0`

Total addresses:

2^(32 - 23) = **512 addresses**

Address range:

`192.168.10.0 – 192.168.11.255`

## 4. Redesigned VLSM Allocation

| Network | Network Address | Prefix | First Host | Last Host | Broadcast |
|---|---|---:|---|---|---|
| Labs | 192.168.10.0 | /25 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| Staff | 192.168.10.128 | /26 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| Library | 192.168.10.192 | /27 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| WAN | 192.168.10.224 | /30 | 192.168.10.225 | 192.168.10.226 | 192.168.10.227 |
| Hostel | 192.168.11.0 | /26 | 192.168.11.1 | 192.168.11.62 | 192.168.11.63 |

All five subnets are within the new /23 address block and do not overlap.

## 5. Address Utilisation

Total address capacity:

512 addresses

Total addresses allocated:

128 + 64 + 32 + 4 + 64 = **292 addresses**

Remaining unallocated addresses:

512 - 292 = **220 addresses**

The redesigned allocation supports all five networks and leaves room for future expansion.

## 6. Comparison

| Parameter | Original /24 | Redesigned /23 |
|---|---:|---:|
| Total address capacity | 256 | 512 |
| Allocated addresses | 228 | 292 |
| Unallocated addresses | 28 | 220 |
| Hostel support | No | Yes |
| Existing subnet preservation | Yes | Yes |

## 7. Validation Criteria

The redesign is considered successful when:

1. All five subnets have sufficient usable host addresses.
2. No two allocated subnet ranges overlap.
3. Existing subnet addresses remain unchanged.
4. The Hostel network has at least 60 usable addresses.
5. Representative Labs and Hostel devices can communicate through the router in Packet Tracer.

## Conclusion

Expanding the address allocation from /24 to /23 provides 512 total addresses. The original four subnets remain unchanged, and a new /26 subnet is allocated for the Hostel. The redesigned allocation satisfies the address requirements and leaves 220 addresses available for future use.