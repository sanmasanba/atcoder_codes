import sys

H, W = map(int, input().split(' '))
Cs = [list(str(input())) for h in range(H)]

N = min(H, W)
Sn = [0 for _ in range(N)]
ans = [0 for _ in range(N)]

cnt = 0
for i in range(1, H):
    #print(i)
    for  j in range(1, W-1):
        if Cs[i][j] == '#' and Cs[i-1][j-1] == '#' and Cs[i-1][j+1] == '#' and Cs[i+1][j-1] == '#' and Cs[i+1][j+1] == '#':
            cnt = 0
            while i > cnt and j > cnt:
                if Cs[i-cnt-1][j-cnt-1] == '#':
                    cnt += 1
                else:
                    break
            ans[cnt-1] += 1

print(*ans)
