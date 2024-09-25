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
    N, Q = map(int, input().split(' '))
    S = list(input())
    str_dict = {}
    for i in range(N-2):
        s = ''.join(S[i:i+3])
        if s not in str_dict:
            str_dict[s] = 0
        str_dict[s] += 1
    res = []
    for _ in range(Q):
        x, c = input().split(' ')
        x = int(x)-1
        if 0 <= x-2 and x < N:
            str_dict[''.join(S[x-2:x+1])] -= 1
        if 0 <= x-1 and x+1 <N:
            str_dict[''.join(S[x-1:x+2])] -= 1
        if  0 <= x and x+2 < N:
            str_dict[''.join(S[x:x+3])] -= 1
        S[x] = c
        if 0 <= x-2 and x < N:
            s = ''.join(S[x-2:x+1])
            if s not in str_dict:
                str_dict[s] = 0
            str_dict[s] += 1
        
        if 0 <= x-1 and x+1 < N:
            s = ''.join(S[x-1:x+2])
            if s not in str_dict:
                str_dict[s] = 0
            str_dict[s] += 1
        if  0 <= x and x+2 < N:
            s = ''.join(S[x:x+3])
            if s not in str_dict:
                str_dict[s] = 0
            str_dict[s] += 1
        res.append(str_dict["ABC"] if "ABC" in str_dict else 0)
    print(*res, sep='\n')

if __name__ == '__main__':
    main()