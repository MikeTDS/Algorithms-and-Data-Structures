class Node():
    def __init__(self, key, p):
        self.key = key
        self.p = p

class PriorityQueue():
    def __init__(self):
        self.size = 0
        self.q = []

    def parent(self, i):
        return ((i+1)//2)-1

    def insert(self, key, p):
        node = Node(key, p)
        self.size += 1
        self.q += [None]
        i = self.size-1
        while i > 0 and self.q[self.parent(i)].p > node.p:
            self.q[i] = self.q[self.parent(i)]
            i = self.parent(i)
        self.q[i] = node
    
    def heapify(self, i):
        l = 2*(i+1)-1
        r = 2*(i+1)
        if l < self.size and self.q[l].p < self.q[i].p:
            minn = l
        else:
            minn = i
        if r < self.size and self.q[r].p < self.q[minn].p:
            minn = r
        if minn != i:
            self.q[i], self.q[minn] = self.q[minn], self.q[i]
            self.heapify(minn)
    
    def empty(self):
        if self.size == 0:
            print('1')
        else:
            print('0')
    
    def top(self):
        if self.size > 0:
            print(self.q[0].key)
        else:
            print()

    def pop(self):
        if self.size == 0:
            print()
        else:
            print(self.q[0].key)
            self.q[0] = self.q[self.size-1]
            self.size -= 1
            self.q = self.q[:-1]
            self.heapify(0)

    def priority(self, key, p):
        for i in range(self.size):
            if self.q[i].key == key:
                if self.q[i].p <= p:
                    continue
                j = i
                self.q[i].p = p
                while j > 0 and self.q[self.parent(j)].p > self.q[j].p:
                    self.q[j],self.q[self.parent(j)] = self.q[self.parent(j)], self.q[j]
                    j = self.parent(j)

    def print(self):
        for x in self.q:
            print('(' + str(x.key) + ', ' + str(x.p) + ')', end=' ')
        print()

    
