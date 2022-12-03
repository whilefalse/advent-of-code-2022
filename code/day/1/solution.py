from utils import stream_file

def get_elves():
    elves = []
    current = 0
    for line in stream_file("data/day/1/input.txt"):
        if line:
            current = current + int(line)
        else:
            elves.append(current)
            current = 0

    return elves

def part1():
    elves = get_elves()
    return sorted(elves, reverse=True)[0]

def part2():
    elves = get_elves()
    return sum(sorted(elves, reverse=True)[0:3])
