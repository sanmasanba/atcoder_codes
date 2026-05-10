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
    A = []
    row_A = [set() for _ in range(9)]
    col_A = [set() for _ in range(9)]
    res = 'Yes'
    for i in range(9):
        tmp_a = list(input().split(' '))
        A.append(tmp_a)
        # 集合を取ると、要素は9種類にならないといけない
        if len(set(tmp_a)) != 9:
            res = 'No'        
        row_A[i] = set(tmp_a)
        for j, a in enumerate(tmp_a):
            col_A[j].add(a)
    # 各列の集合も9種類
    for a_r in row_A:
        if len(a_r) != 9:
            res = 'No'
    # 各行の集合も9種類
    for a_c in col_A:
        if len(a_c) != 9:
            res = 'No'

    # それぞれのブロックの集合も9種類
    tmpsum = [[set() for j in range(3)] for i in range(3)]
    for h in range(9):
        for w in range(9):
            tmpsum[h//3][w//3].add(A[h][w])
    for h in range(3):
        for w in range(3):
            if len(tmpsum[h][w]) != 9:
                res = 'No'

    print(res)
    
if __name__ == '__main__':
    main()