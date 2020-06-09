from pqueue import PriorityQueue, Node
from sys import maxsize

def prim(V,E,s):

    Q = PriorityQueue()
    A = [[] for _ in range(len(V))]
    S = []
    for i in range(len(E)):
        A[E[i][0]-1].append((E[i][1], E[i][2]))
        A[E[i][1]-1].append((E[i][0], E[i][2]))

    for v in V:
        if v == s:
            node = Node(s,0,s)
            node.par = node
        else:
            node = Node(v,maxsize,None)
        Q.insert(node)

    while Q.size > 0:
        u = Q.q[0]
        Q.pop()
        S.append(u)
        for ver, w in A[u.key-1]:
            v = Q.get(ver)
            if v and w < v.dist:
                v.par = u
                v.dist = w
                Q.decrease_key(Q.q.index(v), w)
    
    return S[1:], sum(len(a) for a in A) + len(V)

parent = dict()
rank = dict()

def make_set(v):
    parent[v-1] = v
    rank[v-1] = 0

def find(v):
    if parent[v-1] != v:
        parent[v-1] = find(parent[v-1])
    return parent[v-1]

def union(u,v):
    u = find(u)
    v = find(v)
    if v != u:
        if rank[u-1] > rank[v-1]:
            parent[v-1] = u
        else:
            parent[u-1] = v

        if rank[u-1] == rank[v-1]:
            rank[v-1] += 1

def kruskal(V,E):
    A = set()

    for v in V:
        make_set(v)
        
    Q = PriorityQueue()
    for e in E:
        Q.insert(Node(e[0],e[2],e[1]))

    while Q.size > 0:
        e = Q.q[0]
        Q.pop()
        if find(e.key) != find(e.par):
            A.add((e.key, e.par, e.dist))
            union(e.key, e.par)
    return A, len(parent) + len(rank) + len(E)
