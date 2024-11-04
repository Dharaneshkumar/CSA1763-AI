import itertools
def is_valid_solution(s, e, n, d, m, o, r, y):
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    return send + more == money
def solve_cryptarithmetic():
    letters = 'sendmory'
    for perm in itertools.permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0:
            continue
        if is_valid_solution(s, e, n, d, m, o, r, y):
            print(f"SEND + MORE = MONEY")
            print(f"{s}{e}{n}{d} + {m}{o}{r}{e} = {m}{o}{n}{e}{y}")
            return
    print("No solution found.")
solve_cryptarithmetic()
