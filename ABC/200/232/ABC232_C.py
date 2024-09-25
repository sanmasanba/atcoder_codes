#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    G1 = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        G1[a].add(b)
        G1[b].add(a)
    G2 = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split(' '))
        G2[a].add(b)
        G2[b].add(a)
    
    # 順列全列挙でそれぞれの頂点を対応させるパターンを全部試す
    res = False
    for perm in permutations([i for i in range(N)]):
        tmp_res = True
        for p in range(N):
            tmp_res &= all([perm[n] in G2[perm[p]] for n in G1[p]])
        res |= tmp_res
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()