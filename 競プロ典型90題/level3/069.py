#繰り返し2乗法
def pow(K, N):
    #初期値はA**0 = 1
    res = 1

    #タイルの枚数が1枚以上のとき
    while N != 0:
        #タイルの枚数が奇数枚なら
        if N % 2 == 1:
            #K**1(mod 1000000007)を計算する
            res = res * K % 1000000007
        #K**2, K**4, ... (mod 1000000007) を計算
        K = K * K % 1000000007
        #Nを半分にする
        N //= 2

    return res

def main():
    N, K = map(int, input().split(' '))
    #Kが1色なら
    if K == 1:
        #タイルが1枚なら1、それ以上なら塗分け不可
        print( 1 if N == 1 else 0)
    #Kが2色以上で
    #タイルが１枚
    elif N == 1:
        print(K)
    #タイルが２枚
    elif N == 2:
        print(K * (K - 1))
    #タイルが３枚以上
    else:
        print(K * (K - 1) % 1000000007 * pow(K - 2, N - 2) % 1000000007)

if __name__ == '__main__':
    main()