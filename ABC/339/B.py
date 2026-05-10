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
    H, W, N = map(int, input().split(' '))
    MAP = [['.' for j in range(W)] for i in range(H)]
    pos = [0, 0]
    move = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    vec = 0
    # print(MAP)
    for _ in range(N):
        # print(pos)
        if MAP[pos[0]][pos[1]] == '.':
            MAP[pos[0]][pos[1]] = '#'
            vec = (vec+1)%4
            pos[0], pos[1] = (pos [0]+ move[vec][0])%H, (pos[1] + move[vec][1])%W
        else:
            MAP[pos[0]][pos[1]] = '.'
            vec = (vec-1)%4
            pos[0], pos[1] = (pos [0]+ move[vec][0])%H, (pos[1] + move[vec][1])%W
        
    for i in MAP:
        for j in i:
            print(j, end='')
        print('') 

if __name__ == '__main__':
    main()