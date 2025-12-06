import math
from math import prod

def parse_data(input_file):
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]
    return lines




def part1(data):
    
    split_lines = [line.split() for line in data]
    num_rows = len(split_lines) - 1
    num_cols = len(split_lines[0])
    
    res = 0
    for col_idx in range(num_cols):
        numbers = [int(split_lines[row][col_idx]) for row in range(num_rows)]
        operator = split_lines[-1][col_idx]
        res += prod(numbers) if operator == '*' else sum(numbers)
    
    return res


################################## Part 2 ##########################################

def part2(data, right_to_left=False):
    #all numbers to same length
    max_width = max(len(line) for line in data)
    padded = [line.ljust(max_width) for line in data]
    
    res = 0
    problem_numbers = []
    
    col_indices = reversed(range(max_width)) if right_to_left else range(max_width)
    
    for col_idx in col_indices:
        col = [line[col_idx] for line in padded]
        num_str = ''.join(col[:-1]).strip()
        
        if num_str == '':
            # empty col is a divider
            if problem_numbers:
                operator = prev_op
                res += math.prod(problem_numbers) if operator == '*' else sum(problem_numbers)
                problem_numbers = []
            continue
        
        
        problem_numbers.append(int(num_str))
        prev_op = col[-1]  # Operator is last
    
    
    if problem_numbers:
        operator = prev_op
        res += math.prod(problem_numbers) if operator == '*' else sum(problem_numbers)
    
    return res



data = parse_data("input.txt")
result1 = part1(data)
print("Part 1:", result1)
result2 = part2(data, right_to_left=True)
print("Part 2:", result2)