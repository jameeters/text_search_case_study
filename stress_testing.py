import timeit
import csv
import random
from search.SimpleSearch import SimpleSearch
from search.RegexpSearch import RegexpSearch
from search.IndexedSearch import IndexedSearch

# Files to write data to
data_files = {
    'simple': 'data_files/simple.csv',
    'regexp': 'data_files/regexp.csv',
    'indexed': 'data_files/indexed.csv',
    'setup': 'data_files/setup.csv'
}
# prep the setup times file
setup_file = open(data_files['setup'], 'w')
setup_writer = csv.writer(setup_file)
setup_writer.writerow(['method', 'setup_time'])

# Target files
target_files = [
    '../sample_documents/french_armed_forces.txt',
    '../sample_documents/hitchhikers.txt',
    '../sample_documents/warp_drive.txt',
]


# read in the search terms
with open('data_files/words.txt', 'r') as f:
    words = f.readlines()
    while len(words) < 2E6:
        words.append(words[random.randint(0, len(words) - 1)])

print('Done Making words list')


def do_searches(csvwriter, searcher):
    for w in words:
        start = timeit.default_timer()
        searcher.search(w)
        elapsed = (timeit.default_timer() - start) * 1000
        csvwriter.writerow([elapsed])


# Test the simple search
start = timeit.default_timer()
simple_searcher = SimpleSearch()
simple_searcher.set_target_files(target_files)
elapsed = (timeit.default_timer() - start) * 1000
setup_writer.writerow(['simple', elapsed])

with open(data_files['simple'], 'w') as f:
    simple_writer = csv.writer(f)
    simple_writer.writerow(['time'])
    do_searches(simple_writer, simple_searcher)

print('Simple done.')

# Test the regexp search
start = timeit.default_timer()
regexp_searcher = RegexpSearch()
regexp_searcher.set_target_files(target_files)
elapsed = (timeit.default_timer() - start) * 1000
setup_writer.writerow(['regexp', elapsed])

with open(data_files['regexp'], 'w') as f:
    regexp_writer = csv.writer(f)
    regexp_writer.writerow(['time'])
    do_searches(regexp_writer, regexp_searcher)

print('Regexp done.')

# test the indexed search
start = timeit.default_timer()
indexed_searcher = IndexedSearch()
indexed_searcher.set_target_files(target_files)
indexed_searcher.preprocess()
elapsed = (timeit.default_timer() - start) * 1000
setup_writer.writerow(['indexed', elapsed])

with open(data_files['indexed'], 'w') as f:
    indexed_writer = csv.writer(f)
    indexed_writer.writerow(['time'])
    do_searches(indexed_writer, indexed_searcher)

print('Indexed done.')
