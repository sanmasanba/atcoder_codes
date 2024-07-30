import sys
from collections import deque

sys.setrecursionlimit(10**6)
INF = float('inf')

def run_length_encoding(S):
    rle = []
    n = len(S)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and S[i] == S[i + 1]:
            i += 1
            count += 1
        rle.append((i + 1 - count, S[i], count))
        i += 1
    return rle

def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    
    rle = run_length_encoding(S)
    
    for l_q, r_q in queries:
        res = 0
        pos = 0
        while pos < len(rle) and rle[pos][0] + rle[pos][2] - 1 < l_q:
            pos += 1
        while pos < len(rle) and rle[pos][0] <= r_q:
            start = max(l_q, rle[pos][0])
            end = min(r_q, rle[pos][0] + rle[pos][2] - 1)
            if end - start + 1 > 1:
                res += end - start
            pos += 1
        print(res)

if __name__ == '__main__':
    main()
