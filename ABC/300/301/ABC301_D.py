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
    # input
    S = list(input())
    N = int(input())
    
    min_s = list(map(lambda x: x if x != '?' else '0', S))
    # 最小にしてもNを超えるとき、達成不可
    res = int(''.join(min_s), 2)
    if N < res:
        print(-1)
        return
    
    # 一番大きいところから1にして試していく
    for i in range(len(S)):
        tmp = min_s[:]
        if S[i] == '?':
            tmp[i] = '1'
        tmp_n = int(''.join(tmp), 2)
        if tmp_n <= N:
            res = tmp_n
            min_s = tmp[:]
    
    # output
    print(res)

if __name__ == '__main__':
    main()