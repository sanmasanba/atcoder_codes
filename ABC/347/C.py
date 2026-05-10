#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache

sys.setrecursionlimit(500000)
INF = float('inf')

#main
def main():
    N, A, B = map(int, input().split(' '))
    tmp = list(map(lambda x: int(x)%(A+B), input().split(' ')))
    D = sorted((tmp))

    # 循環列にして考える
    for i in range(len(D)):
        D += [D[i]+A+B]
    
    res = False
    for i in range(N):
        # i日目を基準として、A日後がいつになるかを考えて
        # 挿入位置を求める
        pos = bisect_left(D, D[i]+A)
        # i日目と、求めたpos日目の間にN日あれば、
        # すべて休日に収められる
        res |= (pos-i == N)

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()