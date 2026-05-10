import time

c2i = {v:i for i, v in enumerate('atcoder')}
def ch(s):
    return c2i[s]

def main():
    S = list(map(ch, input()))
    cnt = 0
    for i in range(7):
        while S.index(i) > i:
            idx = S.index(i)
            tmp = S[idx]
            S[idx] = S[idx-1]
            S[idx-1] = tmp
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()