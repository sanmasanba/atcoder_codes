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
    As = []
    for _ in range(N):
        A = list(input())
        As.append(A)
    
    new_A = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            switchx = (N//2-1 - j if j < N//2 else j - N//2) + 1
            switchy = (N//2-1 - i if i < N//2 else i - N//2) + 1
            switch = (N//2- max(switchx, switchy))%4
            match switch:
                case 0:
                    new_A[j][N-1-i] = As[i][j]
                case 1:
                    new_A[N-1-i][N-1-j] = As[i][j]
                case 2:
                    new_A[N-1-j][i] = As[i][j]
                case 3:
                    new_A[i][j] = As[i][j]
    
    for a in new_A:
        print(*a, sep='', flush=True)

if __name__ == '__main__':
    main()