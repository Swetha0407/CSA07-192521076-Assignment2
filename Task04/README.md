# Task 4 – Distance Vector Routing

## Objective

To understand distance vector routing using the Bellman-Ford algorithm, calculate shortest paths between routers, study the count-to-infinity problem, and configure RIP in Cisco Packet Tracer.

## 1. Network Topology

The given network contains five routers: A, B, C, D and E.

| Link | Cost |
|---|---:|
| A – B | 2 |
| A – C | 7 |
| B – C | 3 |
| B – D | 8 |
| C – D | 1 |
| D – E | 4 |

Each router maintains a distance vector containing its estimated cost to reach every destination. Routers exchange their vectors with neighbouring routers and update their routes using the Bellman-Ford algorithm.

## 2. Bellman-Ford Implementation

A Python program is used to simulate distance vector routing and calculate the shortest paths.

- [Distance Vector Python Program](Python/distance_vector.py)
- [Distance Vector Calculations](Calculations/distance_tables.md)

## 3. Count-to-Infinity Problem

Count-to-infinity occurs when routers slowly increase their distance estimates after a route failure because they incorrectly believe that another router still has a valid path.

Split horizon and poison reverse help prevent routing loops.

- [Count-to-Infinity Analysis](Calculations/count_to_infinity.md)

## 4. RIP Configuration

RIP Version 2 is configured on the routers in Cisco Packet Tracer.

- [RIP Router Configurations](Configurations/RIP.txt)
- [Packet Tracer Simulation](PacketTracer/distance_vector_rip.pkt)

## 5. Distance Vector vs Link State Routing

| Parameter | Distance Vector | Link State |
|---|---|---|
| Network knowledge | Neighbour information | Complete topology database |
| Algorithm | Bellman-Ford | Dijkstra |
| Updates | Distance vectors shared with neighbours | Link-state advertisements are flooded |
| Convergence | Can be slower | Generally faster |
| Resource usage | Lower | Higher |
| Example | RIP | OSPF |

Distance vector routing is simpler and requires fewer resources. Link-state routing provides better network-wide topology awareness and is generally more suitable for larger networks.

## 6. Verification and Evidence

The following commands are used to verify the RIP configuration:

```bash
show ip interface brief
show ip route
show ip protocols
show running-config
ping
traceroute
```

Evidence screenshots are stored in:

- [Task 4 Evidence](Evidence/tracer.png)
- [Task 4 Evidence](Evidence/op.png)

| Evidence File | Description |
|---|---|
| topology.png | Five-router network topology |
| python_output.png | Bellman-Ford program output |
| routing_table.png | RIP routing table |
| ping_test.png | Successful connectivity test |
| link_failure.png | Routing behaviour after a link failure |

## Conclusion

Distance vector routing calculates routes through the exchange of distance information between neighbouring routers. The Bellman-Ford algorithm helps determine the shortest paths. RIP implements distance vector routing, while techniques such as split horizon and poison reverse help reduce routing-loop problems.