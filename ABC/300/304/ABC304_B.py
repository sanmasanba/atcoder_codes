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
    if N <= 10**3-1:
        print(N)
    elif 10**3 <= N <= 10**4-1:
        print((N//10)*10)
    elif N <= 10**5-1:
        print((N//100)*100)
    elif N <= 10**6-1:
        print((N//1000)*1000)
    elif N <= 10**7-1:
        print((N//10000)*10000)
    elif N <= 10**8-1:
        print((N//100000)*100000)
    elif N <= 10**9-1:
        print((N//1000000)*1000000)

if __name__ == '__main__':
    main()