from collections import deque

def main():
    N, M = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    
    tmp_A = sorted(A)
    tmp_B = sorted(B)
    AQ = deque(tmp_A)
    BQ = deque(tmp_B)

    res = 0
    pos = 0
    while BQ:
        b = BQ.popleft()
        while AQ:
            a = AQ.popleft() 
            if a >= b:
                pos += 1
                res += a
                break
    
    if res == 0 or pos < M:
        print(-1)
    else:
        print(res)

if __name__ == '__main__':
    main()