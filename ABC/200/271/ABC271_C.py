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
    A = list(map(int, input().split(' ')))
    # その巻を持っているか
    having = [False for _ in range(N+2)]    

    # 売っていい冊数を求める
    sold = 0
    for a in A:
        # 冊数は減少するので、いま持っている冊数より大きい巻数は読めないから売る
        if len(having) <= a: sold += 1
        # 1冊以上持っている場合は売る
        elif having[a]: sold += 1
        # 初めて見た巻は記録
        else: having[a] = True

    # シミュレーション
    l = 1   # 持っていない巻の最小
    r = N+1 # 持っている巻の最大
    while 1:
        # もっている巻はスルー
        while having[l]: l += 1
        # 持っていない巻はスルー
        while (r!=0 and not having[r]): r-= 1 
        # 売れる本が2冊以上あるとき
        if 2 <= sold:
            sold -= 2
            having[l] = True
        # ないとき
        else:
            # rを読まなければいけないとき、それ以上読み進められない
            if r <= l: break
            # 持っている最大の巻を売る
            having[r] = False
            sold += 1
    print(l-1)

if __name__ == '__main__':
    main()  