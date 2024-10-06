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
    # 入力
    N, M, X = map(int, input().split(' '))
    C, A = [], []
    for _ in range(N):
        c, *a = list(map(int, input().split(' ')))
        C.append(c)
        A.append(a)

    # bit全探索
    res = INF
    for buyed_books in range(2**N):
        cost = 0
        understandings = [0] * M
        for book_num in range(N):
            if buyed_books >> book_num & 1:
                cost += C[book_num]
                for knowledge_num in range(M):
                    understandings[knowledge_num] += A[book_num][knowledge_num]
        if all([X <= understanding for understanding in understandings]):
            res = min(res, cost)

    # 出力
    print(res if res != INF else -1)

if __name__ == '__main__':
    main()