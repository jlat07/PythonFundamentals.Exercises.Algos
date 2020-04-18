import search_module as sm
import unittest


class SearchModuleTest(unittest.TestCase):

    def test_binary_search(self):
        test_cases = [
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6, 6),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 3),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 8),
            #([i for i in range(n)], (45), 45)

        ]

        for expected, params in test_cases:
            with self.subTest(f"{params} -> {expected}"):
                actual = sm.binary_search(params[0], params[1])
                self.assertEqual(expected, actual)


