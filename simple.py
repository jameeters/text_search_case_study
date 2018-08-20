from reader import readfile


def search(filenames, term):
    results = []
    for name in filenames:
        results.append(0)
        text = readfile(name)
        for line in text:
            results[-1] += line.split(' ').count(term)
    return results
