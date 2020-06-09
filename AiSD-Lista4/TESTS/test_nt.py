from RBT import RBT
import random
import time

class ListNode():
    def __init__(self, key):
        self.key = key
        self.next = None

def insert_list(key, List):
    node = ListNode(key)
    current = List
    if current is None:
        List = node
        return
    while current.next:
        current = current.next
    current.next = node
    return node

def find_in_list(key, List):
    current = List
    if current:
        if current.key == key:
            return 1
        while current.next:
            current = current.next
            if current.key == key:
                return 1
    return 0

def main():
    for n in range(10,201,10):
        list_avg = []
        rbt_avg = []
        for k in range(1000):
            rbt = RBT()
            rbt.insert('gwnas')
            listt = ListNode('gwnas')
            to_insert = []
            to_find = []
            for i in range(n):
                to_insert.append(''.join([random.choice('qwertyuiopasdfghjklzxcvbnm') for m in range(5)]))
            for i in range(n//5):
                to_find.append(random.choice(to_insert))

            for elem in to_insert:
                rbt.insert(elem)

            start = time.time()
            for elem in to_find:
                rbt.find(elem)
            end_rbt = time.time() - start

            for elem in to_insert:
                insert_list(elem, listt)

            start = time.time()
            for elem in to_find:
                find_in_list(elem, listt)
            end_list = time.time() - start
            
            rbt_avg.append(end_rbt)
            list_avg.append(end_list)
        
        print(n)
        print('rbt: ' + str(sum(rbt_avg)/len(rbt_avg)))
        print('list: ' + str(sum(list_avg)/len(list_avg)))
        print()

if __name__ == "__main__":
    main()
