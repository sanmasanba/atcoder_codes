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
    N = int(input())
    A = [0] + list(map(int, input().split(' ')))
    # 場所と数字が一致している要素の数
    cnt = 0
    # Ai = jのとき、A[j] = iである数
    res = 0
    for i, j in enumerate(A):
        if i == 0:
            continue
        if i == A[j]:
            res += 1
        if i == j:
            cnt += 1
    print((res-cnt)//2 + (cnt*(cnt-1))//2)

if __name__ == '__main__':
    main()