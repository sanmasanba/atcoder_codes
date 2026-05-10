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
    s2pos = defaultdict(list)
    for i, s in enumerate(S):
        s2pos[s].append(i)
    
    res = 0
    for _, pos_list in s2pos.items():
        list_length = len(pos_list)
        cumsum = [0]
        for p in pos_list:
            cumsum.append(cumsum[-1]+p)
        for i in range(list_length-1):
                res += cumsum[-1]-cumsum[i+1] - (list_length-(i+1))*(pos_list[i]+1)
        
    print(res)

if __name__ == '__main__':
    main()