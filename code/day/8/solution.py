from utils import load_file
from termcolor import colored

def lines():
    grid = [list(map(int, line)) for line in load_file("data/day/8/input.txt")]
    h = len(grid)
    w = len(grid[0])
    return (grid, h, w)

def visible_for_row(grid, x, y, dx, dy, w, h):
    visible = []
    last = -1
    curr = None
    while x >= 0 and x < w and y >= 0 and y < h:
        curr = grid[y][x]

        if curr > last:
            last = curr
            visible.append((x,y))

        (x, y) = (x + dx, y + dy)

    return visible

def rating(grid, x, y, w, h):
    left = rating_in_direction(grid, x, y, -1, 0, w, h)
    right = rating_in_direction(grid, x, y, 1, 0, w, h)
    down = rating_in_direction(grid, x, y, 0, 1, w, h)
    up =  rating_in_direction(grid, x, y, 0, -1, w, h)
    return left * right * up * down

def rating_in_direction(grid, x, y, dx, dy, w, h):
    num_can_see = 0
    height = grid[y][x]
    while x > 0 and x < w - 1 and y > 0 and y < h - 1:
        (x, y) = (x + dx, y + dy)
        num_can_see += 1

        if grid[y][x] >= height:
            return num_can_see

    return num_can_see

def flatten(l):
    return [item for sub in l for item in sub]

def part1():
    (grid, h, w) = lines()

    left = flatten([visible_for_row(grid, 0, y, 1, 0, w, h) for y in range(h)])
    right = flatten([visible_for_row(grid, w - 1, y, -1, 0, w, h) for y in range(h)])
    top = flatten([visible_for_row(grid, x, 0, 0, 1, w, h) for x in range(w)])
    bottom = flatten([visible_for_row(grid, x, h - 1, 0, -1, w, h) for x in range(w)])

    visible = set(flatten([left, right, top, bottom]))
    return len(list(visible))

def part2():
    (grid, h, w) = lines()

    ratings = [rating(grid, x, y, w, h) for y in range(h) for x in range(w)]
    best = sorted(ratings, reverse=True)[0]
    return best
