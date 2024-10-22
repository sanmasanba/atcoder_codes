#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations, accumulate

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353

#main
def main():
    # input
    Q = int(input())
    nums = 1
    queue = deque()
    queue.append(1)
    for _ in range(Q):
        S = input()
        if S.startswith('1'):
            _, x = map(int, S.split(' '))
            queue.append(x)
            nums = (10*nums + x)%MOD
        elif S.startswith('2'):
            x = queue.popleft()
            nums = (nums - x * pow(10, len(queue), MOD)) % MOD
        elif S.startswith('3'):
            print(nums)

if __name__ == '__main__':
    main()