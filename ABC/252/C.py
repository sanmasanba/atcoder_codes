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
    N = int(input())
    S = []
    for _ in range(N):
        tmp = input()
        S.append(tmp)
    
    # j文字目の出目がkであるものを数える
    cnt = [[0 for j in range(10)] for k in range(10)]
    for n in range(N):
        for j in range(10):
            cnt[int(S[n][j])][j] = cnt[int(S[n][j])][j] + 1

    mx = [0 for _ in range(10)]
    for k in range(10):
        # 文字kに関して
        for j in range(10):
            # j文字目が重なっているとき、tは、重なっている文字数cntとして
            # t < 10*(cnt-1)+1　になる。
            # (２個重なっているときは、次の周期で何とかできる)
            mx[k] = max(mx[k], 10*(cnt[k][j]-1)+j)
    print(min(mx))

if __name__ == '__main__':
    main()