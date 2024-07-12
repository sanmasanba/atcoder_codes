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
    W, B = map(int, input().split(' '))
    S = list("wbwbwwbwbwbw")

    for _ in range(5):
        S += S

    res = 'No'
    for i in range(12):
        s = S[i:i+W+B+1]
        w = 0
        b = 0
        for j in range(W+B):
            w += s[j] == "w"
            b += s[j] == "b"
        if w == W and b == B:
            res = 'Yes'
            break

    print(res)

if __name__ == '__main__':
    main()