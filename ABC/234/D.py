#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
import heapq
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

# ライブラリはここに貼り付け

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    P = list(map(int, input().split(' ')))
    # キューの初期化
    que = P[0:K]
    # 最初は、必ず最も小さい値が答え
    print(min(que))
    # 優先度付きキューに変換
    heapq.heapify(que)
    for i in range(K, N):
        # 最小値を取り出す
        kth_min = heapq.heappop(que)
        # 現在の最小値と追加する要素で比較
        kth_min = max(kth_min, P[i])
        # 現在の最小値より、大きい値を追加するとき、キューが更新される
        heapq.heappush(que, kth_min)
        kth_min = heapq.heappop(que)
        print(kth_min)
        heapq.heappush(que, kth_min)

if __name__ == '__main__':
    main()