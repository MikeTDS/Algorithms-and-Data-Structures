from mst import prim, kruskal
from traverse import random_walk, weight_walk, mst_walk_prim, mst_walk_kruskal, dynamic
import random
import sys

def read_input():
    n = int(input())
    E = []
    for _ in range((n*(n-1))//2):
        raw = input().split()
        E.append([int(x) for x in raw[:-1]] + [float(raw[-1])])
    return n,E

def main():
    sys.setrecursionlimit(10**6)
    n, E = read_input()
    V = [i+1 for i in range(n)]
    starting = random.choice(V)
    #funcs = [random_walk, weight_walk, mst_walk_prim, mst_walk_kruskal, dynamic]
    funcs = [random_walk, weight_walk, mst_walk_prim, dynamic]
    titles = ["Random walk:", "Weight walk", "MST walk - Prim:", "MST walk - Kruskal:", "Dynamic: "]
    #funcs = [weight_walk, dynamic]
    #titles = ['Weight_walk','Dynamic: ']
    for i in range(len(funcs)):
        #print(titles[i])
        k,W,M,t,path, M_add = funcs[i](V,E,starting)
        # print('steps = ' + str(k))
        # print('distance = ' + str(round(W,5)))
        # print('additional memory = ' + str(M_add))
        # print('time = ' + str(t) + ' s')
        # print('traced memory peak = ' + str(M))
        print(k, W, M_add, t)
        for p in path:
            sys.stderr.write(str(p) + ' ')
        sys.stderr.write('\n')
        print()
    
if __name__ == "__main__":
    main()