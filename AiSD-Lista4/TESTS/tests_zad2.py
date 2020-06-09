from BST import BST
from RBT import RBT
from HMAP import HMAP
import random
import sys
sys.setrecursionlimit(10**6)


def insert_words(data_structure, file_name):
    iterr = 0
    to_find = []
    mod = random.randint(10,100)
    try:
        with open(file_name, 'r') as file:
            word = ''
            char = file.read(1)
            while char and iterr < 20000:
                if char == ' ' or char == '\n' or char == '\t' or char == '\r':
                    if iterr % mod == 0:
                        dec = random.choice([True,False])
                        if dec and word != '':
                            #print(word)
                            to_find.append(word)
                    iterr += 1
                    data_structure.insert(word)
                    char = file.read(1)
                    word = ''
                    continue
                word += char
                char = file.read(1)
        return to_find
    except:
        sys.stderr.write('Could not open file: ' + file_name + '\n')
        return []

def main():
    bst = BST()
    rbt = RBT()
    hmap = HMAP()

    print('slownik: ')
    #BST
    to_find = insert_words(bst, './slownik.txt')
    if len(to_find) > 100:
        to_find = to_find[:100]
    #print(len(to_find))
    compares = []
    prev = 0
    for f in to_find:
        bst.find(f)
        compares.append(bst.stats.compare-prev)
        prev = bst.stats.compare
    print('BST min:' + str(min(compares)))
    print('BST avg:' + str(sum(compares)/len(compares)))
    print('BST max:' + str(max(compares)))

    #RBT
    insert_words(rbt, './slownik.txt')
    compares = []
    prev = 0
    for f in to_find:
        rbt.find(f)
        compares.append(rbt.stats.compare-prev)
        prev = rbt.stats.compare
    print('RBT min:' + str(min(compares)))
    print('RBT avg:' + str(sum(compares)/len(compares)))
    print('RBT max:' + str(max(compares)))

    #HMAP
    insert_words(hmap, './slownik.txt')
    compares = []
    prev = 0
    for f in to_find:
        hmap.find(f)
        compares.append(hmap.stats.compare-prev)
        prev = hmap.stats.compare
    print('HMAP min:' + str(min(compares)))
    print('HMAP avg:' + str(sum(compares)/len(compares)))
    print('HMAP max:' + str(max(compares)))

    bst = BST()
    rbt = RBT()
    hmap = HMAP()

    print('hobbit: ')
    #BST
    to_find = insert_words(bst, './txt1')
    if len(to_find) > 100:
        to_find = to_find[:100]
    #print(len(to_find))
    compares = []
    prev = 0
    for f in to_find:
        bst.find(f)
        #print(bst.stats.compare-prev)
        compares.append(bst.stats.compare-prev)
        prev = bst.stats.compare
    print('BST min:' + str(min(compares)))
    print('BST avg:' + str(sum(compares)/len(compares)))
    print('BST max:' + str(max(compares)))

    #RBT
    insert_words(rbt, './txt1')
    compares = []
    prev = 0
    for f in to_find:
        rbt.find(f)
        compares.append(rbt.stats.compare-prev)
        prev = rbt.stats.compare
    print('RBT min:' + str(min(compares)))
    print('RBT avg:' + str(sum(compares)/len(compares)))
    print('RBT max:' + str(max(compares)))

    #HMAP
    insert_words(hmap, './txt1')
    compares = []
    prev = 0
    for f in to_find:
        hmap.find(f)
        compares.append(hmap.stats.compare-prev)
        prev = hmap.stats.compare
    print('HMAP min:' + str(min(compares)))
    print('HMAP avg:' + str(sum(compares)/len(compares)))
    print('HMAP max:' + str(max(compares)))
    

if __name__ == "__main__":
    main()