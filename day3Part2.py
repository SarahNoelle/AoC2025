def parse_data(input):

    batterie_banks = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                batterie_banks.append(line)
    return batterie_banks
        
        


def best_digits(bank, k = 12):
    stack = []
    drops = len(bank) - k  

    for n in bank:
        while drops > 0 and stack and stack[-1] < n:
            stack.pop()
            drops -= 1
        stack.append(n)

    result_list = stack[:k]
    s = ""
    for d in result_list:
        s = s + d

    return s 


def largest_joltage(banks, k=12):
    total = 0
    for bank in banks:
        best = best_digits(bank, k)
        total += int(best)
    return total


batterie_banks = parse_data("input.txt")
result = largest_joltage(batterie_banks, 12)
print(result)

