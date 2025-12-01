def parse_data(input):
    rotations = []
    with open(input) as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])
            rotations.append((direction, distance))

    return rotations



def count_zeros(rotations):
    position = 50
    res = 0

    for direction, distance in rotations:
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            res = res + 1

    return res



rotations = parse_data("input.txt")
result = count_zeros(rotations)
print(result)

