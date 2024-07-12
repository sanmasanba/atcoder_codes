from collections import deque

def s2p(s):
    if s == 'R':
        return [1, 0]
    elif s == 'L':
        return [-1, 0]
    elif s == 'U':
        return [0, 1]
    else:
        return [0, -1]

def main():
    N, M, H, K = map(int, input().split(' '))
    S = deque(list(input()))
    items = set(tuple(map(int, input().split(' '))) for _ in range(M))

    pos = [0, 0]
    res = True
    while S:
        d = s2p(S.popleft())
        pos = [pos[0]+d[0], pos[1]+d[1]]
        H -= 1
        if H < 0:
            res = False

        if (pos[0], pos[1]) in items and H < K:
            H = K
            items.remove((pos[0], pos[1]))

    print('Yes' if res else 'No')

if __name__ == '__main__':
    main()