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
    p, q = input().split(' ')
    dist = {"A":0, "B":3, "C":4, "D":8, "E":9, "F":14, "G":23}
    if ord(p) > ord(q):
        q, p = p, q
    print(dist[q]-dist[p])

if __name__ == '__main__':
    main()