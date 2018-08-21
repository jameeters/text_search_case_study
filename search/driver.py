import RegexpSearch
import SimpleSearch

from search import IndexedSearch

target_filenames = [
    'sample_documents/french_armed_forces.txt',
    'sample_documents/hitchhikers.txt',
    'sample_documents/warp_drive.txt'
]


def main():
    print('Preprocessing files for indexed search.')
    IndexedSearch.preprocess(target_filenames)
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
        SimpleSearch.search(target_filenames, term)
    elif method == 2:
        RegexpSearch.search(target_filenames, term)
        pass
    elif method == 3:
        IndexedSearch.search(target_filenames, term)
        pass


while True:
    main()
    print('-' * 30)



