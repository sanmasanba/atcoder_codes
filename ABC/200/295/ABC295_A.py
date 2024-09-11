#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    S = list(input().split(' '))    
    print("Yes" if any([any(s == v for v in ["and", "not", "that", "the", "you"]) for s in S]) else "No")

if __name__ == '__main__':
    main()