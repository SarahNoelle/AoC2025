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

    edges = []

    # Calculate all distances
    for i in range(length):
        x1, y1, z1 = junction_boxes[i]
        for j in range(i+1, length):
            x2, y2, z2 = junction_boxes[j]
            d = math.dist((x1, y1, z1), (x2, y2, z2))
            edges.append((d, i, j))

    edges.sort()

    #group the first 1000 connections
    K = 1000
    for d, a, b in edges[:K]:
        union(parent, size, a, b)

    #a circuit is the root of a union-find pattern
    components = {}
    for i in range(length):
        root = find(parent, i)
        components[root] = components.get(root, 0) + 1


    largest = sorted(components.values(), reverse=True)[:3]
    return largest[0] * largest[1] * largest[2]



input = parse_data("input.txt")
result = euclidean_dist(input)
print(result)