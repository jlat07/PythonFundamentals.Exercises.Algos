import search_module as sm
import unittest


class SearchModuleTest(unittest.TestCase):

    def test_number_value(self):
        self.assertEqual(sm.binary_search([0, 1, 2, 3, 12, 5, 6, 7, 8, 9, 10, 11], 12), 4)
        self.assertEqual(sm.binary_search([3,6,7,1,5,8,9,11,12,15,13,14,16,17,19,2,4,10,18,20], 5), 3)

        self.assertNotEqual(sm.binary_search([2, 3, 4, 6, 7, 9, 12, 14, 15, 16], 9), 9)
        self.assertNotEqual(sm.binary_search([2, 3, 4, 6, 7, 9, 12, 14, 15, 16], 9), -1)





test_list = [i for i in range(10000000)]
n = 1919
sm.binary_search(test_list, n)
sm.find(test_list, n)

sm.binary_search(test_list, 999)
sm.find(test_list, 999)