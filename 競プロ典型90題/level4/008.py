def main():
    N = int(input())
    S = list(input())
    MOD = 1000000007

    seq = 'atcoder'

    #dp
    dp = [[0 for j in range(len(seq)+1)] for i in range(N+1)]

    #初期値は0
    dp[0][0] = 1
    for i in range(N):
        for j in range(len(seq)+1):
            #選ばないときは、次の文字の場合の総数に足す
            dp[i+1][j] += dp[i][j] % MOD
            #もし選ぶなら、選んで次に行くので右下に足す
            if j < 7 and S[i] == seq[j]:
                dp[i+1][j+1] += dp[i][j] % MOD

    print(dp[N][len(seq)] % MOD)

if __name__ == '__main__':
    main()