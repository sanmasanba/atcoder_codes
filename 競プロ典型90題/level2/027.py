def main():
    N = int(input())

    S = set()
    ans = []

    for i in range(1, N+1):
        ele = str(input())
        #print(ele)
        if ele not in S:
            ans.append(i)
        S.add(ele)
    
    for j in ans:
        print(j)

if __name__ == '__main__':
    main()
