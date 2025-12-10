import re
from itertools import product

def parse_data(filename):
    machines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            lights = re.search(r"\[(.*?)\]", line).group(1)
            buttons = re.findall(r"\((.*?)\)", line)
            buttons = [tuple(map(int, b.split(","))) for b in buttons]
            
            machines.append((lights, buttons))
    return machines

def gauss_elimination(A, b):
    n_rows = len(A)
    n_cols = len(A[0])

    A = [row[:] for row in A]  
    b = b[:]

    pivot_cols = []
    row = 0

    for col in range(n_cols):
        
        pivot = None
        for r in range(row, n_rows):
            if A[r][col] == 1:
                pivot = r
                break

        if pivot is None:
            continue 
        
        
        A[row], A[pivot] = A[pivot], A[row]
        b[row], b[pivot] = b[pivot], b[row]

        pivot_cols.append(col)

        for r in range(n_rows):
            if r != row and A[r][col] == 1:
                
                A[r] = [(A[r][c] ^ A[row][c]) for c in range(n_cols)]
                b[r] = b[r] ^ b[row]

        row += 1
        if row == n_rows:
            break

    return A, b, pivot_cols


def min_press(A, b):
    A_r, b_r, pivots = gauss_elimination(A, b)

    n_rows = len(A)
    n_cols = len(A[0])

    pivot_set = set(pivots)
    free_vars = [c for c in range(n_cols) if c not in pivot_set]

    min_presses = None

    
    for free_choice in product([0,1], repeat=len(free_vars)):
        x = [0]*n_cols

        for val, col in zip(free_choice, free_vars):
            x[col] = val

        for r, col in enumerate(pivots):
            
            s = 0
            for j in range(n_cols):
                if j != col and A_r[r][j] == 1:
                    s ^= x[j]
            x[col] = s ^ b_r[r]

        presses = sum(x)

        if min_presses is None or presses < min_presses:
            min_presses = presses

    return min_presses




def total_minimum(filename):
    machines = parse_data(filename)
    total = 0

    for lights, buttons in machines:

        n_lights = len(lights)
        n_buttons = len(buttons)

        b = [1 if c == "#" else 0 for c in lights]

        A = []
        for light in range(n_lights):
            row = []
            for btn in range(n_buttons):
                row.append(1 if light in buttons[btn] else 0)
            A.append(row)

        presses = min_press(A, b)
        total += presses

    return total


print(total_minimum("input.txt"))