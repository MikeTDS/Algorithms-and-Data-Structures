class Node():
    def __init__(self, key, dist, par):
        self.key = key
        self.dist = dist
        self.par = par

class PriorityQueue():
    def __init__(self):
        self.size = 0
        self.q = []

    def parent(self, i):
        return ((i+1)//2)-1

    def insert(self, node):
        self.size += 1
        self.q += [None]
        i = self.size-1
        while i > 0 and self.q[self.parent(i)].dist > node.dist:
            self.q[i] = self.q[self.parent(i)]
            i = self.parent(i)
        self.q[i] = node
    
    def heapify(self, i):
        l = 2*(i+1)-1
        r = 2*(i+1)
        if l < self.size and self.q[l].dist < self.q[i].dist:
            minn = l
        else:
            minn = i
        if r < self.size and self.q[r].dist < self.q[minn].dist:
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
            return
            #print()
        else:
            #print(self.q[0].key)
            temp = self.q[0]
            self.q[0] = self.q[self.size-1]
            self.size -= 1
            self.q = self.q[:-1]
            self.heapify(0)
            return temp

    def priority(self, key, w):
        for i in range(self.size):
            if self.q[i].key == key:
                if self.q[i].dist <= w:
                    continue
                j = i
                self.q[i].dist = w
                while j > 0 and self.q[self.parent(j)].dist > self.q[j].dist:
                    self.q[j],self.q[self.parent(j)] = self.q[self.parent(j)], self.q[j]
                    j = self.parent(j)

    def get(self, key):
        for i in range(self.size):
            if self.q[i].key == key:
                return self.q[i]

    def print(self):
        for x in self.q:
            print('(' + str(x.key) + ', ' + str(x.dist) + ')', end=' ')
        print()
    
    def decrease_key(self, pos, w):
        if w > self.q[pos].dist:
            assert(False)

        self.q[pos].dist = w
        j = pos

        while j > 0 and self.q[self.parent(j)].dist > self.q[j].dist:
            self.q[j],self.q[self.parent(j)] = self.q[self.parent(j)], self.q[j]
            j = self.parent(j)

    
