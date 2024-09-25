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
    N = list(map(int, list(input())))
    len_n = len(N)

    # 順列全列挙
    res = 0
    for perm in permutations(N):
        for thred in range(1, len_n):
            c += 1
            n1 = ''.join(map(str, perm[:thred]))
            n2 = ''.join(map(str, perm[thred:]))
            if n1[0] != 0 and n2[0] != 0:
                res = max(res, int(n1)*int(n2))
    print(res) 

if __name__ == '__main__':
    main()