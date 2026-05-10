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
    L = list(map(int, input().split(' ')))
    
    # 少なくとも最も長い単語よりは長いウィンドウ幅
    low = max(L)
    # 上限は、すべての単語を1行に収められる幅
    high = sum(L)+len(L)

    while low <= high:
        # 仮の横幅の上限
        mid = (low+high)//2

        # 仮の上限で、何行になるか
        rows = 1
        tmp = 0
        for l in L:
            # 文頭はそのまま挿入
            if tmp == 0:
                tmp += l
            # 上限を超えないなら足す
            elif tmp+l+1 <= mid:
                tmp += l+1
            # 上限を超えるときは改行する
            elif mid < tmp+l+1:
                tmp = l
                rows += 1
        if M < rows:
            low = mid+1
        else:
            high = mid-1
    print(low)

if __name__ == '__main__':
    main()