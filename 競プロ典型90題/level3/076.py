def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    ele_A = sum(A)
    As = A + A
    
    ans = 'No'
    #総和の10分の1が整数にならない場合は、数列は存在しない
    if ele_A % 10 != 0:
        pass
    else:
        ele_A //= 10
        right = 0   
        left = 0
        res = 0
        
        #leftが最後の数字になるまで尺取り法
        while left < N:
            #部分列がsum//10より小さくて、rightが循環列を超えない範囲
            while res < ele_A and right < left + N:
                res += As[right]
                right += 1

            #breakしたら、res >= ele_Aなので判定をする
            if res == ele_A:
                ans = 'Yes'
                break

            #resがsum//10より大きいかつrightがleftより小さい範囲まで尺取り
            while ele_A < res and left < right:
                res -= As[left]
                left += 1

                #一つ尺とるごとに判定
                if res == ele_A:
                    ans = 'Yes'
                    break

    print(ans)

if __name__ == '__main__':
    main()