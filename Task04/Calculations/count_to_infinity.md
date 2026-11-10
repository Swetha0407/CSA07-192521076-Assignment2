# Count-to-Infinity Problem

## 1. Introduction

Count-to-infinity is a problem in distance vector routing that occurs when routers continue increasing their distance estimates to a destination after a network link fails.

This happens because routers may receive outdated information from their neighbours and incorrectly believe that an alternative route still exists.

## 2. Example Network

Consider three routers connected in a line:

**X — Y — Z**

Initially:

- X reaches Z through Y.
- Y has a direct connection to Z.
- The cost of each link is 1.

Therefore:

| Router | Distance to Z |
|---|---:|
| X | 2 |
| Y | 1 |
| Z | 0 |

## 3. Link Failure

Suppose the Y–Z link fails.

Router Y loses its direct connection to Z. However, X may still advertise its old distance of 2 to Z.

Y may incorrectly calculate a new route through X:

Cost from Y to Z = 1 + 2 = 3.

X may then receive Y's updated distance and calculate:

Cost from X to Z = 1 + 3 = 4.

The routers continue increasing their estimates because each believes the other has a valid route.

A simplified sequence is:

| Update | X's Distance to Z | Y's Distance to Z |
|---|---:|---:|
| Before failure | 2 | 1 |
| After failure | 2 | 3 |
| Next update | 4 | 3 |
| Next update | 4 | 5 |
| Next update | 6 | 5 |
| Next update | 6 | 7 |

The values keep increasing until the routing protocol's maximum metric is reached. In RIP, infinity is defined as 16 hops.

## 4. Poison Reverse

Poison reverse is a technique used to reduce routing loops.

When a router learns a route through a particular neighbour, it advertises that route back to the same neighbour with an infinite metric.

For example:

- Y learns the route to Z through X.
- Y advertises the route to Z back to X with metric 16.
- X understands that Y must not use X as an alternative route to Z.

This prevents the two routers from continuously using each other as the next hop for the same destination.

## 5. Conclusion

Count-to-infinity occurs when routers use outdated routing information after a link failure. Split horizon and poison reverse help prevent routing loops and improve distance vector routing stability. RIP also uses a maximum hop count of 15, with 16 representing an unreachable destination.