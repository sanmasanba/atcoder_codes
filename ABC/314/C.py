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
    N, M = map(int, input().split(' '))
    S = list(input())
    C = list(map(int, input().split(' ')))
    c_dict = {}
    for i in range(N):
        if C[i] not in c_dict:
            c_dict[C[i]] = deque()
        c_dict[C[i]].append(S[i])
    for _, v in c_dict.items():
        tmp_c = v.pop()
        v.appendleft(tmp_c)
    for c in C:
        print_char = c_dict[c].popleft()
        print(print_char, end='')

if __name__ == '__main__':
    main()