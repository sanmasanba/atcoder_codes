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
    A, B = input().split(' ')
    A = int(A)
    B = int(B.replace('.', ''))
    C = 100

    # 桁落ちに注意して出力
    print((A*B)//100)

if __name__ == '__main__':
    main()