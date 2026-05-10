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
    name_set = {i+1:set() for i in range(N)}
    res = []
    for _ in range(M):
        a, b = input().split(' ')
        if b == 'M' and b not in name_set[int(a)]:
            res.append('Yes')
        else:
            res.append('No')
        name_set[int(a)].add(b)

    print(*res, sep='\n')

if __name__ == '__main__':
    main()