nodes = ("A", "B", "C", "D", "E")
distances = {
    "B": {"A": 5, "D": 1},
    "A": {"B": 5, "D": 3, "E": 12},
    "D": {"B": 1, "E": 1, "A": 3},
    "G": {"B": 2, "D": 1, "C": 2},
    "C": {"E": 1},
    "E": {"A": 12, "D": 1, "C": 1},
    "F": {"A": 5, "E": 2, "C": 16},
}

unvisited = {node: None for node in nodes}
visited = {}
current = "A"
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited)
