from search.RegexpSearch import RegexpSearch
from search.SimpleSearch import SimpleSearch
from search.IndexedSearch import IndexedSearch
from search import CONSTANTS
from pprint import pprint

def interactive():
    print('Preprocessing files for indexed search.')
    indexed_searcher = IndexedSearch()
    indexed_searcher.set_target_files(CONSTANTS.target_filenames)
    indexed_searcher.preprocess()
    print('Done.')

    term = input('Enter a search term: ').lower().strip(' ')
    assert len(term) > 0

    method = int(input('''
        Select method:
        1. Simple string matching
        2. Regular expression search
        3. Indexed search
    > '''))
    assert 1 <= method <= 3

    if method == 1:
        # simple string matching
        simple_searcher = SimpleSearch()
        simple_searcher.set_target_files(CONSTANTS.target_filenames)
        results = simple_searcher.search(term)
        results = simple_searcher.prettyfy_results(results)
    elif method == 2:
        regexp_searcher = RegexpSearch()
        regexp_searcher.set_target_files(CONSTANTS.target_filenames)
        results = regexp_searcher.search(term)
        results = regexp_searcher.prettyfy_results(results)
    elif method == 3:
        results = indexed_searcher.search(term)
        results = indexed_searcher.prettyfy_results(results)

    for r in results:
        print(r)


if __name__ == '__main__':
    while True:
        interactive()
        print('-' * 30)



