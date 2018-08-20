import unittest
import simple
from tests import CONSTANTS


class SimpleTests(unittest.TestCase):

    def test_results(self):
        """
        Verify that the simple search produces the correct results
        :return:
        """
        term = 'one'
        expected_results = [1, 3]
        actual_results = simple.search(CONSTANTS.SEARCH_TEST_FILES, term)
        self.assertListEqual(actual_results, expected_results, 'Simple search does not produce expected results!')
