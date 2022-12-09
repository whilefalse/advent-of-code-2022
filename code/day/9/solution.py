import math
from utils import stream_file

DX = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
DY = {'R': 0, 'L': 0, 'U': -1, 'D': 1}

def lines():
    return stream_file("data/day/9/input.txt")

def instructions():
    all = []
    for line in lines():
        [direction, times] = line.split(" ")
        all.extend([direction] * int(times))
    return all

def move(head, instruction):
    (x, y) = head
    return (x + DX[instruction], y + DY[instruction])

def catch_up(head, tail):
    (hx, hy) = head
    (tx, ty) = tail
    dx = hx - tx
    dy = hy - ty

    if abs(dx) > 1 or abs(dy) > 1:
        newdx = max(0, abs(dx) - 1)
        newdy = max(0, abs(dy) - 1)

        tx = hx - math.copysign(newdx, dx)
        ty = hy - math.copysign(newdy, dy)

    return (tx, ty)

def part1():
    head = (0, 0)
    tail = (0, 0)
    seen = set([tail])

    for instruction in instructions():
        head = move(head, instruction)
        tail = catch_up(head, tail)
        seen.add(tail)

    return len(list(seen))

def visualise(head, tails):
    for y in range(-10, 10):
        for x in range(-10, 10):
            if (x, y) == head:
                print('H', end='')
            elif (x, y) in tails:
                i = tails.index((x, y))
                print(i + 1, end='')
            else:
                print('*', end='')
        print()

def part2():
    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]
    seen = set([head])

    for instruction in instructions():
        # visualise(head, tails)
        # print()
        # print(instruction)
        head = move(head, instruction)

        tails[0] = catch_up(head, tails[0])
        for i in range(8):
            tails[i + 1] = catch_up(tails[i], tails[i + 1])

        seen.add(tails[-1])

    return len(list(seen))
