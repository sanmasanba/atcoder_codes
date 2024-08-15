#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, M = map(int, input().split(' '))
    Q = [list(input()) for _ in range(N)]
    for h in range(N-8):
        for w in range(M-8):
            # 左上
            res = True
            for dh in range(3):
                res &= all([Q[h+dh][w] == "#", Q[h+dh][w+1] == "#", Q[h+dh][w+2] == "#", Q[h+dh][w+3] == "."])
            res &= all([Q[h+3][w] == ".", Q[h+3][w+1] == ".", Q[h+3][w+2] == ".", Q[h+3][w+3] == "."])
            # 右下
            res &= all([Q[h+5][w+5] == ".", Q[h+5][w+6] == ".", Q[h+5][w+7] == ".", Q[h+5][w+8] == "."])
            for dh in range(3):
                res &= all([Q[h+6+dh][w+5] == ".", Q[h+6+dh][w+6] == "#", Q[h+6+dh][w+7] == "#", Q[h+6+dh][w+8] == "#"])
            if res:
                print(h+1, w+1)    

if __name__ == '__main__':
    main()