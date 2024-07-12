N = int(input())
p = list(map(float, input().split(' ')))
dp = [[0 for _ in range(N+10)] for _ in range(N+10)]

def main():
    dp[0][0] = 1
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j+1] += dp[i][j] * p[i]
            dp[i+1][j] += dp[i][j] * (1 - p[i])

    res = 0.0

    i = int((N+1)/2)
    while i <= N:    
        res += dp[N][i]
        i += 1

    print(res)

if __name__ == '__main__':
    main()