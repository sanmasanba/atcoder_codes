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
    N, D, P = map(int, input().split(' '))
    F = list(map(int, input().split(' ')))
    # passの一日あたりの料金以上でないと、passを使う意味はない
    exceed_cnt = 0
    # 平均以上の日の数を数える
    for f in F:
        if P <= f*D: exceed_cnt += 1
    # パスの枚数の暫定の数
    passes = ceil(exceed_cnt/D)
    # Fを大きい順にする
    F.sort()
    # 1日も買う必要がないとき
    if exceed_cnt == 0:
        print(sum(F))
    # １枚以上のパスを買った場合
    else:
        # 大きいほうから、残り１枚までパスに置き換えていく
        for _ in range(passes-1):
            for _ in range(D):
                F.pop()
        # 少なくともP*(passes-1)円は確定
        if D < len(F):
            tmp1 = sum(F[-D:])  # パスで置き換わる可能性のある日
            tmp2 = sum(F[:-D])  # 置き換わることのない日
            # 置き換わる可能性のある日の料金とパスで比較
            print(P*(passes-1) + tmp2 + (tmp1 if tmp1 < P else P))
        else:
            tmp = sum(F)
            # 残りの日とパスで比較
            print(P*(passes-1) + (tmp if tmp < P else P))

if __name__ == '__main__':
    main()