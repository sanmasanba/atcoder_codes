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
    S = list(input())
    
    res = -1
    for i in range(N-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
            res = i+1
            break
    print(res) 

if __name__ == '__main__':
    main()