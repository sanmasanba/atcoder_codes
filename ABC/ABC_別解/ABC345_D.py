#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
from heapq import heappush, heappop
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache, cmp_to_key, reduce
from itertools import permutations, combinations, accumulate
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable
T = TypeVar('T')

sys.setrecursionlimit(10**6)
INF = float('inf')

def func(a, b, W):
    # a*(W+1)bitのブロックを宣言
    tmp = (1 << a*W) - 1
    # 幅Wの１列(1 << W - 1)で割って、a * Wの形状に変換
    # 11111111//111 -> 00010001 (番兵だけ残して展開)
    tmp //= (1 << W) - 1
    # 幅bになるように宣言してかけ合わせる
    # 00010001 * 111 = 01110111
    # -> 0111 
    #    0111
    # -> a * bのブロック表現に変換されている
    return tmp * ((1 << b) - 1)
    

def preprocess(W):        
    a, b = map(int, input().split(' '))
    return (func(a, b, W), func(b, a, W))

def solve(grid, blocks):
    global X
    # 埋まり切ったら1
    if not grid: return 1
    
    # girdのうち、最右の1であるbitを取り出してその分シフト
    # grid = 1010
    # gird & -grid = 1010 & 0110 = 0010 
    # 1010 // 0010 = 101
    grid //= grid & -grid
    
    # 全探索
    for i in range(len(blocks)):
        # 順転と反転を試す
        for x in X[blocks[i]]:
            #　設置可能なら不変のはず
            # 111 & 11 = 11 -> ok
            # 101 & 11 = 01 -> bad
            # 上記を確かめながら再帰
            # grid ^ x 
            # -> 1111 ^ 11 = 1100 -> 設置に対応
            if grid & x == x and solve(grid ^ x, blocks[:i] + blocks[i+1:]):
                # うまく置ければ1
                return 1
    return 0
#main
def main():
    # intput
    N, H, W = map(int, input().split(' '))
    # 盤面の右端に番兵を設置
    W += 1    
    # 盤面を展開
    grid = func(H, W-1, W)
    # blockを受けとる
    global X
    X = [preprocess(W) for i in range(N)]    

    # シミュレーション
    res = solve(grid, list(range(N)))
    # output
    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()