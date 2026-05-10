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
    # input
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    cumsum = [0]
    sum_dict = defaultdict(int)    
    # cumsum
    for i in range(N):
        if i == 0:
            cumsum[0] = A[i]
            continue
        cumsum.append(cumsum[-1]+A[i])
    for c in cumsum:
        sum_dict[c] += 1
    
    res = 0
    for i in range(N):
        k = (0 if i == 0 else cumsum[i-1]) + K
        res += sum_dict.get(k, 0)
        sum_dict[cumsum[i]] -= 1
 
    # output
    print(res)

if __name__ == '__main__':
    main()