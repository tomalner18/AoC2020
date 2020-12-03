def split_input(line):
    cond, password = line.split(":")
    password = password.strip()
    bounds, tok = cond.split(" ")
    bounds = bounds.split("-")
    min_bound = int(bounds[0])
    max_bound = int(bounds[1])
    return password, tok, min_bound, max_bound

def solve1(data):
    valid = 0
    for line in data:
        password, tok, min_bound, max_bound = split_input(line)
        if min_bound <= password.count(tok) <= max_bound:
            valid += 1
    return valid

def solve2(data):
    valid = 0
    for line in data:
        password, tok, pos1, pos2 = split_input(line)
        if (password[pos1 - 1] != password[pos2 - 1]) and (password[pos1 - 1] == tok or password[pos2 - 1] == tok):
            valid += 1
    return valid

with open("input.txt") as f:
    data = []
    for line in f:
        data.append(line)
    print(solve1(data))
    print(solve2(data))