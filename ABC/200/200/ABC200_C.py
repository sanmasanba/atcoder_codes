def main():
    N = int(input())
    #答えを保存するやつ
    B = [0] * 200
    cnt = 0

    A = list(map(int, input().split(' ')))

    #200で割った余りがいくつあるかを数え上げる
    for i in A:
        B[i%200] += 1
    
    #数列に200で割った余りがiである要素の数を考える
    #どのように操作しても余りが相殺しないと条件を満たさない
    for i in range(200):
        #あまりがiだったものを一つ取り出したとき、
        #次も余りがiのものを取り出す場合の数は
        #(B[i]*(B[i]-1))/2になる。
        cnt += (B[i]*(B[i]-1))//2

    print(cnt)

if __name__ == '__main__':
    main()