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
    N, T = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    # ループできるだけ回す
    T %= sum(A)
    
    #累積和を見る
    cumsumA = [0]
    for i in range(N):
        cumsumA.append(cumsumA[-1] + A[i])

    # 二分探索
    m_num = bisect_left(cumsumA, T)
    print(m_num, T-cumsumA[m_num-1])

if __name__ == '__main__':
    main()