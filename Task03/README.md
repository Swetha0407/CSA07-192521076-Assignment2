# Task 3 – Which Way Will the Packet Go?

## Objective

To understand longest-prefix-match routing, configure static routes between two networks, and implement floating static routes for backup connectivity.

## 1. Longest Prefix Match

Routers select the most specific matching route in their routing table. This is known as Longest Prefix Match (LPM).

| Destination IP | Selected Prefix | Next Hop |
|---|---|---|
| 10.1.2.200 | /25 | 192.0.2.13 |
| 10.1.2.100 | /24 | 192.0.2.9 |
| 10.1.9.9 | /16 | 192.0.2.5 |
| 10.7.7.7 | /8 | 192.0.2.1 |
| 8.8.8.8 | /0 | 198.51.100.1 |

**Detailed calculations:** [Longest Prefix Match Calculations](Calculations/longest_prefix_match.md)

## 2. Static Routing Implementation

A two-router network is configured in Cisco Packet Tracer.

| Device | Interface | IP Address |
|---|---|---|
| R1 | G0/0 | 192.168.10.1/24 |
| R1 | S0/0/0 | 10.0.0.1/30 |
| R1 | S0/0/1 | 10.0.0.5/30 |
| R2 | G0/0 | 192.168.20.1/24 |
| R2 | S0/0/0 | 10.0.0.2/30 |
| R2 | S0/0/1 | 10.0.0.6/30 |

### Router Configurations

- [R1 Configuration](Configurations/R1.txt)
- [R2 Configuration](Configurations/R2.txt)

### Packet Tracer Simulation

- [Static Routing and Floating Route Simulation](PacketTracer/static_routing_floating_route.pkt)

## 3. Floating Static Route

A floating static route acts as a backup route. It is configured with a higher administrative distance than the primary route.

- Primary route: Administrative Distance 1
- Backup route: Administrative Distance 200

When the primary route becomes unavailable, the backup route can be selected if its next hop remains reachable.

## 4. Verification

The following commands are used to verify connectivity and routing:

```bash
show ip interface brief
show ip route
show running-config
ping
traceroute
```

The primary link is tested first. It is then disabled to verify whether traffic can travel through the backup link.

### Evidence and Screenshots

All simulation screenshots and verification outputs are stored in the following folder:

- [Task 3 Evidence](Evidence/simulation.png)

| Evidence File | Description |
|---|---|
| topology.png | Complete Packet Tracer topology |
| r1_configuration.png | R1 configuration |
| r2_configuration.png | R2 configuration |
| primary_route.png | Primary route verification |
| primary_ping.png | Successful primary-link ping |
| backup_route.png | Backup route verification |
| backup_ping.png | Successful backup-link ping |

## 5. Static Routing vs OSPF

| Parameter | Static Routing | OSPF |
|---|---|---|
| Configuration | Manual | Dynamic |
| Scalability | Small networks | Larger networks |
| Route updates | Manual | Automatic |
| Failure recovery | Backup routes required | Recalculates routes after convergence |
| Resource usage | Low | Higher |
| Complexity | Simple for small networks | More complex |

Static routing is suitable for small and predictable networks, while OSPF is more suitable for larger networks because it automatically learns and updates routes.

## Conclusion

Longest-prefix matching ensures that the most specific route is selected. Static routes provide connectivity between different networks, while floating static routes provide backup connectivity when the primary route fails. OSPF offers dynamic routing and better scalability for larger networks.