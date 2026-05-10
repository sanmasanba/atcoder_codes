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
    N = int(input())
    for i in range(N, 1000):
        h, t, o = str(i)
        if int(h)*int(t) == int(o):
            print(i)
            break
        
if __name__ == '__main__':
    main()