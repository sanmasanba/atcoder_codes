def main():
    #input
    N = int(input())
    A = list(map(int, input().split(' ')))

    #辞書型を作成して、それぞれの数字の数を数える
    cnt = {}
    ans = 0

    #すべての文字を探索
    for j in range(N):
        #（ここまでの全体の文字数）- （その文字はここまでに何回でたか）
        ans += j - cnt.get(A[j], 0)
        #今の文字を保存
        cnt[A[j]] = cnt.get(A[j], 0) + 1

    print(ans)

if __name__ == '__main__':
    main()