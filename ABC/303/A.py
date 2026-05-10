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
    S = input()
    T = input()
    res = 'Yes'
    for i in range(N):
        if S[i] == T[i]:
            continue
        if (S[i] == "1" and T[i] == "l") or (S[i] == "l" and T[i] == "1"):
            continue
        if (S[i] == "o" and T[i] == "0") or (S[i] == "0" and T[i] == "o"):
            continue
        res = 'No'
    print(res)

if __name__ == '__main__':
    main()