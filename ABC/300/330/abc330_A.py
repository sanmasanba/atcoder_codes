N, L = map(int, input().split(' '))
points = list(map(int, input().split(' ')))

cnt = 0
for i in range(N):
    if points[i] >= L:
        cnt += 1
print(cnt)