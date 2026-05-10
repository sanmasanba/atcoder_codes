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
    S = list(input())
    res = 'Yes'
    for i in range(len(S)):
        if i%2 == 1 and S[i] == '1':
            res = 'No'
    print(res)

if __name__ == '__main__':
    main()