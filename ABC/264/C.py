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
    H1, W1 = map(int, input().split(' '))
    A = [list(map(int, input().split(' '))) for _ in range(H1)]
    H2, W2 = map(int, input().split(' '))
    B = [list(map(int, input().split(' '))) for _ in range(H2)]

    res = False
    # bit全探索
    for mask_h in range(2**H1):
        for mask_w in range(2**W1):
            tmp = []
            # 行と列は独立しているので別に考える
            for i in range(H1):
                if mask_h >> i & 1:
                    tmp_row = []
                    for j in range(W1):
                        if mask_w >> j & 1:
                            tmp_row.append(A[i][j])
                    tmp.append(tmp_row)
            if B == tmp:
                res = True
    print("Yes" if res else "No")

if __name__ == '__main__':
    main()