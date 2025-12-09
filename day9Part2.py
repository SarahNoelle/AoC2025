
def parse_data(path):
    points = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            points.append((x, y))
    return points


def compress(values):
    values = sorted(set(values))
    m = {}
    back = {}
    last = None
    idx = 0
    for v in values:
        if last is not None:
            back[idx] = v - last - 1
            idx += 1
        m[v] = idx
        back[idx] = 1
        idx += 1
        last = v
    return m, back


def inside_polygon(vertices):
    vertical_edges = []
    tiles = set()

    for (x1, y1), (x2, y2) in zip(vertices, vertices[1:] + vertices[:1]):
        if x1 == x2:
            if y1 < y2:
                vertical_edges.append((x1, y1, y2, True))
            else:
                vertical_edges.append((x1, y2, y1, False))
        else:
            
            y = y1
            for x in range(min(x1, x2), max(x1, x2) + 1):
                tiles.add((x, y))

    minx = min(x for x, y in vertices)
    maxx = max(x for x, y in vertices)
    miny = min(y for x, y in vertices)
    maxy = max(y for x, y in vertices)

    for y in range(miny, maxy + 1):
        inside = False
        last_dir = None

        for x in range(minx, maxx + 1):
            hit_edge = False

            for ex, ey1, ey2, direction in vertical_edges:
                if x == ex and ey1 <= y <= ey2:
                    if direction != last_dir:
                        hit_edge = True
                        last_dir = direction
                        break

            if hit_edge:
                tiles.add((x, y))
                inside = not inside
                continue

            if inside:
                tiles.add((x, y))

    return tiles


def compute_area(area_set, x_back, y_back):
    s = 0
    for x, y in area_set:
        s += x_back[x] * y_back[y]
    return s


def largest_rectangle_optimized(points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]

    x_map, x_back = compress(xs)
    y_map, y_back = compress(ys)

    vertices = [(x_map[x], y_map[y]) for x, y in points]

    valid_tiles = inside_polygon(vertices)

    candidates = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            candidates.append((vertices[i], vertices[j]))

    candidates.sort(reverse=True)

    best = 0

    for (x1, y1), (x2, y2) in candidates:
        xa, xb = sorted((x1, x2))
        ya, yb = sorted((y1, y2))

        ok = True
        for px, py in vertices:
            if xa < px < xb and ya < py < yb:
                ok = False
                break
        if not ok:
            continue

        area_tiles = {(x, y)
                      for x in range(xa, xb + 1)
                      for y in range(ya, yb + 1)}

        if not area_tiles.issubset(valid_tiles):
            continue

        area = compute_area(area_tiles, x_back, y_back)
        best = max(best, area)

    return best




points = parse_data("input.txt")
result = largest_rectangle_optimized(points)
print(result)
