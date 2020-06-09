from pqueue import PriorityQueue
import random

pq = PriorityQueue()

def read_input():
    instr = []
    M = int(input())
    for i in range(M):
        instr.append(input().split())
    return instr

def execute(instr):
    for i in instr:
        if i[0] == 'insert':
            pq.insert(int(i[1]), int(i[2]))
        elif i[0] == 'empty':
            pq.empty()
        elif i[0] == 'top':
            pq.top()
        elif i[0] == 'pop':
            pq.pop()
        elif i[0] == 'priority':
            pq.priority(int(i[1]),int(i[2]))
        elif i[0] == 'print':
            pq.print()
        else:
            print('Wrong instruction.')

def main():
    instr = read_input()
    execute(instr)

if __name__ == "__main__":
    main()
