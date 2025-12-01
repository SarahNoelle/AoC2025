def parse_data(input_path):
    rotations = []
    with open(input_path, "r") as f:
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
            first_h = position if position != 0 else 100
            if distance < first_h:
                hits = 0
            else:
                hits = 1 + (distance - first_h) // 100
            res += hits
            position = (position - distance) % 100
            
        else:  
            hits = (position + distance) // 100
            res += hits
            position = (position + distance) % 100
            

    return res



rotations = parse_data("input.txt")
result = count_zeros(rotations)
print(result)
