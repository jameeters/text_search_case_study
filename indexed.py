from reader import readfile
index = dict()


def search(filenames, term):
    results = []
    for name in filenames:
        try:
            results.append(index[name][term])
        except KeyError:
            results.append(0)
    return results


def preprocess(filenames):
    for name in filenames:
        index[name] = dict()
        text = readfile(name)
        for line in text:
            for word in line.split(' '):
                try:
                    index[name][word] += 1
                except KeyError:
                    index[name][word] = 0
