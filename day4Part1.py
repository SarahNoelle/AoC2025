def parse_data(input):
    grid = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    return grid


def count_neighbours(grid):
    height = len(grid)
    width = len(grid[0])


    #directions
    dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    res = 0
    

    for x in range(height):
        for y in range(width):
            if grid[x][y] != "@":
                continue
            neighbours = 0
            for dx, dy in dirs:
                nx, ny =  x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width:
                    if grid[nx][ny] == "@":
                        neighbours += 1

            if neighbours < 4:
                res += 1

    return res


grid = parse_data("input.txt")
result = count_neighbours(grid)
print(result)
    