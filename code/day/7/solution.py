from utils import stream_file

class Node(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []

    def __str__(self):
        return "%s [%s] (%s)" % (self.name, self.size, ", ".join(map(str, self.children)))

def lines():
    return stream_file("data/day/7/input.txt")

def parse():
    root = Node("/", 0)
    path = [root]
    for i, line in enumerate(lines()):
        if i == 0:
            continue

        if line.startswith("$ cd "):
            name = line.replace("$ cd ", "")
            if name == "..":
                path.pop()
            else:
                child = list(filter(lambda c: c.name == name, path[-1].children))[0]
                path.append(child)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            name = line.replace("dir ", "")
            child = Node(name, 0)
            path[-1].children.append(child)
        else:
            [size, name] = line.split(" ")
            child = Node(name, int(size))
            path[-1].children.append(child)
    return root

def visit(node):
    small_dirs = []
    for child in node.children:
        visit(child)
        node.size += child.size

def flatten(node):
    flat = []
    if len(node.children) > 0:
        flat.append(node)
    for child in node.children:
        flat.extend(flatten(child))
    return flat

def part1():
    root = parse()
    visit(root)
    dirs = flatten(root)
    small_dirs = filter(lambda d: d.size <= 100000, dirs)
    return sum(map(lambda d: d.size, small_dirs))

def part2():
    root = parse()
    visit(root)
    dirs = flatten(root)
    sizes = map(lambda d: d.size, dirs)

    free_space = 70000000 - root.size
    need_to_free = 30000000 - free_space

    sorted_sizes = sorted(sizes)
    return next(x for x in sorted_sizes if x >= need_to_free)

