def main():
    Q = int(input())
    
    S = []
    ans = []
    for _ in range(Q):
        t, x = map(int, input().split(' '))
        if t == 1:
            S.insert(0, x)
        elif t == 2:
            S.append(x)
        else:
            ans.append(S[x-1])
        #print(S)

    for j in ans:
        print(j)

if __name__ == '__main__':
    main()
