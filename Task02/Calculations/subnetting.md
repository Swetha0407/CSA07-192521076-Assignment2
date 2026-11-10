# Subnetting Calculations

## A. Equal-Size Subnetting

Largest host requirement = 100.

Required host bits:

2^7 - 2 = 126 usable addresses.

Prefix length:

32 - 7 = /25.

Total addresses per subnet:

2^7 = 128.

For four equal-size subnets:

4 × 128 = 512 addresses.

The available /24 provides:

2^8 = 256 addresses.

Therefore, the available block is insufficient.

A /23 provides 512 addresses and can accommodate four /25 subnets.

## B. VLSM Calculations

### Laboratories

Required hosts = 100.

2^7 - 2 = 126.

Prefix = /25.

Block size = 128.

Network = 192.168.10.0/25.

### Staff

Required hosts = 50.

2^6 - 2 = 62.

Prefix = /26.

Block size = 64.

Network = 192.168.10.128/26.

### Library

Required hosts = 25.

2^5 - 2 = 30.

Prefix = /27.

Block size = 32.

Network = 192.168.10.192/27.

### WAN Link

Required hosts = 2.

2^2 - 2 = 2.

Prefix = /30.

Block size = 4.

Network = 192.168.10.224/30.

## C. Next Free Address

The WAN subnet occupies addresses 192.168.10.224 to 192.168.10.227.

The next available address is:

192.168.10.228.

## D. Hostel Expansion

Required hosts = 60.

2^6 - 2 = 62.

Required prefix = /26.

A /26 requires 64 aligned addresses. The remaining space in the original /24 cannot accommodate this subnet.

An additional aligned /26 block is required, such as 192.168.11.0/26 if the larger address allocation is available.

## Conclusion

VLSM allocates address space efficiently by assigning the largest subnet first and smaller subnets afterward. All four original networks fit within the given /24 without overlapping.