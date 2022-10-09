from time import time
from ..unique_iterator.unique_iterator import Unique
import numpy as np
from collections import Counter
from random import randint

def unique1(list1):
    '''
    code taken from https://www.geeksforgeeks.org/python-get-unique-values-list/
    '''
    rtr = ""
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        rtr += x + " "
    
    return rtr

def unique2(list1):
    '''
    code taken from https://www.geeksforgeeks.org/python-get-unique-values-list/
    '''
    rtr = ""
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        rtr += x + " "
    
    return rtr

def unique3(list1):
    '''
    code taken from https://www.geeksforgeeks.org/python-get-unique-values-list/
    '''
    x = np.array(list1)
    return " ".join(np.unique(x))

def unique4(list1):
    '''
    code taken from https://www.geeksforgeeks.org/python-get-unique-values-list/
    '''
    return str(*Counter(list1))

def my_unique(list1):
    return " ".join(Unique(list1))

def test_list(list1):
    s = time()
    
    unique1(list1)
    
    print("unique1 took", time() - s)
    
    s = time()
    
    unique2(list1)
    
    print("unique2 took", time() - s)
    
    s = time()
    
    unique3(list1)
    
    print("unique3 took", time() - s)
    
    s = time()
    
    unique4(list1)
    
    print("unique4 took", time() - s)
    
    s = time()
    
    my_unique(list1)
    
    print("unique5 took", time() - s)

if __name__ == "__main__":
    a = [randint(1,10) for i in range(1_000)]
    
    test_list(a)
    
    a = [randint(1,10) for i in range(10_000)]
    
    test_list(a)
    
    a = [randint(1,10) for i in range(100_000)]
    
    test_list(a)
    
    a = [randint(1,10) for i in range(1_000_000)]
    
    test_list(a)
    
    # -------------------------------------------------
    
    a = [randint(1,100) for i in range(1_000)]
    
    test_list(a)
    
    a = [randint(1,100) for i in range(10_000)]
    
    test_list(a)
    
    a = [randint(1,100) for i in range(100_000)]
    
    test_list(a)
    
    a = [randint(1,100) for i in range(1_000_000)]
    
    test_list(a)
    
    # -------------------------------------------------
    
    a = [randint(1,1000) for i in range(1_000)]
    
    test_list(a)
    
    a = [randint(1,1000) for i in range(10_000)]
    
    test_list(a)
    
    a = [randint(1,1000) for i in range(100_000)]
    
    test_list(a)
    
    a = [randint(1,1000) for i in range(1_000_000)]
    
    test_list(a)
    