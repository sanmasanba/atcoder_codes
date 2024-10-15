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
    N, M, P = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    B.sort()
    cumsumB = [0]
    for i in range(M):
        cumsumB.append(cumsumB[-1] + B[i])

    res = 0    
    for i in range(N):
        a_cost = A[i]
        min_b = P - a_cost
        # 主菜だけでP円以上なら、どの副菜を選んでもP円
        if min_b <= 0:
            res += M * P
            continue

        # 選んでもP円を超えない範囲を求める
        b_cnt = bisect_left(B, min_b)
        res += P*(M-b_cnt) + (b_cnt*a_cost + cumsumB[b_cnt])
    
    # output
    print(res)

if __name__ == '__main__':
    main()