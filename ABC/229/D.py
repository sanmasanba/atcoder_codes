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
    S = input()
    K = int(input())
    S_len = len(S)
    counter = Counter(S)
    # 一つも'.'がないとき、長さがそのまま答え
    if '.' not in counter:
        print(counter['X'])
        return
    # '.'しかないときに、全部置き換える
    if 'X' not in counter:
        print(min(counter['.'], K))
        return
    if K == 0:
        print(max(list(map(lambda x:len(x), list(S.split('.'))))))
        return

    right = 0
    res = 0
    dots = 1 if (S[0] == '.' and 0 < K) else 0
    for left in range(S_len):
        while right+1 < S_len and (S[right+1] == 'X' or (S[right+1] == '.' and dots+1 <= K)):
            right += 1
            if S[right] == '.':
                dots += 1
        if dots <= K:
            res = max(res, right - left + 1)
        if S[left] == '.':
            dots -= 1
        if left == right and right+1 < S_len:
            right += 1
            if S[right] == '.':
                dots += 1

    print(res)


if __name__ == '__main__':
    main()