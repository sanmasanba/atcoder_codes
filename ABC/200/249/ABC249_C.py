#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    L = [list(input()) for _ in range(N)]
    
    res = 0
    for i in range(1, 2**N):
        string = []
        for j in range(N):
            if (i >> j) & 1:
                string += L[j]

        c = Counter(string)
        _, cnt = zip(*c.most_common())
        tmp = 0
        for k in cnt:
            if k == K:
                tmp += 1
        if tmp > res:
            res = tmp

    print(res)

if __name__ == '__main__':
    main()