import unittest
import indexed
from tests import CONSTANTS

class IndexedTests(unittest.TestCase):

    def test_index_creation(self):
        expected_index = {
            'test_documents/doc2.txt': {
                'one': 1,
                'two': 2,
                'three': 2,
                'four': 3,
                'five': 1
            },
            'test_documents/doc3.txt':{
                'one': 3,
                'two': 2,
                'three': 1,
                'four': 2,
                'five': 3
            },
        }
        indexed.preprocess(CONSTANTS.SEARCH_TEST_FILES)
        actual_index = indexed.index
        self.assertDictEqual(actual_index, expected_index, 'Preprocessor does not produce the expected index!')
