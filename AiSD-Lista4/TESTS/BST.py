from Stats import Stats, process_key

class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

class BST():
    def __init__(self):
        self.root = None
        self.stats = Stats()
    
    def inorder_tree_walk(self, x):
        order = []
        if x:
            order += self.inorder_tree_walk(x.left)
            order.append(x.key)
            order += self.inorder_tree_walk(x.right)
        return order

    def tree_search(self, x ,k):
        self.stats.compare += 1
        if x is None or k == x.key:
            return x
        self.stats.compare += 1
        if k < x.key:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def tree_minimum(self, x):
        while x.left:
            x = x.left
        return x
    
    def tree_maximum(self, x):
        while x.right:
            x = x.right
        return x
    
    def tree_successor(self, x):
        if x.right:
            return self.tree_minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def tree_insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    
    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
    ########################
    def insert(self, key):
        if key != '':
            key = process_key(key)
            if key != '':
                self.stats.insert += 1
                self.stats.elements += 1
                self.stats.set_max_elements()
                self.tree_insert(Node(key))
    
    def delete(self, key):
        self.stats.delete += 1
        z = self.tree_search(self.root, key)
        if z:
            self.stats.elements -= 1
            self.tree_delete(z)
    
    def find(self, key):
        self.stats.find += 1
        node = self.tree_search(self.root, key)
        if node:
            return 1
        return 0

    def minimal(self):
        self.stats.min += 1
        if self.root:
            return self.tree_minimum(self.root).key
        return ''
    
    def maximal(self):
        self.stats.max += 1
        if self.root:
            return self.tree_maximum(self.root).key
        return ''

    def successor(self, key):
        self.stats.successor += 1
        x = self.tree_search(self.root, key)
        if x:
            suc = self.tree_successor(x)
            if suc:
                return suc.key
            return ''
        return ''

    def inorder(self):
        self.stats.inorder += 1
        return self.inorder_tree_walk(self.root)


        