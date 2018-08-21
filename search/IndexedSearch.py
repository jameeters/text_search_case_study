from search.SearchMethod import SearchMethod

from search.reader import readfile


class IndexedSearch(SearchMethod):
    def __init__(self):
        super().__init__()
        self.index = None

    def search(self, term):
        if self.index is None:
            self.preprocess()

        results = []
        for name in self.target_files:
            try:
                results.append(self.index[name][term])
            except KeyError:
                results.append(0)
        return results

    def preprocess(self):
        self.index = dict()
        for name in self.target_files:
            self.index[name] = dict()
            text = readfile(name)
            for line in text:
                for word in line.split(' '):
                    try:
                        self.index[name][word] += 1
                    except KeyError:
                        self.index[name][word] = 1

    def set_target_files(self, filenames):
        super().set_target_files(filenames)
        self.preprocess()
