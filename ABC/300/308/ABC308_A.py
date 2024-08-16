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
    S = list(map(int, input().split(' ')))
    res = 'Yes'
    for i in range(len(S)-1):
        if not S[i] <= S[i+1] or not 100 <= S[i] <= 675 or not 100 <= S[i+1] <= 675 or not S[i]%25 == 0 or not S[i+1]%25 == 0:
            res = 'No'
    print(res)

if __name__ == '__main__':
    main()