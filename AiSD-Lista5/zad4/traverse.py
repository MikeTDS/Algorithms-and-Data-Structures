from pqueue import PriorityQueue, Node
from mst import kruskal, prim
import random
import time
import tracemalloc
from sys import maxsize

def count_visited(V):
    c = 0
    for v in V:
        if v == True:
            c+=1
    return c

def random_walk(V,E,starting):
    k = 0
    W = 0
    M = 0
    M_add = 0
    tracemalloc.start()
    t = time.time()
    visited = [False for _ in range(len(V))]
    A = [[] for _ in range(len(V))]
    current = starting
    visited[current-1] = True
    path = [current]

    for e in E:
        A[e[0]-1].append((e[1],e[2]))
        A[e[1]-1].append((e[0],e[2]))
    
    while count_visited(visited) < len(V):
        next_v = random.choice(A[current-1])
        while visited[next_v[0]-1]:
           next_v = random.choice(A[current-1])

        #next_v = random.choice(A[current-1])

        visited[next_v[0]-1] = True
        k += 1
        W += next_v[1]
        current = next_v[0]
        path.append(current)
    
    _, peak = tracemalloc.get_traced_memory()
    M = peak/10**6
    tracemalloc.stop()
    M_add += sum(len(A) for a in A) + len(visited)
    
    return k,W,M,time.time()-t,path, M_add

def find_min(A, visited):
    e = None
    minn = maxsize
    for i in range(len(A)):
        if A[i][1] < minn and not visited[A[i][0]-1]:
            minn = A[i][1]
            e = A[i]
    return e

def weight_walk(V,E,starting):
    k = 0
    W = 0
    M = 0
    M_add = 0
    tracemalloc.start()
    t = time.time()
    visited = [False for _ in range(len(V))]
    A = [[] for _ in range(len(V))]
    current = starting
    visited[current-1] = True
    path = [current]

    for e in E:
        A[e[0]-1].append((e[1],e[2]))
        A[e[1]-1].append((e[0],e[2]))
    
    while count_visited(visited) < len(V):
        next_v = find_min(A[current-1], visited)
        visited[next_v[0]-1] = True
        k += 1
        W += next_v[1]
        current = next_v[0]
        path.append(current)
    
    _, peak = tracemalloc.get_traced_memory()
    M = peak/10**6
    tracemalloc.stop()
    M_add += sum(len(A) for a in A) + len(visited)
    
    return k,W,M,time.time()-t,path, M_add

def find_next(current, A):
    for a in A[current-1]:
        if a[2] == 0:
            a[2] = 1
            for aa in A[a[0]-1]:
                if aa[0] == current:
                    aa[2] = 1
            return a[0], a[1]
    
    for a in A[current-1]:
        if a[2] == 1:
            a[2] = 2
            for aa in A[a[0]-1]:
                if aa[0] == current:
                    aa[2] = 2
            return a[0], a[1]
    
def mst_walk_prim(V,E,starting):
    k = 0
    W = 0
    M = 0
    M_add = 0
    tracemalloc.start()
    t = time.time()
    S, madd = prim(V,E,starting)
    A = [[] for _ in range(len(V))]
    current = starting
    path = [current]

    for s in S:
        if s.dist > 0:
            A[s.key-1].append([s.par.key, s.dist, 0])
            A[s.par.key-1].append([s.key, s.dist, 0])
    
    while True:
        ans = find_next(current, A)
        if ans:
            current, w = ans
            path.append(current)
            k += 1
            W += w
        else:
            break
    
    _, peak = tracemalloc.get_traced_memory()
    M = peak/10**6
    tracemalloc.stop()
    M_add += sum(len(A) for a in A) + len(S)
    #path = list(dict.fromkeys(path))
    return k,W,M,time.time()-t,path, M_add + madd

def mst_walk_kruskal(V,E,starting):
    k = 0
    W = 0
    M = 0
    M_add = 0
    tracemalloc.start()
    t = time.time()
    S, madd = kruskal(V,E)
    A = [[] for _ in range(len(V))]
    current = starting
    path = [current]

    for s in S:
        if s[2] > 0:
            A[s[0]-1].append([s[1], s[2], 0])
            A[s[1]-1].append([s[0], s[2], 0])
    
    while True:
        ans = find_next(current, A)
        if ans:
            current, w = ans
            path.append(current)
            k += 1
            W += w
        else:
            break
    
    _, peak = tracemalloc.get_traced_memory()
    M = peak/10**6
    tracemalloc.stop()
    M_add += sum(len(A) for a in A) + len(S)
    #path = list(dict.fromkeys(path))
    return k,W,M,time.time()-t,path, M_add + madd

#5
costs = dict()
A = []


def dynamic(V,E,starting):
    global costs
    global A

    t = time.time()
    tracemalloc.start()
    A = [[] for _ in range(len(V))]

    for e in E:
        A[e[0]-1].append((e[1],e[2]))
        A[e[1]-1].append((e[0],e[2]))
    
    c, p = cost(starting,0,len(V)-1,set(range(1, len(V)+1)),[])
    _, peak = tracemalloc.get_traced_memory()
    M = peak/10**6
    tracemalloc.stop()
    total_mem = len(p) + sum(len(a) for a in A) + sum(len(c) for c in costs)
    return len(p)-1, c, M, time.time() - t, p, total_mem

def cost(current,k,fin,not_visited,path):
    global costs
    min_cost = maxsize

    not_visited.remove(current)

    if fin == k:
        return 0, [current]

    if (current, tuple(sorted(not_visited))) in costs:
        return costs[current, tuple(sorted(not_visited))]

    for n in A[current-1]:
        if n[0] in not_visited:
            cur_cost, new_path = cost(n[0], k+1, fin, not_visited.copy(), path)
            cur_cost += n[1]
            
            if min_cost == maxsize or cur_cost < min_cost:
                min_cost = cur_cost
                temp_path = new_path
                costs[current, tuple(sorted(not_visited))] = [min_cost, [current]+temp_path]

    return costs[current, tuple(sorted(not_visited))]




    


    

