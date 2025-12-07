from collections import deque


def parse_data(input):

    grid = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            grid.append(line)
    
    return grid


def count_splits(grid):

    rows = len(grid)
    columns = len(grid[0])
    start_idx = grid[0].index('S')
    queue = deque()
    queue.append((0, start_idx))
    res = 0
    visited = set()

    while queue:
        r, c = queue.popleft()

        if r < 0 or r >= rows or c >= columns:
            continue

        if(r, c) in visited:
            continue

        visited.add((r, c))
        cell = grid[r][c]

        if cell == '^':
            res = res + 1
            queue.append((r, c-1))
            queue.append((r, c+1))
            continue

        queue.append((r+1, c))

    return res 





grid = parse_data("input.txt")
result = count_splits(grid)
print(result)

