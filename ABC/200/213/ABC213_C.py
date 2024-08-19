#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    H, W, N = map(int, input().split(' '))
    AB = []
    # 出てきた行を管理する
    A_set, B_set = set(), set()
    for _ in range(N):
        a, b = map(int, input().split(' '))
        AB.append([a, b])
        A_set.add(a)
        B_set.add(b)
    # 単一要素のソートされた変換用リスト
    A_sort = {a:i+1 for i, a in enumerate(sorted(list(A_set)))}
    B_sort = {b:i+1 for i, b in enumerate(sorted(list(B_set)))}

    # 出力
    for a, b in AB:
        print(A_sort[a], B_sort[b])  
    
if __name__ == '__main__':
    main()