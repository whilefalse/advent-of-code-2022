import math
from utils import stream_file

class Monkey(object):
    def __init__(self, i, items, op, test, if_true, if_false):
        self.i = i
        self.items = items
        self.orig_items = list(items)
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def __str__(self):
        return "Monkey %s: [%s], Inspected: %s, Test: %s, If true: %s, If false: %s" % (self.i, ", ".join(map(str, self.items)), self.inspected, self.test, self.if_true, self.if_false)

    def who_to_send_to(self, item):
        if item % self.test == 0:
            return (self.if_true, True)
        else:
            return (self.if_false, False)

def lines():
    return stream_file("data/day/11/input.txt")

def get_op(line):
    [_, _, _, op, arg] = line.split(" ")
    if op == "*":
        func = lambda x, y: x * y
        func.op = '*'
        return (func, lambda x: x, lambda x: x if arg == "old" else int(arg))
    if op == "+":
        func = lambda x, y: x + y
        func.op = '+'
        return (func, lambda x: x, lambda x: x if arg == "old" else int(arg))

def monkeys():
    monkeys = []

    it = lines()
    while True:
        i = int(next(it).replace("Monkey ", "").replace(":", ""))
        items = list(map(int, next(it).strip().replace("Starting items: ", "").split(", ")))
        op = get_op(next(it).strip().replace("Operation: ", ""))
        test = int(next(it).strip().replace("Test: divisible by ", ""))
        if_true = int(next(it).strip().replace("If true: throw to monkey ", ""))
        if_false = int(next(it).strip().replace("If false: throw to monkey ", ""))
        monkeys.append(Monkey(i, items, op, test, if_true, if_false))
        try:
            next(it)
        except StopIteration:
            break

    return monkeys

def round_part1(monkeys):
    for monkey in monkeys:
        # print("Monkey %s" % monkey.i)

        for i, item in enumerate(monkey.items):
            monkey.inspected += 1

            new = new_val(monkey.op, monkey.items[i])
            relaxed = math.floor(new / 3)

            send_to = monkey.who_to_send_to(relaxed)
            monkeys[send_to].items.append(relaxed)
        monkey.items = []

def new_val(op, curr):
    (op, var1, var2) = op
    val1 = var1(curr)
    val2 = var2(curr)

    return op(val1, val2)


def round_part2(monkeys, divisor):
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):
            monkey.inspected += 1

            current = monkey.items[i]
            new = new_val(monkey.op, current) % divisor
            (send_to_index, true_or_false) = monkey.who_to_send_to(new)
            send_to = monkeys[send_to_index]

            send_to.items.append(new)
        monkey.items = []


def output(monkeys):
    for monkey in monkeys:
        print("Monkey %s, inspected %s, items: %s" % (monkey.i, monkey.inspected, monkey.items))

def part1():
    return None
    print("Start")
    ms = monkeys()
    output(ms)

    for i in range(20):
        print("Round %s" % (i+1))
        round_part1(ms)
        output(ms)

    ordered = sorted(ms, key=lambda x: x.inspected, reverse=True)
    return ordered[0].inspected * ordered[1].inspected


def part2():
    ms = monkeys()
    divisor = 1
    for m in ms:
        divisor *= m.test
    print(divisor)

    # output(ms)
    n = 10_000

    # for i in range(n):
    #     print("Round %s" % (i+1))
    #     round_part2(ms)
    #     output(ms)

    ms = monkeys()
    for i in range(n):
        if i % 100 == 0:
            print("Round %s" % (i+1))
        round_part2(ms, divisor)
        # output(ms)

    ordered = sorted(ms, key=lambda x: x.inspected, reverse=True)
    return ordered[0].inspected * ordered[1].inspected
