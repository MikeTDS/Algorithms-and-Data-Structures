from mst import prim, kruskal
import sys

def read_input():
    n = int(input())
    m = int(input())
    E = []
    for _ in range(m):
        raw = input().split()
        E.append([int(x) for x in raw[:-1]] + [float(raw[-1])])
    return n,E

def main():
    n, E = read_input()
    #E = [[e[0]+1, e[1]+1, e[2]] for e in E]
    V = [i+1 for i in range(n)]
    
    if len(sys.argv) < 2:
        sys.stderr.write('Wrong argument, choose -p or -k. \n')
        exit(1)

    if sys.argv[1] == '-p':
        S = prim(V,E,1)
        summ = 0
        for x in S:
            a,b = sorted((x.key, x.par.key))
            if x.dist != 0:
                print(a,b, x.dist)
            summ += x.dist
        print(summ)

    elif sys.argv[1] == '-k':
        S = kruskal(V,E)
        summ = 0
        for x in S:
            a,b = sorted((x[0], x[1]))
            print(a, b, x[2])
            summ += x[2]
        print(summ)

    else:
        sys.stderr.write('Wrong argument, choose -p or -k. \n')
        exit(1)
    
if __name__ == "__main__":
    main()