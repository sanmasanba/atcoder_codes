def main():
    N, K= map(int, input().split(' '))

    res = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            res += 100 * i + j
    
    print(res)

if __name__ == '__main__':
    main()