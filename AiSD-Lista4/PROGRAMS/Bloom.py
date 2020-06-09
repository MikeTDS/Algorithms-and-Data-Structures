from numpy.random import RandomState
from Stats import Stats, process_key
from hashlib import md5

class Bloom():
    def __init__(self):
        self.m = 1024
        self.k = 10
        self.stats = Stats()
        self.filter = [0 for i in range(self.m)]
    def hashes(self,key):
        ids = []
        if key != '':
            h = md5(key.encode()).hexdigest() 
            h = int(h,16)%(2**32-1)
            rs = RandomState(h)
            for _ in range(self.k):
                ids.append(int((rs.random()*(10**6))%self.m))
        return ids
        
    def insert(self, key):
        self.stats.insert += 1
        if key != '':
            key = process_key(key)
            self.stats.elements += 1
            ids = self.hashes(key)
            for i in ids:
                if self.filter[i] == 0:
                    self.stats.max_elements += 1
                self.filter[i] = 1
    
    def find(self, key):
        self.stats.find += 1
        ids = self.hashes(key)
        for i in ids:
            if self.filter[i] == 0:
                return 0
        return 1
    
    def delete(self, key):
        self.stats.delete += 1

    def minimal(self):
        self.stats.min += 1
        return ''
    
    def maximal(self):
        self.stats.max += 1
        return ''
    
    def inorder(self):
        self.stats.inorder += 1
        return []

    def successor(self, key):
        self.stats.successor += 1
        return ''



