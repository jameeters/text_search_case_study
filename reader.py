import re


def readfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.lower()
            line = re.sub(r'[\.,\(\)\"-]', '', line) # remove some punctuation
            yield line
