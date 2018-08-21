import re
from search.SearchMethod import SearchMethod
from search.reader import readfile


class RegexpSearch(SearchMethod):
    def search(self, term):
        pattern = re.compile(term)
        results = []
        for name in self.target_files:
            results.append(0)
            text = readfile(name)
            for line in text:
                # Split to match only words, not substrings of words.
                for word in line.split(' '):
                    if re.fullmatch(pattern, word) is not None:
                        results[-1] += 1
        return results
