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
    N, M = map(int, input().split(' '))
    KSs = [list(map(lambda x: int(x)-1, input().split(' ')))[1:] for _ in range(M)]
    P = list(map(int, input().split(' ')))
    
    #bit_search
    res = 0
    # ついているスイッチを全探索
    for i in range(2**N):
        flag = True
        # それぞれの電球について
        for j, m in enumerate(KSs):
            cnt = 0
            # 電球についているスイッチがついているか
            for k in m:
                if (i >> k) & 1:
                    cnt += 1
            # 今のスイッチが点灯の条件をみたしているか
            if cnt%2 != P[j]:
                flag = False
                break
        # カウント
        if flag:
            res += 1

    print(res)

if __name__ == '__main__':
    main()