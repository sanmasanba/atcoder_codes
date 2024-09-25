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
    Ps = []
    for i in range(N):
        Ps.append([sum(list(map(int, input().split(' ')))), i])
    sortedPs = sorted(Ps)

    # 自分より大きい要素の数を数える
    res = [0] * N
    for i in range(N):
        point = min(sortedPs[i][0]+300, 1200)
        order = bisect_right(sortedPs, point, key=lambda x: x[0])
        res[sortedPs[i][1]] = N-order+1 <= K
    
    # 出力
    for i in range(N):
        print('Yes' if res[i] else 'No')

if __name__ == '__main__':
    main()