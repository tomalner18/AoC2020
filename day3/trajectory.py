def solve1(data):
    trees = 0
    x = 0
    for i in data:
        if i[x % len(i)] == '#':
            trees += 1
        x += 3
    return trees

def solve2(data):
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [0, 0, 0, 0, 0]
    l = len(data[0])
    for idx, (xx, yy) in enumerate(moves):
        x = 0
        y = 0
        for n, i in enumerate(data):
            if yy == 2 and n % 2 != 0:
                continue
            if i[x % l] == '#':
                trees[idx] += 1
            x += xx
            y += yy
    prod = 1
    for t in trees:
        prod *= t
    return prod


with open("input.txt") as f:
    data = []
    for line in f:
        data.append(line.strip())
    print(solve1(data))
    print(solve2(data))