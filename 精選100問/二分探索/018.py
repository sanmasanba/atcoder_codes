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
    S = list(map(int, input().split(' ')))
    q = int(input())
    T = list(map(int, input().split(' ')))
    
    cnt = 0
    for q in T:
        pos = bisect_left(S, q)
        try:
            if S[pos] == q:
                cnt += 1
        except:
            pass
    print(cnt)

if __name__ == '__main__':
    main()