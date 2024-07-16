#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
import copy 

sys.setrecursionlimit(10**6)
INF = float('inf')

# main
def main():
    N, M = map(int, input().split(' '))
    Q = [list(map(int, input().split(' '))) for _ in range(N)]
    
    res = 0
    # bit探索で行だけ返すことを考える
    for i in range(2**N):
        tmp = 0
        q = copy.copy(Q)
        for j in range(N):
            if (i >> j) & 1:
                q[j] = list(map(lambda x: x ^ 1, q[j]))
        # 各列について
        for m in range(M):
            num = 0
            # 各列ごとの0(裏が焼けるもの)の数を数える
            for n in range(N):
                if q[n][m] == 0:
                    num += 1
            # もし、0(裏を焼きたいもの)のほうが多いなら返さない。→0の数が最大枚数
            # 1のほうが多いなら返す。→1の数が最大枚数
            tmp += max(N-num, num)
        res = max(res, tmp)
    print(res)

if __name__ == '__main__':
    main()