from collections import defaultdict

def parse_data(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            grid.append(line)
    return grid



def count_timelines(grid): 
    start_column = grid[0].index('S')
    beams = defaultdict(int)
    beams[start_column] = 1

    for row in grid[1:]:
        new = defaultdict(int)
        for c, count in beams.items():
            if row[c] == '^':
                new[c-1] += count
                new[c+1] += count
                  
            else:
                new[c] += count
        beams = new
    
    res = sum(beams.values())
    return res




grid = parse_data("input.txt")
result = count_timelines(grid)
print(result)
