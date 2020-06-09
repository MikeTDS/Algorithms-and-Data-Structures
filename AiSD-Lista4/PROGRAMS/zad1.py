from BST import BST
from RBT import RBT
from HMAP import HMAP
from Bloom import Bloom
import sys
import time

loads = 0

def read_param():
    if len(sys.argv) > 2:
        if sys.argv[1] == '--type':
            return sys.argv[2]
        else:
            sys.stderr.write('Required type parameter.\n')
            exit(1)
    else:
        sys.stderr.write('Required type parameter.\n')
        exit(1)

def read_instructions():
    instructions = []
    try:
        n = int(sys.stdin.readline())
    except:
        sys.stderr.write('Number of instructions must be integer.\n')
        exit(1)
    for _ in range(n):
        instructions.append(sys.stdin.readline().split())

    return instructions

def load(file_name, data_structure):
    global loads
    loads += 1
    #iterr = 0
    try:
        with open(file_name, 'r') as file:
            word = ''
            char = file.read(1)
            while char:
                if char == ' ' or char == '\n' or char == '\t' or char == '\r':
                    #print(iterr, word)
                    if word != '':
                        data_structure.insert(word)
                    char = file.read(1)
                    word = ''
                    #iterr += 1
                    continue
                word += char
                char = file.read(1)
    except:
        sys.stderr.write('Could not open file: ' + file_name + '\n')
        return

def execute_instructions(instructions, data_structure):
    for i in instructions:
        if i[0] == 'insert':
            data_structure.insert(i[1])
        elif i[0] == 'load':
            load(i[1], data_structure)
        elif i[0] == 'delete':
            data_structure.delete(i[1])
        elif i[0] == 'find':
            print(data_structure.find(i[1]))
        elif i[0] == 'min':
            print(data_structure.minimal())
        elif i[0] == 'max':
            print(data_structure.maximal())
        elif i[0] == 'successor':
            print(data_structure.successor(i[1]))
        elif i[0] == 'inorder':
            order = data_structure.inorder()
            for el in order:
                print(el, end = ' ')
            print()

def insert_from_load(words, data_structure):
    for w in words:
        data_structure.insert(w)

def execute():
    typee = read_param()
    if typee == 'bst':
        data_structure = BST()
    elif typee == 'rbt':
        data_structure = RBT()
    elif typee == 'hmap':
        data_structure = HMAP()
    elif typee == 'bloom':
        data_structure = Bloom()
    else:
        sys.stderr.write('Wrong data structure type.\n')
        exit(1)
    
    instructions = read_instructions()
    start = time.time()
    execute_instructions(instructions, data_structure)
    end = time.time() - start
    sys.stderr.write('time: ' + str(end) + 's\n')
    print_stats(data_structure)
    return data_structure

def print_stats(data_structure):
    sys.stderr.write('insert: ' + str(data_structure.stats.insert) + '\n')
    sys.stderr.write('load: ' + str(loads) + '\n')
    sys.stderr.write('delete: ' + str(data_structure.stats.delete) + '\n')
    sys.stderr.write('find: ' + str(data_structure.stats.find) + '\n')
    sys.stderr.write('min: ' + str(data_structure.stats.min) + '\n')
    sys.stderr.write('max: ' + str(data_structure.stats.max) + '\n')
    sys.stderr.write('successor: ' + str(data_structure.stats.successor) + '\n')
    sys.stderr.write('inorder: ' + str(data_structure.stats.inorder) + '\n')
    sys.stderr.write('max elements: ' + str(data_structure.stats.max_elements) + '\n')
    sys.stderr.write('current elements: ' + str(data_structure.stats.elements) + '\n')

def get_compares(data_structure):
    if type(data_structure) is HMAP:
        for structre in data_structure.hash_table:
            if type(structre) is RBT:
                data_structure.stats.compare += structre.stats.compare
    return data_structure.stats.compare

def main():
    execute()

if __name__ == "__main__":
    main()