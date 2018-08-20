import re
from reader import readfile


def search(filenames, term):
    pattern = re.compile(term)
    results = []
    for name in filenames:
        results.append(0)
        text = readfile(name)
        for line in text:
            results[-1] += len(re.findall(pattern, line))
    print(results)
