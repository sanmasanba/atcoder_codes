#input
N = int(input())
actions = [list(map(int, input().split(' '))) for _ in range(N)]

#dpの初期化
dp = [[0 for j in range(3)] for i in range(N + 10)]

#chmax
def chmax(a, b):
    return a if a >= b else b

#i日目
for i in range(N):
    #昨日の選択j
    for j in range(3):
        #今日の選択k
        for k in range(3):
            #二日連続にならないように
            if j != k:
                #chmax(今のところの最適解, 選択した行動の結果)
                dp[i + 1][k] = chmax(dp[i + 1][k], dp[i][j] + actions[i][k])

ans = 0
for tmp in dp[N]:
    ans = chmax(ans, tmp) 

print(ans)
