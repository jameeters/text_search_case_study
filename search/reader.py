import re


def readfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = sanitize(line)
            yield line


def sanitize(line):
    line = line.lower()
    line = line.strip()
    line = re.sub(r'[.,()\"\-!?/]', '', line)  # remove some punctuation
    return line
