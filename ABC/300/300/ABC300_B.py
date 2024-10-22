import sys

shape = list(map(int, input().split(' ')))

A = [list(str(input())) for h in range(shape[0])]
B = [list(str(input())) for h in range(shape[0])]


for s in range(shape[0]):
    for t in range(shape[1]):
        flag = 1
        for i in range(shape[0]):
            for j in range(shape[1]):
                if A[(i + s) % shape[0]][(j + t) % shape[1]] != B[i][j]:
                    flag = 0
        if flag == 1:
            print('Yes')
            exit()

print('No')  
