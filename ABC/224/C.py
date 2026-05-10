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
    dots = []
    for _ in range(N):
        dots.append(list(map(int, input().split(' '))))

    # 組み合わせの数を全て調べる
    res = 0
    for n1, n2, n3 in combinations(dots, 3):
        # 直線の式を満たすものを数え上げる
        if n3[1]*(n2[0]-n1[0]) != (n2[1]-n1[1])*(n3[0]-n2[0])+n2[1]*(n2[0]-n1[0]):
            res += 1
    print(res)

if __name__ == '__main__':
    main()