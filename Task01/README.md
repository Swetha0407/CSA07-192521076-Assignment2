# Task 1 – Spot the Invalid Addresses

## Objective
To analyse IPv4 addresses, identify invalid host addresses, understand NAT/PAT translation, and compare datagram switching with virtual-circuit switching.

## 1. IPv4 Address Analysis

Four devices were examined using their assigned IP addresses and subnet prefixes.

| Device | IP Address/Prefix | Subnet Mask | Network Address | Broadcast Address | Usable Host Range | Status |
|---|---|---|---|---|---|---|
| Admission PC | 172.16.45.200/20 | 255.255.240.0 | 172.16.32.0 | 172.16.47.255 | 172.16.32.1–172.16.47.254 | Valid |
| Lab printer | 10.0.15.255/21 | 255.255.248.0 | 10.0.8.0 | 10.0.15.255 | 10.0.8.1–10.0.15.254 | Invalid |
| X-ray server | 192.168.4.0/23 | 255.255.254.0 | 192.168.4.0 | 192.168.5.255 | 192.168.4.1–192.168.5.254 | Invalid |
| Clinic router | 203.0.113.10/29 | 255.255.255.248 | 203.0.113.8 | 203.0.113.15 | 203.0.113.9–203.0.113.14 | Valid |

### Invalid Address Identification

- The lab printer address 10.0.15.255 is the broadcast address of its /21 subnet. Therefore, it cannot be assigned to an individual host.
- The X-ray server address 192.168.4.0 is the network address of its /23 subnet. It identifies the network rather than an individual host.

The Admission PC and clinic router addresses are valid host addresses within their respective subnets.

**Note:** The 203.0.113.0/24 block is reserved for documentation purposes. The clinic router address is valid for the subnet calculation in this assignment but is not a globally routable public Internet address.

## 2. NAT and Port Address Translation

Network Address Translation (NAT) allows devices using private IP addresses to communicate with external networks through a public IP address.

Port Address Translation (PAT) allows multiple devices to share the same public IP address by assigning different translated source port numbers.

Example:

| Inside Local Address | Inside Global Address | Destination |
|---|---|---|
| 192.168.1.10:50000 | 203.0.113.10:40001 | 8.8.8.8:443 |
| 192.168.1.11:50000 | 203.0.113.10:40002 | 8.8.8.8:443 |

Both PCs use source port 50000, but the router translates them into different public source ports, 40001 and 40002.

The router stores these translations in its NAT table. When response packets arrive, the router uses the translated port numbers to forward them to the correct internal devices.

## 3. Datagram Switching

Datagram switching is a connectionless packet-switching method in which each packet is routed independently according to its destination address.

Packets belonging to the same file may travel through different routes due to congestion or routing decisions. Therefore, they may arrive at the destination in a different order.

The receiving protocol can rearrange packets into the correct order when required.

## 4. Virtual-Circuit Switching

Virtual-circuit switching establishes a logical path between the sender and receiver before transmitting data.

Packets normally follow the established path, providing more predictable packet ordering. However, the network must maintain connection information, and a path failure may interrupt the virtual circuit.

## 5. Comparison

| Feature | Datagram Switching | Virtual-Circuit Switching |
|---|---|---|
| Connection | Connectionless | Connection-oriented |
| Route | Independent route for each packet | Established logical path |
| Packet order | May arrive out of order | Usually maintained |
| Setup | Not required | Required |
| Failure handling | Can use alternate routes | May require circuit re-establishment |
| Router state | No per-circuit connection state | Maintains circuit information |

Datagram switching offers flexibility and fault tolerance, whereas virtual-circuit switching provides a more predictable communication path.

## 6. Alternative Concept – Public /27 Instead of NAT Behind /29

A /27 subnet contains 32 total addresses, of which 30 are usable host addresses.

The clinic requires addresses for 18 devices.

Available spare addresses:

30 - 18 = 12

Therefore, a public /27 subnet can accommodate all 18 devices.

| Factor | NAT Behind /29 | Public /27 |
|---|---|---|
| Total addresses | 8 | 32 |
| Usable addresses | 6 | 30 |
| Addressing | Private addresses | Individual public addresses |
| Public IP usage | Shared public IP | 18 public IPs |
| Cost | Generally lower | Generally higher |
| Internet exposure | Devices behind NAT | Devices directly addressable |
| Inbound connections | May require port forwarding | No NAT port forwarding required |

### Problems Avoided by Removing NAT

- Difficulties with applications that embed IP addresses or port numbers.
- Complications with peer-to-peer connections.
- Port-forwarding requirements for inbound services.
- Certain VoIP and video-conferencing connection issues.

### Evaluation

A public /27 provides enough addresses for the clinic's 18 devices and removes several NAT-related application complications. However, it consumes more public IPv4 addresses, may increase cost, and exposes devices to direct Internet addressing.

For a hospital environment, private addressing with NAT and appropriate firewall protection is generally more economical and secure.

## Result

The four IPv4 addresses were analysed successfully, and two invalid host addresses were identified. A NAT/PAT translation example was demonstrated, and datagram switching was compared with virtual-circuit switching. The public /27 alternative was evaluated based on address capacity, cost, application compatibility and security.