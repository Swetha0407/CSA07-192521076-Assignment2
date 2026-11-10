# Route Summarisation

## 1. Given Networks

The following four contiguous Class C networks are given:

- 172.16.8.0/24
- 172.16.9.0/24
- 172.16.10.0/24
- 172.16.11.0/24

## 2. Finding the Summary Route

The four networks are contiguous and share the first 22 bits.

| Network | Third Octet (Binary) |
|---|---|
| 172.16.8.0/24 | 00001000 |
| 172.16.9.0/24 | 00001001 |
| 172.16.10.0/24 | 00001010 |
| 172.16.11.0/24 | 00001011 |

The common prefix is 22 bits.

**Summary network:** `172.16.8.0/22`

**Subnet mask:** `255.255.252.0`

**Address range:** `172.16.8.0 – 172.16.11.255`

This single summary route represents all four /24 networks.

## 3. Adding Another Network

Suppose the network `172.16.12.0/24` is added.

The existing `/22` summary cannot include this network because it covers only 172.16.8.0 through 172.16.11.255.

A broader summary of `172.16.8.0/21` would cover:

- 172.16.8.0 – 172.16.15.255

However, this also includes the networks:

- 172.16.13.0/24
- 172.16.14.0/24
- 172.16.15.0/24

These additional networks may not belong to the organisation.

## 4. Potential Routing Problem

Advertising the broader `/21` route may cause routers to send traffic for the additional address ranges towards this organisation, even when those networks are not actually reachable through it.

This can result in incorrect traffic forwarding or black-hole routing.

Therefore, route summarisation must be performed carefully, ensuring that the advertised summary covers only address ranges that are owned and reachable.

## 5. Conclusion

The four given networks can be summarised into `172.16.8.0/22`, reducing routing table entries from four to one. Adding `172.16.12.0/24` requires a broader summary, which may unintentionally advertise unused networks. Hence, route summarisation improves routing efficiency but must be planned carefully.