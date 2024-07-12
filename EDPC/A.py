#二つを比較して、小さいほうを返す
def chmin(a, b):
    return a if a <= b else b

INF = 1e10
#input
N = int(input())
hs = list(map(int, input().split(' '))) + [INF, INF, INF, INF, INF, INF, INF, INF]
#dpの初期化
dp = [INF for _ in range(N + 10)]
dp[0] = 0

#現在の総コスト(dp[i])と移動前＋コストを比較する
for i in range(1, N):
    #現在のdp[i]とdp[i - 1]+costを比較する
    dp[i] = chmin(dp[i], dp[i - 1] + abs(hs[i] - hs[i - 1]))
    #現在のdp[i]とdp[i - 2]+costを比較する
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(hs[i] - hs[i - 2]))

#print(dp)
print(dp[N - 1])
