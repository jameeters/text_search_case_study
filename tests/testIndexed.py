import unittest
from search.IndexedSearch import IndexedSearch
from tests import CONSTANTS


class IndexedTests(unittest.TestCase):
    def setUp(self):
        self.indexed_searcher = IndexedSearch()
        self.indexed_searcher.set_target_files(CONSTANTS.SEARCH_TEST_FILES)

        self.expected_index = {
            'tests/test_documents/doc2.txt': {
                'one': 1,
                'two': 2,
                'three': 2,
                'four': 3,
                'five': 1
            },
            'tests/test_documents/doc3.txt': {
                'one': 3,
                'two': 2,
                'three': 1,
                'four': 2,
                'five': 3
            },
        }

    def test_index_creation(self):
        """
        Verify that the preprocessor method creates the index correctly
        :return: None
        """
        self.indexed_searcher.preprocess()
        actual_index = self.indexed_searcher.index
        self.assertDictEqual(actual_index, self.expected_index, 'Preprocessor does not produce the expected index!')

    def test_index_lookup(self):
        """
        Verify that the indexed search function properly does a lookup into the index.
        :return: None
        """
        words = ['one', 'two', 'three', 'four', 'five']
        self.indexed_searcher.index = self.expected_index  # Make sure we are working with the same index
        for w in words:
            expected_results = [self.expected_index[file][w] for file in CONSTANTS.SEARCH_TEST_FILES]

            actual_results = self.indexed_searcher.search(w)

            self.assertListEqual(actual_results, expected_results)

if __name__ == '__main__':
    unittest.main()
