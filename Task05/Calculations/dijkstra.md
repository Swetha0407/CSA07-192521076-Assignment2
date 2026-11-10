# Dijkstra's Shortest Path Algorithm

## 1. Given Network

The following six-router network is used. The values represent link costs.

| Link | Cost |
|---|---:|
| R1 – R2 | 10 |
| R1 – R3 | 5 |
| R2 – R3 | 2 |
| R2 – R4 | 1 |
| R3 – R4 | 9 |
| R3 – R5 | 2 |
| R4 – R6 | 4 |
| R5 – R6 | 6 |

The shortest paths are calculated from source router R1.

## 2. Dijkstra's Algorithm

1. Set the distance of the source router R1 to zero.
2. Set all other router distances to infinity.
3. Select the unvisited router with the smallest tentative distance.
4. Update the distances of its neighbouring routers.
5. Mark the selected router as visited.
6. Repeat until all reachable routers are visited.

## 3. Step-by-Step Calculation

**Initial distances:**

| Router | R1 | R2 | R3 | R4 | R5 | R6 |
|---|---:|---:|---:|---:|---:|---:|
| Distance | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |

**Step 1 – Visit R1**

R1 connects to R2 with cost 10 and R3 with cost 5.

Distances: R2 = 10, R3 = 5.

**Step 2 – Visit R3**

R3 has the smallest tentative distance of 5.

- R2 = min(10, 5 + 2) = 7
- R4 = 5 + 9 = 14
- R5 = 5 + 2 = 7

**Step 3 – Visit R2**

R2 has distance 7.

- R4 = min(14, 7 + 1) = 8

**Step 4 – Visit R5**

R5 has distance 7.

- R6 = 7 + 6 = 13

**Step 5 – Visit R4**

R4 has distance 8.

- R6 = min(13, 8 + 4) = 12

**Step 6 – Visit R6**

R6 has distance 12. All routers have now been visited.

## 4. Final Shortest Path Table

| Destination | Shortest Path | Total Cost |
|---|---|---:|
| R1 | R1 | 0 |
| R2 | R1 → R3 → R2 | 7 |
| R3 | R1 → R3 | 5 |
| R4 | R1 → R3 → R2 → R4 | 8 |
| R5 | R1 → R3 → R5 | 7 |
| R6 | R1 → R3 → R2 → R4 → R6 | 12 |

## 5. Reference Bandwidth Selection

OSPF cost is calculated using:

**Cost = Reference Bandwidth / Interface Bandwidth**

Default reference bandwidth = 100 Mbps.

At higher interface speeds, the default calculation can produce the same minimum integer cost for different interfaces.

A reference bandwidth of 10,000 Mbps is selected to distinguish the following speeds:

| Bandwidth | Calculation | Cost |
|---|---|---:|
| 10 Mbps | 10000 / 10 | 1000 |
| 100 Mbps | 10000 / 100 | 100 |
| 1 Gbps | 10000 / 1000 | 10 |
| 10 Gbps | 10000 / 10000 | 1 |

This reference bandwidth should be configured consistently on all OSPF routers.

## Conclusion

Dijkstra's algorithm calculates the shortest path by repeatedly selecting the router with the lowest tentative cost and updating its neighbours. From R1, the shortest route to R6 is R1 → R3 → R2 → R4 → R6, with a total cost of 12.