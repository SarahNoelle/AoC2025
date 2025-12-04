def parse_data(input):
    grid = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))

    return grid


def count_neighbours(grid):
    height = len(grid)
    width = len(grid[0])


    #directions
    dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    accesible = []
    

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
                accesible.append((x, y))

    return accesible


def remove(grid):
    res = 0

    while True:
        removable = count_neighbours(grid)
        if not removable:
            break

        for x, y in removable:
            grid[x][y] = "."
        
        res = res + len(removable)

    return res


grid = parse_data("input.txt")
result = remove(grid)
print(result)
    