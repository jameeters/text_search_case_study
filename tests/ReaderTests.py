import unittest
import reader


class ReaderTests(unittest.TestCase):

    def test_reading(self):
        """
        Verify that the reader reads the file line by line.
        (Basically that it works at all)
        :return:
        """

        test_filename = 'test_documents/doc1.txt'

        expected_lines = ['line one', 'line two', 'line three']

        actual_lines = []
        for line in reader.readfile(test_filename):
            actual_lines.append(line)

        self.assertListEqual(actual_lines, expected_lines, 'Reader has not produced the expected lines!')

    def test_sanitization(self):
        """
        Verify that sanitize() strips out upper case and the appropriate punctuation marks.
        :return:
        """
        raw_line = 'THIS LINE has (some, crazy.) "weird" punc-tuation AND USE OF UPPER CASE. WE don\'t want THat!?'
        sanitary_line = 'this line has some crazy weird punctuation and use of upper case we don\'t want that'

        processed_line = reader.sanitize(raw_line)
        self.assertEqual(processed_line, sanitary_line, 'sanitize() method does not produce the expected string!')
