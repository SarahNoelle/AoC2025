def parse_data(input):
    connections = {}
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            left, right = line.split(":")
            node = left.strip()
            output = right.strip().split() if right.strip() else []
            connections[node] = output

    return connections


def number_of_paths(connections, start, goal):
    paths = []

    def dfs(current, path):
        if current == goal:
            paths.append(paths[:])
            return
        for x in connections.get(current, []):
            if x not in path:
                dfs(x, path+[x])
    
    dfs(start, [start])
    return paths




    


graph = parse_data("input.txt")
paths = number_of_paths(graph, "you", "out")

print("Anzahl Pfade:", len(paths))
print()
for p in paths:
    print(" → ".join(p))
    