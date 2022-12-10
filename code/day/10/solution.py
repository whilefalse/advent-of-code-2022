from utils import stream_file

PCS = [20, 60, 100, 140, 180, 220]

def lines():
    return stream_file("data/day/10/input.txt")

def program():
    for line in lines():
        if line == "noop":
            yield ("noop", 1, None)
        else:
            [_, num] = line.split(" ")
            num = int(num)
            yield ("addx", 2, num)

def update_score(score, pc, x):
    if pc in PCS:
        score += pc * x
    return score

def part1():
    score = 0
    pc = 1
    x = 1
    for (instruction, cycles, arg) in program():
        score = update_score(score, pc, x)
        for cycle in range(cycles - 1):
            pc += 1
            score = update_score(score, pc, x)

        if instruction == "addx":
            x += arg

        pc += 1
    return score

def draw(pc, x):
    if pc % 40 == 1:
        print()

    pixel_drawing = (pc % 40) - 1
    sprite = [x - 1, x, x + 1]
    if pixel_drawing in sprite:
        print('##', end='')
    else:
        print('..', end='')

def part2():
    pc = 1
    x = 1
    for (instruction, cycles, arg) in program():
        draw(pc, x)

        for cycle in range(cycles - 1):
            pc += 1
            draw(pc, x)

        if instruction == "addx":
            x += arg

        pc += 1
    print()
    return None
