# Longest Prefix Match Calculations

## Given Routing Table

| Network | Prefix Length | Next Hop |
|---|---:|---|
| 10.0.0.0 | /8 | 192.0.2.1 |
| 10.1.0.0 | /16 | 192.0.2.5 |
| 10.1.2.0 | /24 | 192.0.2.9 |
| 10.1.2.128 | /25 | 192.0.2.13 |
| 0.0.0.0 | /0 | 198.51.100.1 |

## Destination Analysis

### 1. Destination: 10.1.2.200

Matches 10.0.0.0/8, 10.1.0.0/16, 10.1.2.0/24 and 10.1.2.128/25.

The most specific matching route is /25.

**Selected next hop:** 192.0.2.13

### 2. Destination: 10.1.2.100

Matches /8, /16 and /24. It does not belong to 10.1.2.128/25.

**Selected next hop:** 192.0.2.9

### 3. Destination: 10.1.9.9

Matches 10.0.0.0/8 and 10.1.0.0/16.

**Selected next hop:** 192.0.2.5

### 4. Destination: 10.7.7.7

Matches only 10.0.0.0/8 among the listed specific routes.

**Selected next hop:** 192.0.2.1

### 5. Destination: 8.8.8.8

Does not match any specific network. The default route is selected.

**Selected next hop:** 198.51.100.1

## Final Result

The router forwards packets using the route with the longest matching prefix. If no specific route matches, it uses the default route, provided one is available.