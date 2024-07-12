N, K = map(int, (input().split(' ')))
A = list(map(int, input().split(' ')))

#ビットを用いて初期化
dp = [False] * 100010

def main():
    #残りの石の数がi個のとき
    for i in range(K+1):
        #ｊ番目の選択肢を選ぼうとするとき
        for j in range(N):
            #選択可能なら
            if i >= A[j]:
                #石がi個の時のdp[i]は、
                #自分がtrue(=[dp[i]])かつ、
                #その前の手番がFalse(=dp[i-A[j]])のとき
                #trueになる。（勝てる）
                dp[i] = dp[i] or not dp[i-A[j]]

    print('First' if dp[K] else 'Second')

if __name__ == '__main__':
    main()


