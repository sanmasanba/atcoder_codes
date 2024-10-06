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
    # 入力
    N = int(input())
    P = list(map(int, input().split(' ')))
    
    Q = [0]*N
    for i, p in enumerate(P):
        Q[p-1] = i+1
    
    # 出力
    print(*Q)

if __name__ == '__main__':
    main()