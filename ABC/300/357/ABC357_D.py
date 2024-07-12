def main():
    N = int(input())
    
    length = len(str(N))
    res = 0
    for i in range(N):
        x = N * 10 ** (length * i) % 998244353
        res = (res + x) % 998244353

    print(res)
    print(res%998244353)
    
if __name__ == '__main__':
    main()