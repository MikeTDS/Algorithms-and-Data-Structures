from RBT import RBT
from BST import BST
import random

inserts = 1000
deletes = 1000

def main():
    for k in range(10000):
        print(k)
        to_insert = []
        to_delete = []
        for i in range(inserts):
            to_insert.append(''.join([random.choice("abcdefghijklmnoprstuwxyz") for j in range(3)]))
        for i in range(deletes):
            to_delete.append(random.choice(to_insert))
        to_delete = list(dict.fromkeys(to_delete))

        rbt = RBT()
        bst = BST()
        
        for i in to_insert:
            rbt.insert(i)
            bst.insert(i)
    

        for j in to_delete:
            rbt.delete(j)
            bst.delete(j)

        if rbt.inorder() != bst.inorder():
            print(to_insert)
            print(to_delete)
            print(rbt.inorder())
            print(bst.inorder())
            print(len(to_insert))
            print(len(to_delete))
            print(len(rbt.inorder()))
            print(len(bst.inorder()))
            for b in bst.inorder():
                if b not in rbt.inorder():
                    print(b)
            break

if __name__ == "__main__":
    main()