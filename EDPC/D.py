#input
N, W = map(int, input().split(' '))
weight = [0] * 110
value = [0] * 110
for i in range(N):
    weight[i], value[i] = map(int, input().split())

#最大化なので、初期化は0
dp = [[0 for j in range(W + 1)] for i in range(N + 1)]

#i個めの荷物
for i in range(N):
    #荷物の総重量
    for sum_w in range(W + 1):
        if sum_w - weight[i] >= 0:
            #i番目の荷物を選ぶ
            #今の選んだ場合の価値と更新された価値の比較
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w - weight[i]] + value[i])
        #i番目の荷物を選ばない
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

print((dp[N][W]))