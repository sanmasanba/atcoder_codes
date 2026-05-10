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
    S = [input() for _ in range(N)]
    
    res = 'Yes'
    for i in range(len(S)-2):
        if S[i] == "sweet" and S[i+1] == "sweet":
            res = 'No'
            break
    print(res)

if __name__ == '__main__':
    main()