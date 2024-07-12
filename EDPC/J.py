c = [0 for _ in range(4)]
dp = [[[-1 for k in range(310)] for j in range(310)] for i in range(310)]
N = int(input())
p = list(map(int, input().split(' ')))

def solve(c1, c2, c3):
    if c1 == 0 and c2 == 0 and c3 == 0:
        return 0.0
    if dp[c1][c2][c3] > 0:
        return dp[c1][c2][c3]
    
    #答えは、絶対にNを下回らない
    res = N
    if c1 >= 1:
        res += solve(c1-1, c2, c3) * c1
    if c2 >= 1:
        res += solve(c1+1, c2-1, c3) * c2
    if c3 >= 1:
        res += solve(c1, c2+1, c3-1) * c3
    res /= (c1 + c2 + c3)
    dp[c1][c2][c3] = res
    return dp[c1][c2][c3]

def main():
    for i in p:
        c[i] += 1
    
    ans = solve(c[1], c[2], c[3])

    print(f"{ans:.10f}")

if __name__ == '__main__':
    main()