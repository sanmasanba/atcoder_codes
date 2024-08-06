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
    N = input()
    
    res = 'Yes'
    for n in range(len(N)-1):
        # もし次の文字が同じか、以上なら
        if N[n] <= N[n+1]:
            res = 'No'
    print(res)

if __name__ == '__main__':
    main()