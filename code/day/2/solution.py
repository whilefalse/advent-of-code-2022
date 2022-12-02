SCORES = {"A": 1, "B": 2, "C": 3}
BEATS = {"A": "C", "B": "A", "C": "B"}
LOSES = dict([(v, k) for (k,v) in BEATS.items()])

def total_score(move_fun):
    score = 0
    with open("data/day/2/input.txt", 'r') as f:
        for line in f:
            [left, right] = line.strip().split(" ")
            right = chr(ord(right) - 23)
            right = move_fun(left, right)
            score += move_score(right) + game_score(left, right)

    return score

def move_score(move):
    return SCORES[move]

def game_score(left, right):
    if BEATS[right] == left:
        return 6
    elif LOSES[right] == left:
        return 0
    else:
        return 3

def part1():
    return total_score(lambda l, r: r)

def part2_move(left, right):
    if right == "A":
        return BEATS[left]
    elif right == "B":
        return left
    else:
        return LOSES[left]

def part2():
    return total_score(part2_move)


if __name__ == "__main__":
    print(part1())
    print(part2())
