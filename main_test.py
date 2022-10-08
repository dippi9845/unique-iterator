import unittest
from unique_iterator import UniqueIterator

class BasicTests(unittest.TestCase):
    
    def test_unicity(self):
        uniques = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duplicated = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        
        for i in UniqueIterator(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)
    
    def test_no_duplicate(self):
        uniques = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duplicated = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in UniqueIterator(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)
        



if __name__ == '__main__':
    unittest.main()