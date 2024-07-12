s = list(input())
t = list(input())

#dp
dp = [[0 for j in range(3010)] for i in range(3010)]

for i, vs in enumerate(s):
    for j, ts in enumerate(t):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

ans = []
i = len(s) - 1
j = len(t) - 1

while i >= 0 and j >= 0:
    if s[i] == t[j]:
        ans.append(s[i])
        i -= 1
        j -= 1
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    elif dp[i+1][j+1] == dp[i+1][j]:
        j -= 1

ans.reverse()
for i in ans:  
    print(i, end='') 
