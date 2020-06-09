from RBT import RBT
from hashlib import md5
from Stats import Stats, process_key

class ListNode():
    def __init__(self, key):
        self.key = key
        self.next = None

def insert(hmap,key):
    j = md5(key.encode()).hexdigest() 
    j = int(j,16)
    j = j % hmap.m
    if hmap.size_table[j] < hmap.nt-1:
        insert_list(hmap,j,key)
    elif hmap.size_table[j] == hmap.nt-1:
        list_to_tree(hmap,j)
        insert_tree(hmap,j,key)
    else:
        insert_tree(hmap,j,key)

def insert_list(hmap,j,key):
    node = ListNode(key)
    current = hmap.hash_table[j]
    if current is None:
        hmap.hash_table[j] = node
        hmap.size_table[j] += 1
        return node
    while current.next:
        current = current.next
    current.next = node
    hmap.size_table[j] += 1
    return node

def insert_tree(hmap,j,key):
    hmap.size_table[j] += 1
    return hmap.hash_table[j].insert(key)

def list_to_tree(hmap,j):
    temp = []
    current = hmap.hash_table[j]
    if current:
        temp.append(current.key)
        while current.next:
            current = current.next
            temp.append(current.key)
    rbt = RBT()
    hmap.hash_table[j] = rbt
    for v in temp:
        rbt.insert(v)
    return rbt

def tree_to_list(hmap,j):
    elements = hmap.hash_table[j].inorder()
    hmap.stats.compare += hmap.hash_table[j].stats.compare
    hmap.hash_table[j] = None
    hmap.size_table[j] = 0
    for el in elements:
        insert_list(hmap,j,el)

def find(hmap,key):
    j = md5(key.encode()).hexdigest() 
    j = int(j,16)
    j = j % hmap.m
    if hmap.size_table[j] < hmap.nt:
        return find_in_list(hmap,j,key)
    else:
        return find_in_tree(hmap,j,key)

def find_in_list(hmap,j,key):
    current = hmap.hash_table[j]
    if current:
        hmap.stats.compare += 1
        if current.key == key:
            return 1
        while current.next:
            current = current.next
            hmap.stats.compare += 1
            if current.key == key:
                return 1
    return 0

def find_in_tree(hmap,j,key):
    return hmap.hash_table[j].find(key)

def select(hmap, key):
    j = md5(key.encode()).hexdigest() 
    j = int(j,16)
    j = j % hmap.m
    if hmap.size_table[j] < hmap.nt:
        return select_from_list(hmap,j,key)
    else:
        return select_from_tree(hmap,j,key)

def select_from_list(hmap,j,key):
    current = hmap.hash_table[j]
    if current:
        if current.key == key:
            return current, j
        while current.next:
            current = current.next
            if current.key == key:
                return current, j
    return None, j

def select_from_tree(hmap,j,key):
    node = hmap.hash_table[j].select(hmap.hash_table[j].root, key)
    if node == hmap.hash_table[j].nil:
        return None, j
    return node, j

def delete(hmap, key):
    node, j = select(hmap, key)
    if node:
        hmap.stats.elements -= 1
        if hmap.size_table[j] < hmap.nt:
            current = hmap.hash_table[j]
            if current == node:
                if current.next:
                    hmap.hash_table[j] = current.next
                    current = None
                else:
                    hmap.hash_table[j] = None
                hmap.size_table[j] -= 1
                return
            while current.next != node:
                current = current.next
            temp = current.next
            current.next = current.next.next
            temp = None
            hmap.size_table[j] -= 1
        else:
            hmap.hash_table[j].delete(key)
            hmap.size_table[j] -= 1
            if hmap.size_table[j] < hmap.nt:
                tree_to_list(hmap, j)
        

class HMAP():
    def __init__(self):
        self.m = 1024
        self.nt = 50
        self.hash_table = [None for i in range (self.m)]
        self.size_table = [0 for i in range(self.m)]
        self.stats = Stats()

    def insert(self,key):
        if key != '':
            key = process_key(key)
            if key != '':
                self.stats.insert += 1
                self.stats.elements += 1
                self.stats.set_max_elements()
                return insert(self, key)
    
    def find(self, key):
        self.stats.find += 1
        return find(self, key)
    
    def print_hash_table(self):
        for i in range(len(self.size_table)):
            if self.hash_table[i]:
                print(str(i) + ': ', end = ' ')
                if self.size_table[i] < self.nt:
                    current = self.hash_table[i]
                    if current:
                        print(current.key, end=' ')
                        while current.next:
                            current = current.next
                            print(current.key, end=' ')
                    print()
                else:
                    print(self.hash_table[i].inorder())

    def delete(self, key):
        self.stats.delete += 1
        return delete(self, key)

    def minimal(self):
        self.stats.min += 1
        return ''
    
    def maximal(self):
        self.stats.max += 1
        return ''
    
    def successor(self, key):
        self.stats.successor += 1
        return ''
    
    def inorder(self):
        self.stats.inorder += 1
        return ''
    