#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
import statistics

sys.setrecursionlimit(10**6)
INF = float('inf')

def func(ent, exi, A, B):
    tmp = 0
    for i in range(len(A)):
        tmp += abs(ent-A[i])
        tmp += abs(A[i]-B[i])
        tmp += abs(B[i]-exi)
    return tmp

#main
def main():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        A.append(a)
        B.append(b)

    res = INF
    ent_exi = A+B
    # 入口と出口は、AとBのいずれかになるのでそれらで全探索
    for ent in ent_exi:
        tmp = 0
        for exi in ent_exi:
            res = min(res, func(ent, exi, A, B))

    print(res)
    
if __name__ == '__main__':
    main()