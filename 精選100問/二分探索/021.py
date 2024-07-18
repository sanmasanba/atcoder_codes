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
    N = int(input())
    H, S = [], []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        H.append(a)
        S.append(b)

    # 最大と最小の設定
    low = min([H[i] for i in range(N)])
    high = max([H[i]+(N-1)*S[i] for i in range(N)])
    # 探索開始
    # lowとhighが一致するまで(一致した点が挿入する点)
    while high - low > 1:
        # 中間点の設定
        mid = (low + high) // 2
        # 判定
        flag = True
        t = [0 for i in range(N)]
        for i in range(N):
            # 目的の時間が、初期値より低いときは不可能
            if mid < H[i]:
                flag = False
                break
            # 制限時間を代入
            t[i] = (mid - H[i]) // S[i]
        # すべてが制限時間内に割れるか判定
        if flag:
            t.sort()
            for limit in range(N):
                if t[limit] < limit:
                    flag = False
                    break
        # 条件が満たされるとき、正解の高度はもっと下
        if flag:
            high = mid
        else:
            low = mid
    print(high) 

if __name__ == '__main__':
    main()