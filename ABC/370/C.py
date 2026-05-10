#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations
import copy

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    S = list(input())
    T = list(input())
    res_set = set()
    res = []

    N = len(S)
    for _ in range(N):
        tmp_list = []
        for i in range(N):
            if S[i] != T[i]:
                tmp = copy.copy(S)
                tmp[i] = T[i]
                tmp_list.append(tmp)
        if not tmp_list:
            break 
        tmp_list.sort()
        S = tmp_list[0]
        s = "".join(S)
        if s not in res_set:
            res_set.add(s)
            res.append(s)
    
    res = list(res)
    cnt = len(res)
    if cnt == 0:
        print(0)
    else:
        print(cnt)
        print(*res, sep='\n')


if __name__ == '__main__':
    main()