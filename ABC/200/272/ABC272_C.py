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
    N = int(input())
    A = list(map(int, input().split(' ')))
    
    # oddとevenで振り分けて、ソート
    odds, evens = [], []
    for a in A:
        if a%2:
            odds.append(a)
        else:
            evens.append(a)
    odds.sort()
    evens.sort()

    # どっちも要素が1個以下なら、達成不可
    if len(odds) < 2 and len(evens) < 2:
        print(-1)
    # 比較
    else:
        print(max(sum(odds[-2:]), sum(evens[-2:])))

if __name__ == '__main__':
    main()