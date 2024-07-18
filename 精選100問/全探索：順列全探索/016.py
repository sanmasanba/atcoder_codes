#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N = int(input())
    P = tuple(map(int, input().split(' ')))
    Q = tuple(map(int, input().split(' ')))
    
    C = permutations([i+1 for i in range(N)], N)
    p_pos, q_pos = 0, 0
    for i, order in enumerate(C):
        if order == P:
            p_pos = i
        if order == Q:
            q_pos = i
    print(abs(p_pos-q_pos))

if __name__ == '__main__':
    main()