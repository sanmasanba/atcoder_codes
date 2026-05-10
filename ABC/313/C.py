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
    N = int(input())
    A = list(map(int, input().split(' ')))
    ### 1.最大と最小の差が1以下となるBを仮定する
    A.sort()
    # sum(A) = N*p + (N-r)*(p+1)であるため
    # 変換後の数列Bは、N個のpとN-r個のp+1からなるといえる
    p, r = sum(A)//N, sum(A)%N
    B = []
    # Aの小さいほうからpを割り当てて、残りをp+1とする
    for i in range(N):
        if i < N-r:
            B.append(p)
        else:
            B.append(p+1)
    
    ### 2. 求められたBより操作回数を求める
    res = 0
    # すべての0≦j≦Nに対する|A_j - B_j|の総和をSとしたとき、操作によって
    # Sは2減少する。したがって、Sを0にするには、少なくともS//2の操作が必要
    # ー＞最適な操作ではS//2で操作が可能である。
    for i in range(N):
        res += abs(A[i]-B[i])
    print(res//2)
    
if __name__ == '__main__':
    main()