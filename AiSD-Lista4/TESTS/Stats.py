class Stats():
    def __init__(self):
        self.insert = 0
        self.load = 0
        self.delete = 0
        self.find = 0
        self.min = 0
        self.max = 0
        self.successor = 0
        self.inorder = 0
        self.compare = 0
        self.elements = 0
        self.max_elements = 0
    
    def set_max_elements(self):
        if self.elements > self.max_elements:
            self.max_elements = self.elements

def process_key(w):
    if not ((64 < ord(w[0]) < 91) or (96 < ord(w[0]) < 123)):
        w = w[1:]
    if w != '':
        if not ((64 < ord(w[-1]) < 91) or (96 < ord(w[-1]) < 123)):
            w = w[:-1]
    return w