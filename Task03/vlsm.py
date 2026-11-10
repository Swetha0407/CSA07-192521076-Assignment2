
"""Variable-length subnetting (VLSM) of 192.168.10.0/24 for a college campus."""

import math
import ipaddress


def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def to_ip(n):
    return ".".join(str((n >> s) & 255) for s in (24, 16, 8, 0))


def vlsm(base, needs):
    addr = to_int(base)

    for name, hosts in sorted(needs, key=lambda x: -x[1]):

        # Find the smallest power-of-two block for hosts + network/broadcast.
        block = 1 << math.ceil(math.log2(hosts + 2))

        # Calculate prefix length.
        prefix = 32 - int(math.log2(block))

        # Align the next network address to the block boundary.
        addr = ((addr + block - 1) // block) * block

        network = ipaddress.ip_network(
            f"{to_ip(addr)}/{prefix}", strict=True
        )

        first_host = network.network_address + 1
        last_host = network.broadcast_address - 1

        print(
            f"{name:<13} {network.network_address}/{prefix} "
            f"hosts {first_host} - {last_host} "
            f"bcast {network.broadcast_address}"
        )

        # Move to the address immediately after this subnet.
        addr += block

    return to_ip(addr)


needs = [
    ("Labs", 100),
    ("Staff", 50),
    ("Library", 25),
    ("WAN link", 2)
]

print("next free address:", vlsm("192.168.10.0", needs))
