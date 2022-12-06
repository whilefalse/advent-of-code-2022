from utils import stream_file_characters

def chars():
    return stream_file_characters("data/day/6/input.txt")

def find_marker(n):
    lastn = []
    for i, char in enumerate(chars()):
        if len(lastn) == n:
            lastn = lastn[1:]
            lastn.append(char)
        else:
            lastn.append(char)

        if len(list(set(lastn))) == n:
            return i + 1

def part1():
    return find_marker(4)

def part2():
    return find_marker(14)
