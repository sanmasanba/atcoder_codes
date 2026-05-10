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
    N, X, Y, Z = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    AB = []
    for i in range(1, N+1):
        AB.append([i, A[i-1], B[i-1]])
    # 全体を　数学の点が高い順にソート
    AB.sort(key=lambda x: (-x[1], x[0]))
    # 順位が確定した人以降を、英語の点でソート
    AB[X:] = sorted(AB[X:], key = lambda x: (-x[2], x[0]))
    # 合計点でソート
    AB[X+Y:] = sorted(AB[X+Y:], key = lambda x: (-(x[1]+x[2]), x[0]))
    # 合格となった人を昇順にソート
    AB[:X+Y+Z] = sorted(AB[:X+Y+Z], key = lambda x: x[0])

    for x in AB[:X+Y+Z]:
        print(x[0])
    
if __name__ == '__main__':
    main()