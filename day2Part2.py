def parse_data(input):
    ranges = []
    with open(input, "r") as f:
       content = f.read().strip()
    
    for chunk in content.split(","):
        start, end = chunk.split("-")
        ranges.append((int(start), int(end)))
    return ranges



def valid_id(id):
    s = str(id)
    n = len(s)

    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        block = s[:size]
        if block * (n // size) == s:
            return True
    return False



def sum_invalid_ids(ranges):
    res = 0
    for start,end in ranges:
        for id in range(start, end + 1):
            if valid_id(id):
                res = res + id

    return res

ranges = parse_data("input.txt")
result = sum_invalid_ids(ranges)
print(result)
