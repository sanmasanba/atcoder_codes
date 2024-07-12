#定数
INF = 1e10

#chmin
def chmin(a, b):
    return a if a <= b else b

#input
N, K = map(int, input().split(' '))
hs = list(map(int, input().split(' '))) + [INF, INF, INF, INF, INF, INF, INF, INF]

#dpの初期化
dp = [INF for _ in range(N + 10)]
dp[0] = 0

for i in range(1, N):
    for k in range(1, K + 1):
        if k <= i:
            dp[i] = chmin(dp[i], dp[i - k] + abs(hs[i] - hs[i - k]))

print(dp[N - 1])