import sys

def main():
    #input
    N = int(input())
    l = [0] * N
    r = [0] * N
    for i in range(N):
        l[i], r[i] = map(int, input(). split(' '))
    #左端と右端でそれぞれソート
    l.sort()
    r.sort()

    #全部のパターンを列挙
    ans = N*(N-1) // 2

    #尺取り法を使う(全パターンから余事象を引く形で考える)
    j = 0
    #leftをi、rightをjとする
    for i in range(N):
        #右端が左端を超えるまで、右端をインクリメント
        while r[j] < l[i]:
            j += 1
        #超えたら、区間が重複している範囲なので列挙から引く
        ans -= j
    
    print(ans)

if __name__ == '__main__':
    main()