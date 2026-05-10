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
    A, B, N = map(int, input().split(' '))

    # 試すと、最大はx = B-1の時か、x = Nの時とわかる
    res = 0
    res = max(res, ((A*N)//B)-A*(N//B))
    if B - 1 <= N:
        res = max(res,  ((A*(B-1))//B)-A*((B-1)//B))
    
    # 出力
    print(res)

if __name__ == '__main__':
    main()