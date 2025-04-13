for i in range(1):
    with open(f'./tools/in/{i:04}.txt', 'r') as f:
        text = f.readlines()

    # read input
    cursor = 0
    N, M, Q, L, W = map(int, text[cursor].split())
    cursor += 1
    G = list(map(int, text[cursor].split()))
    cursor += 1
    lx, rx, ly, ry = [], [], [], []
    for i in range(N):
        a, b, c, d = text[cursor+i].split()
        lx.append(a)
        rx.append(b)
        ly.append(c)
        ry.append(d)
    cursor += N
    TRUE_POS = [list(map(int, text[cursor+i].split())) for i in range(N)]