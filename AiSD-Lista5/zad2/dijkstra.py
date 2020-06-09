from pqueue import PriorityQueue, Node
from sys import maxsize

def dijkstra(V, E, s):
    Q = PriorityQueue()
    A = [[] for _ in range(len(V))]
    S = [Node(i+1,maxsize,-1) for i in range(len(V))]

    S[s-1].dist = 0
    S[s-1].par = s

    for i in range(len(E)):
        A[E[i][0]-1].append((E[i][1], E[i][2]))

    for v in S:
        Q.insert(v)

    while Q.size > 0:
        u = Q.q[0]
        Q.pop()
        for ver, w in A[u.key-1]:
            v = S[ver-1]
            if v.dist > u.dist + w:
                v.dist = u.dist + w
                v.par = u
                Q.decrease_key(Q.q.index(v), v.dist)
    return S

# def dijkstra(V, E, s):
#     Q = PriorityQueue()
#     A = [[] for _ in range(len(V))]
#     S = [Node(i,maxsize,-1) for i in range(len(V))]

#     S[s].dist = 0
#     S[s].par = s

#     for i in range(len(E)):
#         A[E[i][0]].append((E[i][1], E[i][2]))

#     for v in S:
#         Q.insert(v)

#     while Q.size > 0:
#         u = Q.q[0]
#         Q.pop()
#         for ver, w in A[u.key]:
#             v = S[ver]
#             if v.dist > u.dist + w:
#                 v.dist = u.dist + w
#                 v.par = u
#                 Q.decrease_key(Q.q.index(v), v.dist)
#     return S
    
    


