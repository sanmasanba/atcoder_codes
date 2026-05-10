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
    H, W = map(int, input().split(' '))
    si, sj = map(lambda x: int(x)-1, input().split(' '))
    Q = [list(input()) for _ in range(H)]
    S = list(input())
    
    move = {"L":[0, -1] , "U":[-1, 0], "R":[0, 1], "D":[1, 0]}
    pos = [si, sj]
    for s in S:
        tmp_pos = [pos[0]+move[s][0], pos[1]+move[s][1]]
        if 0 <= tmp_pos[0] <= H-1 and 0 <= tmp_pos[1] <= W-1 and Q[tmp_pos[0]][tmp_pos[1]] == ".":
            pos = tmp_pos
        else:
            pass
        
    print(*list(map(lambda x: x+1, pos)))

if __name__ == '__main__':
    main()