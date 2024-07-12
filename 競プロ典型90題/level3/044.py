import collections

def main():
    N, Q = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    T, X, Y = [], [], []
    for _ in range(Q):
        t, x, y = map(int, input().split(' '))
        T.append(t)
        X.append(x)
        Y.append(y)
    length = len(A)

    slide = 0
    for i in range(Q):
        if T[i] == 1:
            tmp = A[(X[i]-1-slide)%length]
            A[(X[i]-1-slide)%length] = A[(Y[i]-1-slide)%length]
            A[(Y[i]-1-slide)%length] = tmp
        elif T[i] == 2: 
            slide += 1
        else:
            print(A[(X[i]-1-slide)%length])
        #print(A)
        
if __name__ == '__main__':
    main()