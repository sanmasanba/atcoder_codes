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
    M = int(input())
    D = list(map(int, input().split(' ')))
    mid_day = (sum(D)//2)
    i = 0
    while 1:
        if 0 < mid_day - D[i]:
            mid_day -= D[i]
            i += 1
        else:
            break
    month = i
    day = 1
    while 1:
        if 0 < mid_day and day < D[month]:
            day += 1
        elif 0 < mid_day and D[month] <= day:
            month += 1
            day = 1
        elif mid_day == 0:
            break
        mid_day -= 1
    print(month+1, day)


if __name__ == '__main__':
    main()