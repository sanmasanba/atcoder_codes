#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N = int(input())
    Q = [list(map(int, input().split(' '))) for _ in range(N)]
    
    for i in range(N):
        tmp = 0
        res = 0
        for j in range(N):
            if i == j:
                pass
            else:
                dis2 = (Q[i][0]-Q[j][0])**2+(Q[i][1]-Q[j][1])**2
                # print(dis2)
                res = j+1 if tmp < dis2 else res
                tmp = max(tmp, dis2)
        print(res)

if __name__ == '__main__':
    main()