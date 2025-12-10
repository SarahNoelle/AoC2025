import re
import pulp

def parse_data_part2(filename):
    machines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lights = re.search(r"\[(.*?)\]", line).group(1)
            button_strings = re.findall(r"\((.*?)\)", line)
            target_string = re.search(r"\{(.*?)\}", line).group(1)
            buttons = [tuple(map(int, b.split(","))) for b in button_strings]
            target = list(map(int, target_string.split(",")))
            machines.append((lights, buttons, target))
    return machines



def solve_machine_ilp_pulp(target, buttons):
    m = len(target)
    n = len(buttons)
    prob = pulp.LpProblem("MinPresses", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]
    prob += pulp.lpSum(x)
    
    for i in range(m):
        prob += pulp.lpSum(x[j] for j, btn in enumerate(buttons) if i in btn) == target[i]
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if pulp.LpStatus[prob.status] == "Optimal":
        return int(sum(v.varValue for v in x))
    else:
        return float('inf')



def total_part2_pulp(filename):
    machines = parse_data_part2(filename)
    total = 0
    for _, buttons, target in machines:
        total += solve_machine_ilp_pulp(target, buttons)
    return total

print(total_part2_pulp("input.txt"))
