#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')
def bfs(x:str, Ss:list, s:int, second:int, M:int):
    s1, s2 = (s+1)%3, (s+2)%3
    res = [0, 0]
    for s1_sec in range(second+1, 3*M):
        if Ss[s1][s1_sec] == x:
            for s2_sec in range(s1_sec+1, 3*M):
                if Ss[s2][s2_sec] == x:
                    res[1] = s2_sec
                    break
        if res[1]:
            break
    for s2_sec in range(second+1, 3*M):
        if Ss[s2][s2_sec] == x:
            for s1_sec in range(s2_sec+1, 3*M):
                if Ss[s1][s1_sec] == x:
                    res[0] = s1_sec
                    break
        if res[0]:
            break

    return min(res)

#main
def main():
    M = int(input())
    Ss = []
    for _ in range(3):
        tmp = list(input())*3
        Ss.append(tmp)

    # すべてに共通する数字がなければ、スロットはそろわない
    S_set = set(Ss[0]) & set(Ss[1]) & set(Ss[2])
    if not S_set:
        print(-1)
    else:
        res = INF
        # 重複する数字に関してシミュレート
        for x in S_set:
            for s in range(3):
                # いずれかは、M秒以内に選ばなければいけない
                for second in range(M):
                    # 最初に一致したところからbfs
                    if Ss[s][second] == x:
                        res = min(res, bfs(x, Ss, s, second, M))
        print(res)

if __name__ == '__main__':
    main()