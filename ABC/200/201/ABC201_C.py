def main():
    S = input()
    #0000から9999まで調べる
    ans = 0
    for i in range(10000):
        flag = [False]*10
        now = i
        #10で割りながら、使われている数字をメモ
        for j in  range(4):
            flag[now%10] = True
            now //= 10
        flag2 = True
        #使われているかチェック
        for j in range(10):
            #文字が使われているはずなのに、使われていない
            if S[j] == 'o' and not flag[j]:
                flag2 = False
            #文字が使われていないはずが、使われている
            if S[j] == 'x' and flag[j]:
                flag2 = False
        ans += flag2
    
    print(ans)

if __name__ == '__main__':
    main()