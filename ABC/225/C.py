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
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split(' '))))

    # 全て調べる
    res = True
    for i in range(N):
        for j in range(M):
            # Bの要素は次の要素を満たす
            # Bの要素は、一つ上の要素との差が7になる ... (i) 
            # Bの要素は、右方向へ必ず1ずつ増加する ... (ii)
            # Bの要素は、1-7, 8-14, ..., の範囲で推移する ... (iii)
            check_up = True
            check_side = True
            check_range = True
            # (i)
            if 0 < i:
                check_up = B[i-1][0]+7 == B[i][0]
            # (ii)
            if 0 < j:
                check_side = B[i][j-1]+1 == B[i][j]
            row_top = 7*((B[i][0]-1)//7)+1
            # (iii)
            check_range = row_top <= B[i][j] < row_top+7
            res &= check_up and check_side and check_range

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()