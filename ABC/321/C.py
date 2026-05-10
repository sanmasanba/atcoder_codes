#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    K = int(input())
    ans = []
    # 10桁分のマスクを作成
    for mask in range(2, 1 << 10):
        x = 0
        # マスクの部分の数字のみを結合していく
        for i in range(9, -1, -1):
            if mask & (1 << i):
                x *= 10
                x += i
        ans.append(x)
    ans.sort()
    print(ans[K-1])

if __name__ == '__main__':
    main()