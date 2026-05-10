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
    N = int(input())
    SA = []
    min_age, min_num = INF, 0
    for i in range(N):
        s, a = input().split(' ')
        SA.append([int(a), s])
        if int(a) < min_age:
            min_age = int(a)
            min_num = i
    SA += SA
    for i in range(N):
        print(SA[min_num+i][1])    

if __name__ == '__main__':
    main()