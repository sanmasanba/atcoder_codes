#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

res = 0
#main
def main():
    S = list(input())
    for n in range(1, len(S)+1):
        for i in range(len(S)-n+1):
            tmp_res = True
            for pos in range(n//2):
                if S[i+pos] != S[i-1+n-pos]:
                    tmp_res = False
                    break
            if tmp_res:
                res = n
    print(res)

if __name__ == '__main__':
    main()