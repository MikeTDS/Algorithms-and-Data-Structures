import sys
import random
import time
import os

compares = 0

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def read_params():
    if len(sys.argv)<2:
        return False
    if sys.argv[1] == '--stat':
        return True
    
def read_input():
    temp = input('array: ').split()
    val = int(input('value: '))
    array = [int(x) for x in temp]
    return array, val

def check_if_sorted(array):
    if all(array[i] <= array[i+1] for i in range(len(array)-1)):
        return True
    return False

def array_to_bst(array):
    if not array:
        return None
    mid = len(array)//2
    root = Node(array[mid])
    root.left = array_to_bst(array[:mid])
    root.right = array_to_bst(array[mid+1:])
    return root

def search(root,key):
    global compares
    if root is None:
        return False
    compares += 1 
    if root.val == key:
        return True
    compares += 1 
    if root.val < key:
        return search(root.right, key)   
    return search(root.left, key)

def DFS(root):
    if root is None:
        return
    print(root.val)
    DFS(root.left)
    DFS(root.right)

def generate_random_bst(n):
    key = n+1
    vals = [x for x in range(1,n+1)]
    bst = array_to_bst(vals)
    return bst, key

def main():
    global compares
    stats = read_params()
    if stats:
        if os.path.exists('bst.data'):
            os.remove('bst.data')
        for n in range(1000,101000,1000):
            compares = 0
            bst, key = generate_random_bst(n)
            start = time.time()
            search(bst,key)
            end = time.time()-start
            print(n, compares, "%.16f" %end)
            with open('bst.data', 'a') as file:
                file.write(str(n) + ';' + str(compares) + ';' + "%.16f" %end + '\n')

    else:
        array, key = read_input()
        if not check_if_sorted(array):
            sys.stderr.write('ERROR: array needs to be sorted. \n')
            exit(1)
        bst = array_to_bst(array)
        if search(bst,key):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()