def parse_data(input):

    batterie_banks = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                batterie_banks.append(line)
    return batterie_banks
        
        


def largest_joltage(batterie_banks):
    res = 0
    for bank in batterie_banks:
        largest = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                val = int(bank[i]) * 10 + int(bank[j])
                if val > largest:
                    largest = val
        res += largest
    return res
        


batterie_banks = parse_data("input.txt")
result = largest_joltage(batterie_banks)
print(result)

