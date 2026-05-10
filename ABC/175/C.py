def main():
    X, K, D = map(int, input().split(' '))

    X = abs(X)

    #移動回数を求める(K回とX/Dで移動回数が少ないほう)
    p = min(K, X//D)
    #余分な移動回数を削る
    K -= p
    #移動する
    X -= p * D

    #移動回数が余っているなら、残りを移動する
    if K % 2:
        print(D - X)
    #余っていないなら、そのまま出力
    else:
        print(X) 

if __name__ == '__main__':
    main()