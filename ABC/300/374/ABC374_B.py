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
    S = list(input())
    T = list(input())
    S_len = len(S)
    T_len= len(T)

    if S == T:
        print(0)
        return
    for i in range(min(S_len, T_len)):
        if S[i] != T[i]:
            print(i+1)
            return
    
    print(min(S_len, T_len)+1)

if __name__ == '__main__':
    main()