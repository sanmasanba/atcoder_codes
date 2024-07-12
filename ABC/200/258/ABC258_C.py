def main():
    N, Q = map(int, input().split(' '))
    S = list(input())
    MOD = len(S)

    pos = 0
    res = []
    for _ in range(Q):
        t, x = map(int, input().split(' '))
        if t == 1:
            pos -= x
        else:
            res.append(S[(pos+x-1)%MOD])

    for i in res:
        print(i)

if __name__ == '__main__':
    main()