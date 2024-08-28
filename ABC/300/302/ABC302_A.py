A, B = map(int, input().split(" "))

res = A//B
print(res + (1 if A-B*res > 0 else 0))