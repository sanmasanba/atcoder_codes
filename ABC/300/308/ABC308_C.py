#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def cmp(a, b):
    x1, y1, i1 = a
    x2, y2, i2 = b
    # A_i(A_j+B_j) < A_j(A_i+B_i)を比較する
    s = x1*y2 - y1*x2
    # j番目のほうが大きいとき1、等しいとき0、小さいとき-1を返す
    return 1 if s > 0 else -1 if s < 0 else 0

#main
def main():
    N = int(input())
    success_ratio = []
    for i in range(N):
        a, b = map(int, input().split(' '))
        success_ratio.append((-a, a+b, i))
    success_ratio.sort(key=cmp_to_key(cmp))
    print(*[i+1 for _, _, i in success_ratio])
    
if __name__ == '__main__':
    main()