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
    N, M = map(int, input().split(' '))
    C = list(input().split(' '))
    D = list(input().split(' '))
    P = list(map(int, input().split(' ')))
    dish2value = {}
    for k, v in zip(D, P[1:]):
        dish2value[k] = v
    print(sum([dish2value[k] if k in dish2value else P[0] for k in C]))    

if __name__ == '__main__':
    main()