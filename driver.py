import timeit
from search.RegexpSearch import RegexpSearch
from search.SimpleSearch import SimpleSearch
from search.IndexedSearch import IndexedSearch
from search import CONSTANTS


def interactive():
    print('Preprocessing files for indexed search.')
    start = timeit.default_timer()
    indexed_searcher = IndexedSearch()
    indexed_searcher.set_target_files(CONSTANTS.target_filenames)
    indexed_searcher.preprocess()
    elapsed = (timeit.default_timer() - start) * 1000
    print('Done. {} ms elapsed'. format(elapsed))

    term = input('Enter a search term: ').lower().strip(' ')
    assert len(term) > 0

    method = int(input('''
        Select method:
        1. Simple string matching
        2. Regular expression search
        3. Indexed search
    > '''))
    assert 1 <= method <= 3

    start = timeit.default_timer()
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

    elapsed = (timeit.default_timer() - start) * 1000
    for r in results:
        print(r)
    print('{} ms elapsed'.format(elapsed))

if __name__ == '__main__':
    while True:
        interactive()
        print('-' * 30)
