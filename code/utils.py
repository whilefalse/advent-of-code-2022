def load_file(path):
    with open(path, 'r') as f:
        return list(filter(lambda x: x != "", map(lambda x: x.rstrip(), f.readlines())))

def stream_file(path):
     with open(path, 'r') as f:
        for line in f:
            line = line.rstrip()
            yield line

def stream_file_characters(path):
     with open(path, 'r') as f:
        char = f.read(1)
        while char and char != "\n":
            yield char
            char = f.read(1)
