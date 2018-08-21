import unittest
from search.RegexpSearch import RegexpSearch
from tests import CONSTANTS


class RegexpTests(unittest.TestCase):
    def setUp(self):
        self.regexp_searcher = RegexpSearch()
        self.regexp_searcher.set_target_files(CONSTANTS.SEARCH_TEST_FILES)

    def test_results(self):
        """
        Verify that the regexp search works with a normal word as the term.
        :return: None
        """
        term = 'one'
        expected_results = [1, 3]
        actual_results = self.regexp_searcher.search(term)
        self.assertListEqual(actual_results, expected_results,
                             'Regexp search with simple term does not produce expected results!')

    def test_results_with_regular_expression_term(self):
        """
        Verify that the regexp search can accept a regular expression as its search term.
        :return: None
        """
        term = 'one|three'
        expected_results = [3, 4]
        actual_results = self.regexp_searcher.search(term)
        self.assertListEqual(actual_results, expected_results,
                             'Regexp search with regexp term does not produce expected results!')


if __name__ == '__main__':
    unittest.main()
