N = int(input())

cnt = 0
for b in (range(1, N)):
    for a in (range(b, N)):
        if a * b < N:
            if a == b:
                cnt += 1
            else:
                cnt += 2
        else:
            break

print(cnt)
