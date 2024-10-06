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
    L, N1, N2 = map(int, input().split(' '))
    line1 = []; line2 = []
    for i1 in range(N1):
        v, l = map(int, input().split(' '))
        if i1 == 0:
            line1.append((l-1, v))
            continue
        line1.append((line1[-1][0] + l, v))
    for i2 in range(N2):
        v, l = map(int, input().split(' '))
        if i2 == 0:
            line2.append((l-1, v))
            continue
        line2.append((line2[-1][0] + l, v))
    
    res = 0
    for i, chunk in enumerate(line2):
        if i == 0:
            l2start = 0
        else:
            l2start = line2[i-1][0] + 1
        l2end = chunk[0]
        l2v = chunk[1]
        l1left = bisect_left(line1, l2start, key=lambda x: x[0])
        l1right = bisect_left(line1, l2end, key=lambda x: x[0])
        
        for target in range(l1left, l1right+1):
            if target == 0:
                l1start = 0
            else:
                l1start = line1[target-1][0] + 1
            l1end = line1[target][0]
            l1v = line1[target][1]            

            if l2v == l1v:
                res += (min(l1end, l2end) + 1 - max(l1start, l2start))

    print(res)

if __name__ == '__main__':
    main()