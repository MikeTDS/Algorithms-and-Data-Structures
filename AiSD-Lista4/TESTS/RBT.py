from Stats import Stats, process_key

class Node():
    def __init__(self, key):
        self.key = key
        self.right = self
        self.left = self
        self.parent = self
        self.color = 'r'

class RBT():
    def __init__(self):
        self.nil = Node(None)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.nil.color = 'b'
        self.root = self.nil
        self.stats = Stats()
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def insertt(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z 
        else:
            y.right = z 
        z.left = self.nil
        z.right = self.nil
        z.color = 'r'
        self.insert_fixup(z)
    
    def insert_fixup(self, z):
        while z.parent.color == 'r':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'r':
                    z.parent.color = 'b'
                    y.color = 'b'
                    z.parent.parent.color = 'r'
                    z = z.parent.parent
                else: 
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'b'
                    z.parent.parent.color = 'r'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'r':
                    z.parent.color = 'b'
                    y.color = 'b'
                    z.parent.parent.color = 'r'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'b'
                    z.parent.parent.color = 'r'
                    self.left_rotate(z.parent.parent)

        self.root.parent = self.nil
        self.root.color = 'b'

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x
    
    def tree_maximium(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def deletee(self, node):
        if node.left == self.nil or node.right == self.nil:
            n = node
        else:
            n = self.successorr(node)
        

        if n.left != self.nil:
            m = n.left
        else:
            m = n.right
        

        m.parent = n.parent

        if (n.parent == self.nil):
            self.root = m
        elif (n == n.parent.left):
            n.parent.left = m
        else:
            n.parent.right = m
        
        if (n != node):
            node.key = n.key
        
        if (n.color == 'b'):
            self.delete_fixup(m)

    def delete_fixup(self, node):
        while (node != self.root and node.color == 'b'):
            if (node == node.parent.left):
                m = node.parent.right

                if (m.color == 'r'):
                    m.color = 'b'
                    node.parent.color = 'r'
                    self.left_rotate (node.parent)
                    m = node.parent.right
            

                if (m.left.color == 'b' and m.right.color == 'b'):
                    m.color = 'r' #Case 2: node's sibling m is 'b',  and both of m's children are 'b'
                    node = node.parent
                else: 
                    if (m.right.color == 'b'):
                        m.left.color = 'b' #Case 3: node's sibling m is 'b', m's left child is 'r', and m's right child is 'b'
                        m.color = 'r'
                        self.right_rotate(m)
                        m = node.parent.right
                
                    m.color = node.parent.color #node's sibling m is 'b', and m's right child is 'r'
                    node.parent.color = 'b'
                    m.right.color = 'b'
                    self.left_rotate (node.parent)
                    node = self.root
            
            else:
                m = node.parent.left

                if (m.color == 'r'):
                    m.color = 'b'
                    node.parent.color = 'r'
                    self.right_rotate(node.parent)
                    m = node.parent.left
                

                if (m.right.color == 'b' and m.left.color == 'b'):
                    m.color = 'r'
                    node = node.parent
                else:
                    if (m.left.color == 'b'):
                        m.right.color = 'b'
                        m.color = 'r'
                        self.left_rotate (m)
                        m = node.parent.left
                    

                    m.color = node.parent.color
                    node.parent.color = 'b'
                    m.left.color = 'b'
                    self.right_rotate (node.parent)
                    node = self.root
    
        node.color = 'b'



    def successorr (self, node):
        if (node.right != self.nil):
            return self.tree_minimum(node.right)

        tmp = node.parent
        while (tmp != self.nil and node == tmp.right):
            node = tmp
            tmp = tmp.parent

        return tmp

    def select(self, node, key):
        self.stats.compare += 1
        if node.key == key or node == self.nil:
            return node
        self.stats.compare += 1
        if node.key < key:
            return self.select(node.right, key)
        return self.select(node.left, key)

    def inorderr(self, node):
        order = []
        if node != self.nil:
            order += self.inorderr(node.left)
            order.append(node.key)
            order += self.inorderr(node.right)
        return order
########################   
    def insert(self, key):
        if key != '':
            key = process_key(key)
            if key != '':
                self.stats.insert += 1
                self.stats.elements += 1
                self.stats.set_max_elements()
                node = Node(key)
                node.parent = self.nil
                node.left = self.nil
                node.right = self.nil
                self.insertt(node)

    def delete(self, key):
        self.stats.delete += 1
        node = self.select(self.root, key)
        if node != self.nil:
            self.stats.elements -= 1
            return self.deletee(node)

    def find(self, key):
        self.stats.find += 1
        node = self.select(self.root, key)
        if node != self.nil:
            return 1
        return 0

    def minimal(self):
        self.stats.min += 1
        if self.root != self.nil:
            return self.tree_minimum(self.root).key
        return ''
    
    def maximal(self):
        self.stats.max += 1
        if self.root != self.nil:
            return self.tree_maximium(self.root).key
        return ''

    def successor(self, key):
        self.stats.successor += 1
        node = self.select(self.root, key)
        if node != self.nil:
            succ = self.successorr(node)
            if succ != self.nil:
                return succ.key
        return ''        

    def inorder(self):
        self.stats.inorder += 1
        return self.inorderr(self.root)

