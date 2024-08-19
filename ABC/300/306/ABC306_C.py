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
    A = list(map(lambda x:int(x)-1, input().split(' ')))
    a_pos = [0 for _ in range(N)]
    for a in A:
        a_pos[a] += 1
        if a_pos[a] == 2:
            print(a+1, end=' ')

if __name__ == '__main__':
    main()