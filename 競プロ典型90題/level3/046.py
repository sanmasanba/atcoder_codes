import collections

def main():
    A = [0 for i in range(47)]
    B = [0 for i in range(47)]
    C = [0 for i in range(47)]

    N = int(input())
    As = list(map(int, input().split(' ')))
    for i in As:
        A[i%46] += 1     
    
    Bs = list(map(int, input().split(' ')))
    for i in Bs:
        B[i%46] += 1   

    res = 0
    Cs = list(map(int, input().split(' ')))
    for i in Cs:
        C[i%46] += 1   

    res = 0
    for i in range(46):
        for j in range(47):
            for k in range(47):
                if (i + j + k) % 46 == 0:
                    res += A[i] * B[j] * C[k]
    print(res)
        
if __name__ == '__main__':
    main()