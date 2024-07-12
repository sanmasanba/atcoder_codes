#入力の処理と初期化
N = int(input())
A = list(map(int, input().split()))
dp = [[0 for j in range(N)] for i in range(N)]

#メイン関数
def main():
    # 区間の長さ
    for length in range(1, N+1):  
        #区間の始点を設定
        for l in range(N - length + 1):
            #終点は始点に区間長をたしたもの
            r = l + length - 1
            #始点と終点が一致
            if l == r:
                dp[l][r] = A[l]
            else:
                #始点を選ぶとl+1に始点がずれて、rを選ぶと終点がr-1にずれる
                #これら二つを比較する
                dp[l][r] = max(A[l] - dp[l + 1][r], A[r] - dp[l][r - 1])

    #出力
    print(dp[0][N - 1])

if __name__ == '__main__':
    main()
