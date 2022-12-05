from utils import stream_file
from collections import defaultdict
import re

LINE_REGEX = r"(?:(\[[A-Z]\]|\s{4}))"
INSTRUCTION_REGEX = r"move (\d+) from (\d+) to (\d+)"

def parse():
    stacks = defaultdict(lambda: [])
    instructions = []
    parsing = "lines"
    for line in stream_file("data/day/5/input.txt"):
        if line.strip() == "":
            parsing = "instructions"

        elif parsing == "lines":
            match = re.findall(LINE_REGEX, line)
            for i, m in enumerate(match):
                if m.strip() != "":
                    stacks[i].append(re.sub(r'[\[\]]', "", m))
        else:
            match = re.match(INSTRUCTION_REGEX, line)
            instructions.append(tuple(map(int, match.groups())))
    stacks = [list(reversed(v)) for (_,v) in sorted(stacks.items())]
    return (stacks, instructions)

def part1():
    (stacks, instructions) = parse()
    for (num, fr, to) in instructions:
        for _ in range(num):
            popped = stacks[fr - 1].pop()
            stacks[to - 1].append(popped)
    return "".join([stack[-1] for stack in stacks])


def part2():
    (stacks, instructions) = parse()
    for (num, fr, to) in instructions:
        popped = stacks[fr - 1][-num:]
        stacks[fr - 1] = stacks[fr - 1][:-num]
        stacks[to - 1].extend(popped)
    return "".join([stack[-1] for stack in stacks])
