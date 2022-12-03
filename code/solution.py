import sys

if __name__ == "__main__":
    day = sys.argv[1]
    print("Solving day %s" % day)

    mod = __import__("day.%s" % day, globals(), locals(), ["solution"])
    print("Part 1: %s" % mod.solution.part1())
    print("Part 2: %s" % mod.solution.part2())
