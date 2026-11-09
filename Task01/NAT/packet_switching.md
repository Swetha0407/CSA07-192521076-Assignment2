# Packet Switching and NAT Analysis

## NAT/PAT Translation

Port Address Translation allows multiple private devices to share a single public IP address.

Two clinic PCs use the same source port 50000. The NAT router assigns different translated source ports to distinguish their connections.

| PC | Private IP and Port | Public IP and Translated Port |
|---|---|---|
| PC1 | 192.168.1.10:50000 | 203.0.113.10:40001 |
| PC2 | 192.168.1.11:50000 | 203.0.113.10:40002 |

The router stores these mappings in its NAT translation table and uses them to direct incoming response packets to the correct internal device.

## Datagram Switching

Datagram switching is a connectionless method in which every packet is routed independently.

Packets from the same file may follow different routes depending on network conditions. As a result, they may arrive out of order.

## Virtual-Circuit Switching

Virtual-circuit switching establishes a logical path before transmission. Packets normally follow the same path, making their delivery order more predictable.

## Comparison

| Parameter | Datagram | Virtual Circuit |
|---|---|---|
| Connection | Connectionless | Connection-oriented |
| Route | Independently selected | Pre-established |
| Ordering | May vary | Usually maintained |
| Setup delay | No setup | Setup required |
| Failure | Alternate routing possible | Circuit may be interrupted |
| State | No per-circuit state | Circuit state maintained |

## Public /27 Alternative

A /27 subnet provides 32 total addresses and 30 usable host addresses.

For 18 clinic devices:

30 - 18 = 12 spare addresses.

A public /27 can therefore accommodate all 18 devices using individual public IP addresses.

### Advantages

- Removes the need for NAT translation.
- Simplifies certain peer-to-peer applications.
- Avoids some port-forwarding complications.
- Allows direct addressing of individual devices.

### Disadvantages

- Requires more public IPv4 addresses.
- May increase ISP costs.
- Devices become directly addressable from the Internet.
- Requires careful firewall and access-control configuration.

## Conclusion

NAT/PAT is generally more economical for a hospital clinic because it allows multiple private devices to share a public IP address. A public /27 avoids certain NAT-related application issues but requires more public addresses and stronger security controls.