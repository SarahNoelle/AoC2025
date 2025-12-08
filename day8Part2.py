import math


def parse_data(input):
    junction_boxes = []
    with open(input,"r") as f:
        for line in f:
            line = line.strip()
            x, y, z = line.split(",")
            junction_boxes.append((int(x),int(y),int(z)))

    return junction_boxes



def make_union_find(n):
    parent = list(range(n))
    size = [1]*n
    return parent, size



def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]


def union(parent, size, elem_a, elem_b):
    elem_a = find(parent, elem_a)
    elem_b = find(parent, elem_b)

    if elem_a == elem_b:
        return False
    
    if size[elem_a] < size[elem_b]:
        elem_a, elem_b = elem_b, elem_a

    parent[elem_b] = elem_a
    size[elem_a] += size[elem_b]

    return True




def euclidean_dist(junction_boxes):
    length = len(junction_boxes)
    parent, size = make_union_find(length)
    components = length

    edges = []

    for i in range(length):
        x1, y1, z1 = junction_boxes[i]
        for j in range(i+1, length):
            x2, y2, z2 = junction_boxes[j]
            d = math.dist((x1, y1, z1), (x2, y2, z2))
            edges.append((d, i, j))

    edges.sort()

    for d2, a, b in edges:
        merged = union(parent, size, a, b)
        if merged:
            components -= 1
            if components == 1:
                x_a = junction_boxes[a][0]
                x_b = junction_boxes[b][0]
                return x_a * x_b


input = parse_data("input.txt")
result = euclidean_dist(input)
print(result)