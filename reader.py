def readfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.lower()
