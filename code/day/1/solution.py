def get_elves():
    elves = []
    current = 0
    with open("data/day/1/input.txt", 'r') as f:
        for line in f:
            line = line.strip()
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



if __name__ == "__main__":
    print(part1())
    print(part2())
