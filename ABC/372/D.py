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
    H = list(map(int, input().split(' ')))
    
    H.reverse()
    stack = []
    res = [0] * N
    for i in range(N-1):
        while stack:
            if stack[-1] < H[i]:
                stack.pop()
            else:
                break
        stack.append(H[i])
        res[i+1] = len(stack)
    
    # output
    print(*reversed(res))

if __name__ == '__main__':
    main()