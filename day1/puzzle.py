def solve1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j

def solve2(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k

with open('input.txt') as f:
    data = []
    for line in f:
        data.append(int(line))
    print(solve1(data))
    print(solve2(data))
