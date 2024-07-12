#input
INF = 1e20
N, W = map(int, input().split(' '))
weight = [0] * 110
value = [0] * 110
for i in range(N):
    weight[i], value[i] = map(int, input().split())

#最小化なので、初期化はINF
dp = [[INF for j in range(100100)] for i in range(110)]
#荷物がないから、幸福度がゼロになる
dp[0][0] = 0

#i番目の荷物
for i in range(N):
    #価値の総量
    for sum_v in range(100100):
        if sum_v - value[i] >= 0:
            #荷物を選んだ場合
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v - value[i]] + weight[i])
        #選ばなかった場合
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])

ans = 0
for sum_v in range(100100):
    ans = sum_v if dp[N][sum_v] <= W else ans
print(ans)