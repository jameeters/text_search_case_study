import simple
import regexp
import indexed

target_filenames = [
    'sample_files/french_armed_forces.txt',
    'sample_files/hitchhikers.txt',
    'sample_files/warp_drive.txt',
]


def main():
    print('Preprocessing files for indexed search.')
    indexed.preprocess(target_filenames)
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
        simple.search(target_filenames, term)
    elif method == 2:
        regexp.search(target_filenames, term)
        pass
    elif method == 3:
        indexed.search(target_filenames, term)
        pass


while True:
    main()
    print('-' * 30)



