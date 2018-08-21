import unittest
from SimpleSearch import SimpleSearch
from tests import CONSTANTS


class SimpleTests(unittest.TestCase):

    def setUp(self):
        self.simple_searcher = SimpleSearch()
        self.simple_searcher.set_target_files(CONSTANTS.SEARCH_TEST_FILES)

    def test_results(self):
        """
        Verify that the simple search produces the correct results
        :return:
        """
        term = 'one'
        expected_results = [1, 3]
        actual_results = self.simple_searcher.search(term)
        self.assertListEqual(actual_results, expected_results, 'Simple search does not produce expected results!')
