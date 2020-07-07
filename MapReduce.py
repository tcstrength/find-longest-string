from multiprocessing import Pool
from multiprocessing import cpu_count
from itertools import islice

def mapper(input):
    maxl = 0
    maxs = None
    for word in input:
        lenw = len(word)
        if (lenw > maxl):
            maxl = lenw
            maxs = word
    return maxs

class MRLongestStrFinder:

    def __init__(self, num_workers = None):
        self.pool = Pool(num_workers)

    def chunkify(self, input):
        num_workers = 8
        chunksize=int(len(input) / num_workers)
        it = iter(input)
        return iter(lambda: tuple(islice(it, chunksize)), ())

    def __call__(self, input):
        chunks = self.chunkify(input)
        mapped = self.pool.map(mapper, chunks, 1)
        print(mapped)
        return mapper(mapped)
        