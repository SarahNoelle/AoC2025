from collections import Counter
from typing import Dict, List, Tuple

def parse_data(path: str) -> Dict[str, List[str]]:
    graph = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(":")
            node = left.strip()
            outputs = right.strip().split() if right.strip() else []
            graph[node] = outputs
    return graph

def count_paths_with_flags(graph: Dict[str, List[str]], start: str, goal: str,special1: str = "dac", special2: str = "fft"):
    memo: Dict[str, Counter] = {}

    def dfs(node: str) -> Counter:
        if node == goal:
            key = (node == special1, node == special2)
            return Counter({key: 1})

        if node in memo:
            return memo[node]

        total = Counter()
        for x in graph.get(node, []):
            x_counts = dfs(x)
            is_s1 = (node == special1)
            is_s2 = (node == special2)
            for (d_seen, f_seen), cnt in x_counts.items():
                new_key = (d_seen or is_s1, f_seen or is_s2)
                total[new_key] += cnt

        memo[node] = total
        return total

    counts_from_start = dfs(start)
    return sum(cnt for (d,f), cnt in counts_from_start.items() if d and f)


graph = parse_data("input.txt")
result = count_paths_with_flags(graph, "svr", "out", "dac", "fft")
print(result)
