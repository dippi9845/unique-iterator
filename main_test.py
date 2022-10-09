import unittest
from unique_iterator import Unique
from random import randint

class BasicTests(unittest.TestCase):
    
    def test_unicity(self):
        uniques = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duplicated = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        
        for i in Unique(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)
    
    def test_no_duplicate(self):
        uniques = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        duplicated = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in Unique(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)
    
    def test_long_duplicated(self):
        duplicated = [randint(1,6) for i in range(1_000_000)]
        uniques = []
        
        for i in duplicated:
            if not i in uniques:
                uniques.append(i)
        
        self.assertGreater(len(uniques), 0)
        
        for i in Unique(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)



class Pearson:
    def __init__(self, name: str, surname: str, age : int) -> None:
        self.name = name
        self.surname = surname
        self.age = age
    
    def __eq__(self, __o: object) -> bool:
        return __o.name == self.name and __o.surname == self.surname and __o.age == self.age
    
    def __hash__(self) -> int:
        return hash(hash(self.surname) + hash(self.name) + hash(self.age))
    
    def __str__(self) -> str:
        return self.name + " " + self.surname + " " + str(self.age)



class ObjectTests(unittest.TestCase):
    def test_unicity(self):
        uniques = [
            Pearson("Antonio", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 12),
            Pearson("Filippo", "Dippi", 11)]
        
        duplicated = [
            Pearson("Antonio", "Bacillio", 11),
            Pearson("Antonio", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 12),
            Pearson("Federico", "Bacillio", 12),
            Pearson("Filippo", "Dippi", 11),
            Pearson("Filippo", "Dippi", 11)]
        
        for i in Unique(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)
    
    def test_no_duplicate(self):
        uniques = [
            Pearson("Antonio", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 12),
            Pearson("Filippo", "Dippi", 11)]
        
        duplicated = [
            Pearson("Antonio", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 11),
            Pearson("Federico", "Bacillio", 12),
            Pearson("Filippo", "Dippi", 11)]
        
        for i in Unique(duplicated):
            uniques.remove(i)
        
        self.assertListEqual([], uniques)

if __name__ == '__main__':
    unittest.main()