import search_module as sm
import unittest


class Test_Search_Module(unittest.TestCase):

    def test_search_index(self):
        self.assertEqual(sm.binary_search([i for i in range(10000000)], 7645220), 7645220)
        self.assertEqual(sm.binary_search([i for i in range(20, 10000000)], 7645220), 7645200)
        self.assertEqual(sm.binary_search([0, 1, 2, 3, 4, 5, 7, 8, 9, 10], 2), 2)
        self.assertEqual(sm.binary_search([0, 1, 2, 3, 4, 5, 7, 8, 9, 10], 1), 1)
        self.assertNotEqual(sm.binary_search([0, 1, 2, 3, 4, 5, 7, 8, 9, 10], 2), 1)
        self.assertNotEqual(sm.binary_search([0, 1, 2, 3, 4, 5, 7, 8, 9, 10], 10), 11)


if __name__ == '__main__':
    unittest.main()