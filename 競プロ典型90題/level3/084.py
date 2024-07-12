def main():
    N = int(input())
    S = list(input())

    res = N*(N+1)//2

    lengths = 0
    prior_c = S[0]
    cnt = 1
    for i in range(1, N):
        if prior_c == S[i]:
            cnt += 1
        else:
            lengths += cnt*(cnt+1)//2
            cnt = 1
            prior_c = S[i]
    lengths += cnt*(cnt+1)//2
    
    print(res - lengths)

if __name__ == '__main__':
    main()