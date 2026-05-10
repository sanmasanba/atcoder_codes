def main():
    N, K = map(int, input().split(' '))
    
    for k in range(K):
        if N % 200 == 0:
            N /= 200
        else:
            N = N*1000 + 200

    print(int(N))

if __name__ == '__main__':
    main()