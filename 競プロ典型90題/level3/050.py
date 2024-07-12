def main():
    N, L = map(int, input().split(' '))

    dp = [0 for _ in range(N+10)]
    dp[0] = 1

    for i in range(1, N+1):
        if i < L:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-L]

    print(dp[N] % 1000000007)

if __name__ == '__main__':
    main()