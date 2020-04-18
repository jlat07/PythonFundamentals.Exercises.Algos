import search_module as sm
import unittest


class SearchModuleTest(unittest.TestCase):

    def test_binary_search(self):
        test_cases = [
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 6, 6),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 3),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 8),
        ]

        for expected, params in test_cases:
            with self.subTest(f"{params} -> {expected}"):
                actual = sm.binary_search(params[0], params[1])
                self.assertEqual(expected, actual)

    def test_binary_search_random(self):
            test_cases = [
                ([i for i in range(1000)], 221, 221),
                #([i for i in range(1000)], 850, 850),
                #([i for i in range(10000)], 45, 45),
                #([i for i in range(10000)], 45, 45)
            ]

            for expected, params in test_cases:
                with self.subTest(f"{params} -> {expected}"):
                    actual = sm.binary_search(params[0], params[1])
                self.assertEqual(expected, actual)
            
            #print


