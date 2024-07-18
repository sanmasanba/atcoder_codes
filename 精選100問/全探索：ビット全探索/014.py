#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations
import copy

sys.setrecursionlimit(10**6)
INF = float('inf')

#main
def main():
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    
    # 建物の高さの組み合わせをすべて試す(2**15=32768)
    res = INF
    for bit in range(2**N): 
        tmp = set()
        A_copy = copy.copy(A)
        # bitが立っている建物だけを増設する
        for i in range(N):  
            if (bit >> i) & 1: tmp.add(i)
        tmp_max = A_copy[0]  # i番目の建物までで、最も高い建物の高さ 
        tmp_res = 0     # この手法でかかったコスト
        for ai in range(N):
            # ai番目の建物がまだ隠れているとき
            if tmp_max >= A_copy[ai] and (ai in tmp): 
                tmp_res += tmp_max - A_copy[ai] + 1
                A_copy[ai] = tmp_max + 1
            tmp_max = max(A_copy[:ai+1])
        # 建物が条件を満たしているかを調べる
        tmp_max = A_copy[0]
        cnt = 1
        for i in A_copy[1:]:
            if tmp_max < i:
                cnt += 1
                tmp_max = i
        if cnt >= K: res = min(res, tmp_res)
    print(res)

if __name__ == '__main__':
    main()