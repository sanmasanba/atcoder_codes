#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import re
import sys
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')
T = TypeVar('T')
MOD998244353 = 998244353
MOD1000000007 = 1000000007

#main
def main():
    # intput
    N, K = map(int, input().split())
    S = ['.'] + list(input().strip()) + ['.']
    for i in range(1, N+1):
        if S[i] == '?' and (S[i-1] == 'o' or S[i+1] == 'o'):
            S[i] = '.'

    o_cnt = sum([1 if S[i] == 'o' else 0 for i in range(1, N+1)])
    # 'o'がK個含まれている　→　残りの？は全て'.'
    if o_cnt == K:
        for s in S[1:-1]:
            if s == 'o':
                print('o', end='')
            else:
                print('.', end='')
    else:
        # 貪欲法で置き換えてみる
        max_o_cnt = 0
        pre = 0
        for i in range(1, N+1):
            if S[i] == 'o': 
                pre = 1
                max_o_cnt += 1
            elif S[i] == '.':
                pre = 0
            elif S[i] == '?':
                if pre == 0 and S[i-1] != 'o' and S[i+1] != 'o':
                    pre = 1
                    max_o_cnt += 1
                else:
                    pre = 0
        # 貪欲解でK個になる場合
        if max_o_cnt == K:
            tmp = 0
            for s in S[1:-1]:
                if s != '?':
                    # ？が連続して奇数個の時、'o.o.o.o'のようになる
                    if tmp%2:
                        for i in range(tmp): 
                            print('.', end='') if i%2 else print('o', end='')
                    # 偶数なら'o.o.' or '.o.o' -> '????'
                    else:
                        print('?'*tmp, end='')
                    print(s, end='')
                    tmp = 0
                else:
                    tmp += 1
            if tmp%2:
                for i in range(tmp): 
                    print('.', end='') if i%2 else print('o', end='')
            else:
                print('?'*tmp, end='')
        elif K < max_o_cnt:
            print(''.join(S[1:-1]))

if __name__ == '__main__':
    main()