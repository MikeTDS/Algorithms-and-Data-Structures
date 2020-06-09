from dijkstra import dijkstra
import sys
import time

def read_input():
    n = int(input())
    m = int(input())
    E = []
    for _ in range(m):
        raw = input().split()
        E.append([int(x) for x in raw[:-1]] + [float(raw[-1])])
    s = int(input())
    return n,E,s

def find_w(x,y,E):
    for e in E:
        if e[0] == x and e[1] == y:
            return e[2]

def print_paths(S,s,E):
    for x in S:
        p = []
        while x.key != x.par:
            p.append(x.key)
            x = x.par
        p.append(s)

        p = p[::-1]

        sys.stderr.write('(' + str(p[0]) + ')')
        for i in range(1,len(p)):
            w = find_w(p[i-1], p[i], E)
            sys.stderr.write('--' + str(w) + '--' + '(' + str(p[i]) + ')')
        sys.stderr.write('\n')

def main():
    start = time.time()
    n, E, s = read_input()
    V = [i+1 for i in range(n)]
    S = dijkstra(V,E,s)
    for x in S:
        print(x.key, x.dist)
    print_paths(S,s,E)
    sys.stderr.write(str((time.time()-start)*(1000)) + ' ms\n')



if __name__ == "__main__":
    main()