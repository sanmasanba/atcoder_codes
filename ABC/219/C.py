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
    X = input()
    N = int(input())
    # 新しい辞書を作成
    c2n = {c:i for i, c in enumerate(X)}
    n2c = {i:c for i, c in enumerate(X)}

    S = []
    for _ in range(N):
        # 文字を数値に変換
        input_c = list(input())
        input_c = list(map(lambda x: int(c2n[x]), input_c))
        S.append(input_c)
    S.sort()

    # 出力
    for s in S:
        s = ''.join(list(map(lambda x:n2c[x], s)))
        print(s)

if __name__ == '__main__':
    main()