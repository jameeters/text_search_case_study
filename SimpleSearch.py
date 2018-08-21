from reader import readfile
from SearchMethod import SearchMethod


class SimpleSearch(SearchMethod):

    def search(self, term):
        results = []
        for name in self.target_files:
            results.append(0)
            text = readfile(name)
            for line in text:
                results[-1] += line.split(' ').count(term)
        return results
