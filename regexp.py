import re
from reader import readfile


def search(filenames, term):
    pattern = re.compile(term)
    results = []
    for name in filenames:
        results.append(0)
        text = readfile(name)
        for line in text:
            # Split to match only words, not substrings of words.
            for word in line.split(' '):
                if re.fullmatch(pattern, word) is not None:
                    results[-1] += 1
    return results
