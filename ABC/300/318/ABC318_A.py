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
    N, M, P = map(int, input().split(' '))
    
    day = M
    cnt = 0
    while day <= N:
        cnt += 1
        day += P 
    print(cnt)

if __name__ == '__main__':
    main()