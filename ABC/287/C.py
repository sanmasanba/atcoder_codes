#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

def search(G:dict, visited:set, i):
    visited.add(i)
    for j in G[i]:
        if j not in visited:
            return search(G, visited, j) 
        else:
            continue
    return i

def depth(G:dict, visited:set, i):
    visited.add(i)
    for j in G[i]:
        if j not in visited:
            return depth(G, visited, j) + 1
        else:
            continue
    return 0

#main
def main():
    N, M = map(int, input().split(' '))
    G = {}
    for _ in range(M):
        a, b = map(int, input().split(' '))
        if a not in G:
            G[a] = [b]
            if b not in G:
                G[b] = [a]
            else:
                G[b].append(a)
        else:
            G[a].append(b)    
            if b not in G:
                G[b] = [a]
            else:
                G[b].append(a)
    
    res = 0
    if M != 0:
        visited_1 = set()
        res = search(G, visited_1, 1)
        visited_2 = set()
        ans = depth(G, visited_2, res)
        print('Yes' if M == ans else 'No')
    else:
        print('No')

if __name__ == '__main__':
    main()