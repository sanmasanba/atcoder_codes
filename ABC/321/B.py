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
    N, X = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    tmp_min, tmp_max, tmp_sum = min(A), max(A), sum(A)
    tmp_score = tmp_sum - tmp_min - tmp_max
    res = -1
    for score in range(101):
        tmp_A = [score] + A
        tmp_A.sort()
        tmp_min, tmp_max, tmp_sum = min(tmp_A), max(tmp_A), sum(tmp_A)
        tmp_score = tmp_sum - tmp_min - tmp_max
        if X <= tmp_score:
            res = score
            break
    print(res)

if __name__ == '__main__':
    main()