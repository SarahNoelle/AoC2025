def parse_data(input):
    points = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(","))
            points.append((x,y))
    return points


def largest_rectangle(points):
    max_area = 0
    length = len(points)

    for i in range(length):
        x1, y1 = points[i]
        for j in range(i+1, length):
            x2, y2 = points[j]
            width = abs(x2-x1)+1
            height = abs(y2-y1)+1

            area = width*height
            if area > max_area:
                max_area = area

    return max_area


points = parse_data("input.txt")
result = largest_rectangle(points)
print(result)
