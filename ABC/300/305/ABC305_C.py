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
    H, W = map(int, input().split(' '))
    grid = [input() for _ in range(H)]
    
    for i in range(H-1):
        h1 = grid[i]
        h2 = grid[i+1]
        # クッキーが並んでいる列とりあげる
        if "#" in h1 and "#" in h2 and h1 != h2:
            # クッキーが欠けているx座標を調べる
            for j in range(W):
                if h1[j] != h2[j]:
                    w = j + 1
                    break
            # y座標を確定する
            h = i+1 if grid[i][w-1] == "." else i+2
            break
    print(h, w)

if __name__ == '__main__':
    main()