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


def count_fresh_index(ranges):
    res = 0
    ranges_sorted = sorted(ranges, key = lambda r: r[0])
    merged = []
    cur_start, cur_end = ranges_sorted[0]

    for start, end in ranges_sorted[1:]:
        if start <= cur_end + 1 :
            cur_end = max(cur_end, end)

        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    res = sum(end - start + 1 for start, end in merged)
    return res



ranges, ids = parse_data("input.txt")
result = count_fresh_index(ranges)
print(result)

