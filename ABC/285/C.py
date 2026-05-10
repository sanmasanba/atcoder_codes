#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations
from string import ascii_uppercase

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    S = list(input())
    # 26進数に変換
    c2i = {c:i+1 for i, c in enumerate(ascii_uppercase)}

    res = 0
    order = 0
    while S:
        s = S.pop()
        res += c2i[s]*26**order
        order += 1
    print(res)

if __name__ == '__main__':
    main()