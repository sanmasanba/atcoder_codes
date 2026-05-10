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
    N = int(input())
    A = list(map(int, input().split(' ')))
    W = list(map(int, input().split(' ')))
    
    box = [0 for _ in range(N)]
    tmp = []
    for i in range(N):
        box[A[i]-1] += 1
        tmp.append((W[i], A[i]-1))
    tmp.sort()
    aw = deque(tmp)

    res = 0
    for b in box:
        if b == 0:
            while aw:
                x = aw.popleft()
                if box[x[1]] > 1:
                    res += x[0]
                    box[x[1]] -= 1
                    break
    print(res)


if __name__ == '__main__':
    main()