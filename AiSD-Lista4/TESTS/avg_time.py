from BST import BST
from HMAP import HMAP
from RBT import RBT
import random
import time
import sys
sys.setrecursionlimit(10**6)

N = 300000
F = 50000
R = 20

def main():
    bst_insert = []
    rbt_insert = []
    hmap_insert = []
    bst_find = []
    rbt_find = []
    hmap_find = []
    bst_min = []
    rbt_min = []
    bst_max = []
    rbt_max = []
    bst_successor = []
    rbt_successor = []
    bst_inorder = []
    rbt_inorder = []
    bst_delete = []
    rbt_delete = []
    hmap_delete = []

    for N in range(5000,100001,5000):
        print(N)
        F = N//5
        bst = BST()
        rbt = RBT()
        hmap = HMAP()

        to_insert = []
        to_find = []
        for n in range(N):
            to_insert.append(''.join([random.choice('qwertyuiopasdfghjklzxcvbnm') for m in range(5)]))
        for f in range(F):
            to_find.append(random.choice(to_insert))
        #insert
        start = time.time()
        for x in to_insert:
            bst.insert(x)
        end = time.time() - start
        bst_insert.append(end/N)

        start = time.time()
        for x in to_insert:
            rbt.insert(x)
        end = time.time() - start
        rbt_insert.append(end/N)

        start = time.time()
        for x in to_insert:
            hmap.insert(x)
        end = time.time() - start
        hmap_insert.append(end/N)

        #find
        start = time.time()
        for x in to_find:
            bst.find(x)
        end = time.time() - start
        bst_find.append(end/N)

        start = time.time()
        for x in to_find:
            rbt.find(x)
        end = time.time() - start
        rbt_find.append(end/N)

        start = time.time()
        for x in to_find:
            hmap.find(x)
        end = time.time() - start
        hmap_find.append(end/N)

        #min
        start = time.time()
        bst.minimal()
        end = time.time() - start
        bst_min.append(end)

        start = time.time()
        rbt.minimal()
        end = time.time() - start
        rbt_min.append(end)

        #max
        start = time.time()
        bst.maximal()
        end = time.time() - start
        bst_max.append(end)

        start = time.time()
        rbt.maximal()
        end = time.time() - start
        rbt_max.append(end)

        #successor
        start = time.time()
        for x in to_find:
            bst.successor(x)
        end = time.time() - start
        bst_successor.append(end/N)

        start = time.time()
        for x in to_find:
            rbt.successor(x)
        end = time.time() - start
        rbt_successor.append(end/N)

        #inorder
        start = time.time()
        bst.inorder()
        end = time.time() - start
        bst_inorder.append(end)

        start = time.time()
        rbt.inorder()
        end = time.time() - start
        rbt_inorder.append(end)

        #delete
        start = time.time()
        for x in to_insert:
            bst.delete(x)
        end = time.time() - start
        bst_delete.append(end/N)

        start = time.time()
        for x in to_insert:
            rbt.delete(x)
        end = time.time() - start
        rbt_delete.append(end/N)

        start = time.time()
        for x in to_insert:
            hmap.delete(x)
        end = time.time() - start
        hmap_delete.append(end/N)

    print("Average time in seconds")
    print("Insert: ")
    print("BST: " + str(sum(bst_insert)/R))
    print("RBT: " + str(sum(rbt_insert)/R))
    print("HMAP: " + str(sum(hmap_insert)/R))
    print("Find: ")
    print("BST: " + str(sum(bst_find)/R))
    print("RBT: " + str(sum(rbt_find)/R))
    print("HMAP: " + str(sum(hmap_find)/R))
    print("Min: ")
    print("BST: " + str(sum(bst_min)/R))
    print("RBT: " + str(sum(rbt_min)/R))
    print("Max: ")
    print("BST: " + str(sum(bst_max)/R))
    print("RBT: " + str(sum(rbt_max)/R))
    print("Successor: ")
    print("BST: " + str(sum(bst_successor)/R))
    print("RBT: " + str(sum(rbt_successor)/R))
    print("Inorder: ")
    print("BST: " + str(sum(bst_inorder)/R))
    print("RBT: " + str(sum(rbt_inorder)/R))
    print("Delete: ")
    print("BST: " + str(sum(bst_delete)/R))
    print("RBT: " + str(sum(rbt_delete)/R))
    print("HMAP: " + str(sum(hmap_delete)/R))
        
        

        

if __name__ == "__main__":
    main()