import bisect

def main():
    #input
    N = int(input())
    A = list(map(int, input().split(' ')))
    A.sort()
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    #
    for query in B:
        idx = bisect.bisect_left(A, query)
        if idx == N:
            print(abs(query - A[idx-1]))
        elif abs(query - A[idx-1]) < abs(A[idx]-query):
            print(abs(query - A[idx-1]))
        else:
            print(abs(A[idx]-query))

if __name__ == '__main__':
    main()
