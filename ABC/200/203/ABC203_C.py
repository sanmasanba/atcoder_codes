def main():
    #input
    N, K= map(int, input().split(' '))
    AB = [list(map(int, input().split(' '))) for i in range(N)]        
    #sort
    AB.sort()

    j = 0
    ans = K

    #まだ友達が残っていて、かつ所持金で次の友達がいる村に到達できる
    while j < N and AB[j][0] <= ans:
        #到達できるところまで移動して、
        ans += AB[j][1]
        #次の友人を試す
        j += 1

    print(ans)
    
if __name__ == '__main__':
    main()