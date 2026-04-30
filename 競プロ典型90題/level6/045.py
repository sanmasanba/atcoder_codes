#main
def main():
    # intput
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    
    # それぞれの点についてあらかじめ計算
    dist = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            # i->jを計算して、j->iに再利用
            dist[i][j] = (XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2
            dist[j][i] = dist[i][j]

    # 各状態ごとに最大距離を求めておく
    cost = [0] * (1 << N)
    for bit in range(1, 1<<N):
        for i in range(1, N):
            # 選ばれていない点からの計算はスキップ
            if (bit >> i) & 1 == 0:
                continue
            for j in range(i):
                if (bit >> j) & 1 == 1:
                    cost[bit] = max(cost[bit], dist[i][j])

    # dp[i][bit] := bitで表される点を選んで、現在のグループ数がiのときの最小値
    INF = 10**18
    dp = [[INF]*(1<<N) for _ in range(K+1)]
    dp[0][0] = 0
    # 現在のグループ数
    for i in range(1, K+1):
        # 点の集合
        for bit1 in range(1, 1<<N):
            # bit2はbit1の部分集合
            bit2 = bit1
            while bit2 != 0:
                # 現在の集合bit1を
                # bit1-bit2の集合とbit2の集合に分ける
                dp[i][bit1] = min(dp[i][bit1], 
                                  max(dp[i-1][bit1-bit2], cost[bit2]))
                # bit2を1ずつ下げていって、部分集合を全列挙
                bit2 = (bit2-1) & bit1
    print(dp[K][(1<<N)-1])

if __name__ == '__main__':
    main()