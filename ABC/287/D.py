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
def check(s, t):
    for s_cha, t_cha in zip(s, t):
        if s_cha != t_cha and (s_cha != '?' and t_cha != '?'):
            return False
    return True

#main
def main():
    S = list(input())
    T = list(input())
    S_length = len(S)
    T_length = len(T)

    # 先頭からどこまで一致するかを調べる
    s1 = [False] * (T_length+1)
    s1[0] = True
    for i in range(T_length):
        if S[i] == T[i] or S[i] == '?' or T[i] == '?':
            s1[i+1] = True
        else:
            break
    # 末尾からの一致を調べる
    s2 = [False] * (T_length+1)
    s2[-1] = True
    for i in range(T_length):
        if S[-(i+1)] == T[-(i+1)] or S[-(i+1)] == '?' or T[-(i+1)] == '?':
            s2[-(i+2)] = True
        else:
            break
    
    for i, j in zip(s1, s2):
        print('Yes' if i and j else 'No')
        
if __name__ == '__main__':
    main()