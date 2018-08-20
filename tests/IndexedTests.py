import unittest
import indexed
from tests import CONSTANTS

class IndexedTests(unittest.TestCase):

    expected_index = {
        'test_documents/doc2.txt': {
            'one': 1,
            'two': 2,
            'three': 2,
            'four': 3,
            'five': 1
        },
        'test_documents/doc3.txt': {
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
        indexed.preprocess(CONSTANTS.SEARCH_TEST_FILES)
        actual_index = indexed.index
        self.assertDictEqual(actual_index, __class__.expected_index, 'Preprocessor does not produce the expected index!')

    def test_index_lookup(self):
        """
        Verify that the indexed search function properly does a lookup into the index.
        :return: None
        """
        words = ['one', 'two', 'three', 'four', 'five']
        indexed.index = __class__.expected_index  # Make sure we are working with the same index
        for w in words:
            expected_results = [__class__.expected_index[file][w] for file in CONSTANTS.SEARCH_TEST_FILES]

            actual_results = indexed.search(CONSTANTS.SEARCH_TEST_FILES, w)

            self.assertListEqual(actual_results, expected_results)
