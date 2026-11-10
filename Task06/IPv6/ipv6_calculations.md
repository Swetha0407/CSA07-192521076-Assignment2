# IPv6 Addressing and ICMP Calculations

## 1. IPv6 Address Compression

Given address:

`2001:0db8:0000:0000:0000:ff00:0042:8329`

### Rules

1. Remove leading zeros from each hexadecimal group.
2. Replace one consecutive sequence of zero groups with `::`.
3. The `::` notation can be used only once in an IPv6 address.

### Result

**Compressed address:**

`2001:db8::ff00:42:8329`

## 2. EUI-64 Interface Identifier

Given MAC address:

`00:1A:2B:3C:4D:5E`

### Steps

1. Divide the MAC address into two halves:

   `00:1A:2B` and `3C:4D:5E`

2. Insert `FF:FE` between the two halves:

   `00:1A:2B:FF:FE:3C:4D:5E`

3. Invert the universal/local bit in the first octet.

   `00 XOR 02 = 02`

4. The resulting interface identifier is:

   `021A:2BFF:FE3C:4D5E`

## 3. Traceroute Using TTL and ICMP

Traceroute identifies the routers between a source and destination by sending packets with increasing TTL values.

| Probe | Initial TTL | Result |
|---|---:|---|
| 1 | 1 | First router returns ICMP Time Exceeded |
| 2 | 2 | Second router returns ICMP Time Exceeded |
| 3 | 3 | Third router returns ICMP Time Exceeded |
| 4 | 4 | Probe may reach the destination |

Each router decreases the TTL by one. When it reaches zero, the router discards the packet and normally sends an ICMP Time Exceeded message.

When the probe reaches the destination, the final response depends on the traceroute method. For example, UDP-based traceroute may receive ICMP Destination Unreachable (Port Unreachable), while other methods may receive an ICMP Echo Reply.

## 4. Conclusion

IPv6 compression reduces the length of address representations without changing the actual address. EUI-64 generates an interface identifier from a MAC address, while traceroute uses TTL and ICMP messages to identify network paths.

## 5. IPv6-over-IPv4 Tunnelling Overhead (6in4)

In 6in4 tunnelling, an IPv6 packet is encapsulated inside an IPv4 packet so that it can travel through an IPv4 network.

Given:

- Original sensor packet size: 100 bytes
- Additional IPv4 header: 20 bytes

### Calculation

Total packet size:

100 + 20 = **120 bytes**

Overhead relative to the original payload:

(20 / 100) × 100 = **20%**

Overhead as a percentage of the final packet:

(20 / 120) × 100 = **16.67%**

Therefore, the 6in4 tunnel adds 20 bytes of IPv4 header overhead to the original 100-byte packet.

*Assumption: The IPv4 header has no optional fields. Link-layer overhead is excluded.*

## 6. IPv6 Transition Comparison

| Method | Advantages | Limitations |
|---|---|---|
| Dual stack | Supports IPv4 and IPv6 simultaneously | Requires managing both protocols |
| 6in4 tunnelling | Carries IPv6 traffic through IPv4 infrastructure | Adds an IPv4 header and requires tunnel configuration |
| Native IPv6 | Direct IPv6 communication without IPv4 encapsulation | Requires IPv6 support across the network path |

Dual stack is a practical approach for gradual migration because both protocols can operate together. Tunnelling is useful when IPv6 traffic must cross an IPv4-only network, while native IPv6 is preferable for long-term IPv6 connectivity.