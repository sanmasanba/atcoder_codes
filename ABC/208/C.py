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
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # 国民番号を小さい順にする
    a2order = {a:i for i, a in enumerate(sorted(A))}

    # 配れる最低数と残りを記録
    base_sweets = K//N
    k = K%N

    # 国民番号の小さい順が、残り個数以下の国民に再配布
    for a in A:
        print(base_sweets + (1 if a2order[a] < k else 0))

if __name__ == '__main__':
    main()