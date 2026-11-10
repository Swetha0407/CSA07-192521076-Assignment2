
"""Distance Vector Routing using the Bellman-Ford algorithm."""

NAMES = ["A", "B", "C", "D", "E"]
INF = float("inf")

# Undirected links and their costs
links = {
    ("A", "B"): 2,
    ("A", "C"): 7,
    ("B", "C"): 3,
    ("B", "D"): 8,
    ("C", "D"): 1,
    ("D", "E"): 4,
}

# Create a direct-link cost table
cost = {u: {v: INF for v in NAMES} for u in NAMES}

for u in NAMES:
    cost[u][u] = 0

for (u, v), weight in links.items():
    cost[u][v] = weight
    cost[v][u] = weight

# Initially, each router knows only its direct neighbours
table = {u: cost[u].copy() for u in NAMES}

rounds = 0

while True:
    old = {u: table[u].copy() for u in NAMES}
    changed = False

    # Each router updates its vector using neighbours' old vectors
    for u in NAMES:
        for n in NAMES:
            if cost[u][n] != INF and u != n:
                for dest in NAMES:
                    if old[n][dest] != INF:
                        new_cost = cost[u][n] + old[n][dest]

                        if new_cost < table[u][dest]:
                            table[u][dest] = new_cost
                            changed = True

    rounds += 1

    if not changed:
        break

print(f"Converged after {rounds} rounds")
print("Router  " + "  ".join(NAMES))

for u in NAMES:
    values = [
        "-" if table[u][v] == INF else str(int(table[u][v]))
        for v in NAMES
    ]
    print(f"{u:<8}" + "  ".join(values))
