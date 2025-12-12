
def parse_data(path):
    shapes = []
    regions = []

    with open(path) as f:
        lines = [line.rstrip("\n") for line in f]

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if ":" in line and line.split(":")[0].isdigit():
            i += 1
            shape = []
            while i < len(lines) and lines[i] and not lines[i].endswith(":"):
                shape.append(lines[i])
                i += 1
            shapes.append(tuple(shape))
            continue
        break

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        dims, rest = line.split(":")
        W, H = map(int, dims.split("x"))
        counts = list(map(int, rest.split()))
        regions.append((W, H, counts))
        i += 1

    return shapes, regions


def shape_stats(shape):
    area = 0
    for row in shape:
        for c in row:
            if c == "#":
                area += 1
    return 0, 0, area 



def can_fit_region(W, H, counts, shapes):
    total_area = sum(shape_stats(shapes[i])[2] * cnt for i, cnt in enumerate(counts))
    if total_area > W * H:
        return False

    for i, cnt in enumerate(counts):
        if cnt == 0:
            continue
        shape = shapes[i]
        h = len(shape)
        w = max(len(row) for row in shape)
        if h > H and w > H:
            return False
        if h > W and w > W:
            return False

    
    return True

def solve(data):
    shapes, regions = data
    valid = 0
    for (W, H, counts) in regions:
        if can_fit_region(W, H, counts, shapes):
            valid += 1
    return valid


data = parse_data("input.txt")
result = solve(data)
print(result)
