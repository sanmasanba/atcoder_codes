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
    N = int(input())
    A = list(map(int, input().split(' ')))
    Q = int(input())
    Query = [list(map(int, input().split(' '))) for _ in range(Q)]
    
    # 最後にリセットされたときの値を覚えておく
    last_reset = None
    # リセットからの増分のみ覚えておく
    add_dict = {}
    for query in Query:
        if query[0] == 1:
            _, x = query
            # リセット
            last_reset = x
            add_dict = {}
        elif query[0] == 2:
            _, i, x = query
            # 増分管理
            if i-1 not in add_dict:
                add_dict[i-1] = 0
            add_dict[i-1] += x
        else:
            _, i = query
            # リセット入ったどうかで分岐
            if last_reset == None:
                print(A[i-1] + (add_dict[i-1] if i-1 in add_dict else 0))
            else:
                print(last_reset + (add_dict[i-1] if i-1 in add_dict else 0))

if __name__ == '__main__':
    main()