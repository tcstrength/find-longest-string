from MapReduce import MRLongestStrFinder
from MapReduce import mapper
import time

def execute(func):
    start_time = time.time()
    func()
    print("Execution time: {}".format(time.time() - start_time))

def normal():
    input = ['cuong', 'dep', 'trai', 'vo', 'cung'] * 1000000
    print("Without MapReduce")
    print(mapper(input))

def mapreduce():
    input = ['cuong', 'dep', 'trai', 'vo', 'cung'] * 1000000
    print("With MapReduce")
    finder = MRLongestStrFinder()
    print(finder(input))

execute(mapreduce)
execute(normal)