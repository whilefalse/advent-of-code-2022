from utils import stream_file
from functools import reduce

def points(char):
    if ord(char) > 96:
        return ord(char) - 96
    else:
        return ord(char) - 38

def part1():
    sum = 0
    for line in stream_file("data/day/3/input.txt"):
        split = int(len(line) / 2)
        [left, right] = [line[:split], line[split:]]
        overlap = list(set(left).intersection(set(right)))[0]
        sum += points(overlap)
    return sum

def part2():
    sum = 0
    current = []
    for i, line in enumerate(stream_file("data/day/3/input.txt")):
        current.append(line)
        if i % 3 == 2:
            sets = [set(l) for l in current]
            common = reduce(lambda a, b: a.intersection(b), sets)
            sum += points(list(common)[0])
            current = []

    return sum


