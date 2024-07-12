import sys

def main():
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    N, Q = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))

    # 右隣の区画との差の配列を作成
    B = [A[i + 1] - A[i] for i in range(N - 1)] + [0]

    # 不便さ合計初期値
    ans = sum(abs(b) for b in B)

    # 地殻変動ごとの不便さの差分を計算→合計に反映して出力
    res = []
    for _ in range(Q):
        l, r, v = map(int, input().split(" "))
        l, r = l - 1, r - 1

        # 地殻変動前の左右の不便さ合計
        before = abs(B[l - 1]) + abs(B[r])

        # 左側の階差の変化（+vだけ変化する）
        if l != 0:  # 1番目の区画以外の時のみ計算する
            B[l - 1] += v
        # 右側の階差の変化（-vだけ変化する）
        if r != N - 1:  # N番目の区画以外の時のみ計算する
            B[r] -= v

        # 地殻変動後の左右の不便さ合計
        after = abs(B[l - 1]) + abs(B[r])

        ans += after - before
        res.append(ans)

    for i in res:    
        print(i)

if __name__ == '__main__':
    main()