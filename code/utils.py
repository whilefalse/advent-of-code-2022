def stream_file(path):
     with open(path, 'r') as f:
        for line in f:
            line = line.rstrip()
            yield line
