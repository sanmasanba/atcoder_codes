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
    N, M, D = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    A.sort()
    B.sort()

    res = -1
    b_pos = 0
    for a in A:
        # 差を限界まで大きくして、Bを最大化する
        while b_pos+1 < M and (abs(a-B[b_pos+1]) <= D or abs(a-B[b_pos+1]) <= abs(a-B[b_pos])): 
            b_pos += 1
        if abs(a-B[b_pos]) <= D:
            res = max(res, a+B[b_pos])
    
    print(res)

if __name__ == '__main__':
    main()

