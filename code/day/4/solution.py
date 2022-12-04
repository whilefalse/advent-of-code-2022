from utils import stream_file

def lines():
    return stream_file("data/day/4/input.txt")

def expand_range(string):
    return map(int, string.split("-"))

def boundaries():
    for line in lines():
        [left, right] = line.split(",")
        [ls, le] = expand_range(left)
        [rs, re] = expand_range(right)
        yield (ls, le, rs, re)


def part1():
    return sum(
        1 for (ls, le, rs, re) in boundaries()
        if (ls <= rs and le >= re) or (rs <= ls and re >= le)
    )


def part2():
    return count(
        1 for (ls, le, rs, re) in boundaries()
        if (ls <= rs and le >= rs) or (rs <= ls and re >= ls)
    )
