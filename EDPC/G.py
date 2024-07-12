import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split(' '))
G = [[] for _ in range(100100)]
dp = [-1 for _ in range(100100)]

#メモ化再帰
def solve(u):
    #開始地点の長さを0にして、
    if dp[u] == -1:
        dp[u] = 0
        #u番目のノードから探索したときに、v番目のノードに行く場合
        for v in G[u]:
            #現在の最大経路長とv番目の経路長(+１)の比較
            dp[u] = max(dp[u], solve(v) + 1)
    return dp[u]

#入力をリストに収納
for _ in range(M):
    x, y = map(int, input().split(' '))
    #x番目のノードから、y番目に行くことを記すリストを作成
    G[x-1].append(y-1)

res = -1

#i番目の要素から探索開始
for i in range(N):
    #今の最長経路とiから始めた時の経路長の比較
    res = max(res, solve(i))

print(res)