# Task 6 – IPv6, ICMP, Multicast and SDN

## Objective

To understand IPv6 address representation, EUI-64, ICMP traceroute, IPv4 multicast addressing, OpenFlow rules and IPv6 transition mechanisms.

## 1. IPv6 Addressing

IPv6 addresses use 128 bits and are represented in hexadecimal notation. Consecutive zero groups can be compressed using the `::` notation.

The given IPv6 address is:

`2001:0db8:0000:0000:0000:ff00:0042:8329`

Compressed representation:

`2001:db8::ff00:42:8329`

### EUI-64 Address Generation

EUI-64 generates a 64-bit interface identifier from a 48-bit MAC address by inserting `FF:FE` in the middle and inverting the universal/local bit.

Given MAC address: `00:1A:2B:3C:4D:5E`

Generated interface identifier:

`021A:2BFF:FE3C:4D5E`

- [IPv6 Calculations](IPv6/ipv6_calculations.md)

## 2. ICMP and Traceroute

Traceroute identifies the intermediate routers between a source and destination.

It uses increasing TTL values. When a router decrements the TTL to zero, it returns an ICMP Time Exceeded message.

## 3. IPv4 Multicast

IPv4 multicast allows one sender to transmit data to a group of receivers without sending separate copies to every receiver.

For multicast group `239.1.2.3`, the corresponding Ethernet multicast MAC address is:

`01:00:5E:01:02:03`

- [Multicast Calculations and Analysis](Multicast/multicast.md)

## 4. Software Defined Networking (SDN)

SDN separates the control plane from the data plane. The controller manages forwarding decisions using programmable flow rules.

The OpenFlow example uses destination IP addresses and transport-layer ports to decide how HTTP and SSH traffic should be handled.

- [OpenFlow Analysis](SDN/openflow_analysis.md)

## 5. IPv6 Transition Mechanisms

| Method | Description | Advantage | Limitation |
|---|---|---|---|
| Dual stack | IPv4 and IPv6 operate together | Native connectivity to both protocols | Requires managing both protocols |
| Tunnelling | IPv6 packets are carried through IPv4 networks | Connects IPv6 networks across IPv4 infrastructure | Adds encapsulation overhead |
| Native IPv6 | Network operates using IPv6 | Avoids IPv4 tunnelling overhead | Requires IPv6 support throughout the path |

A dual-stack approach is suitable for gradual migration, while tunnelling can help connect IPv6 networks across infrastructure that does not yet support native IPv6.

## 6. Evidence and Verification

The following commands can be used for IPv6 and connectivity verification:

```bash
ipconfig
ping
tracert
```
## Conclusion

IPv6 provides a larger address space and simplified address representation. ICMP helps identify network paths and errors, multicast improves one-to-many communication, and SDN provides programmable network control. Dual-stack and tunnelling are useful mechanisms for transitioning from IPv4 to IPv6.