#library
from collections import deque, Counter, defaultdict
import sys

# setting
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 1 << 32

def is_out_of_range(x:int, y:int, Xmi:int, Xma:int, Ymi:int, Yma:int) -> bool:
    return not (Xmi <= x < Xma and Ymi <= y < Yma)

#main
def main():
    # intput
    H, W = map(int, input().split())
    dist = [[INF]*W for _ in range(H)]
    que = deque()
    S = []
    for i in range(H):
        s = list(input().strip())
        for j, c in enumerate(s):
            if c == 'E':
                dist[i][j] = 0
                que.append((i, j))
        S.append(s)

    d = [[-1, 0, 'v'], [1, 0, '^'], [0, -1, '>'], [0, 1, '<']]
    while que:
        i, j = que.popleft()

        for di, dj, c in d:
            if (is_out_of_range(i+di, j+dj, 0, H, 0, W) or 
                dist[i+di][j+dj] != INF): continue
            if S[i+di][j+dj] == '#': continue

            dist[i+di][j+dj] = dist[i][j] + 1
            S[i+di][j+dj] = c
            que.append((i+di, j+dj))
    
    for s in S:
        print(''.join(s))

if __name__ == '__main__':
    main()