# Distance Vector Routing – Calculations

## Given Link Costs

| Link | Cost |
|---|---:|
| A–B | 2 |
| A–C | 7 |
| B–C | 3 |
| B–D | 8 |
| C–D | 1 |
| D–E | 4 |

## Bellman-Ford Equation

The distance vector update equation is:

**Dₓ(y) = min [c(x,v) + Dᵥ(y)]**

Where:

- Dₓ(y) is the estimated cost from router x to destination y.
- c(x,v) is the direct link cost from router x to neighbour v.
- Dᵥ(y) is the neighbour's estimated cost to destination y.

Each router compares the direct cost with the cost obtained through its neighbours and selects the minimum.

## Final Shortest-Path Distance Table

| Router | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| A | 0 | 2 | 5 | 6 | 10 |
| B | 2 | 0 | 3 | 4 | 8 |
| C | 5 | 3 | 0 | 1 | 5 |
| D | 6 | 4 | 1 | 0 | 4 |
| E | 10 | 8 | 5 | 4 | 0 |

## Shortest Path Examples

### From A to E

A → B → C → D → E

Cost = 2 + 3 + 1 + 4 = **10**

### From B to D

B → C → D

Cost = 3 + 1 = **4**

### From A to D

A → B → C → D

Cost = 2 + 3 + 1 = **6**

### From C to E

C → D → E

Cost = 1 + 4 = **5**

## Convergence

The algorithm starts with each router knowing only its directly connected neighbours. Routers exchange their distance vectors and update their route estimates over successive rounds.

The Python simulation converges after **4 rounds**, including the final round in which no further changes occur.

## Link Failure Analysis

If the C–D link fails, the network recalculates its shortest paths using the remaining links.

| Router | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| A | 0 | 2 | 5 | 10 | 14 |
| B | 2 | 0 | 3 | 8 | 12 |
| C | 5 | 3 | 0 | 11 | 15 |
| D | 10 | 8 | 11 | 0 | 4 |
| E | 14 | 12 | 15 | 4 | 0 |

For example, after the C–D failure, the route from A to E becomes:

A → B → D → E

Cost = 2 + 8 + 4 = **14**

The network remains connected through the alternate path.

## Conclusion

Distance vector routing uses information exchanged between neighbouring routers to calculate shortest paths. The Bellman-Ford algorithm updates the distance table until all routers reach stable route estimates. When a link fails, the routers recalculate their routes using the remaining available paths.