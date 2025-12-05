def parse_data(input):
    ranges = []
    ids = []
    with open(input, "r") as f:
        parsing_ranges = True
        for line in f:
            line = line.strip()

            if line == "":
                parsing_ranges = False
                continue

            if parsing_ranges:
                start, end = line.split("-") 
                ranges.append((int(start), int(end)))
            
            else:
                ids.append(int(line))

    return ranges, ids


def count_fresh_index(ranges, ids):
    res = 0
    for id in ids:
        for start, end in ranges:
           if start <= id <= end:
               res = res + 1
               break
    return res


ranges, ids = parse_data("input.txt")
result = count_fresh_index(ranges, ids)
print(result)

