import random
import numpy as np

# 初期設定
s_time = 0
rng = random.Random(42)
thete = 0.2
min_score = 10**10
min_status = []

# 入力
N, T, sigma = map(int, input().split())
wh = []
for _ in range(N):
    w, h = map(int, input().split())
    wh.append((w, h))

def calculate_score(N, T, sigma, rectangles, operations):
    def simulate_layout(operations):
        layout = []
        for op in operations:
            p, r, d, b = op
            w, h = rectangles[p]
            if r == 1:
                w, h = h, w
            if d == 'U':
                if b == -1:
                    x = 0
                else:
                    x = layout[b][0] + layout[b][2]
                y = 0
                for lx, ly, lw, lh in layout:
                    if lx <= x < lx + lw:
                        y = max(y, ly + lh)
                layout.append((x, y, w, h))
            elif d == 'L':
                if b == -1:
                    y = 0
                else:
                    y = layout[b][1] + layout[b][3]
                x = 0
                for lx, ly, lw, lh in layout:
                    if ly <= y < ly + lh:
                        x = max(x, lx + lw)
                layout.append((x, y, w, h))
        return layout

    # 配置結果からスコアを計算する関数
    def calculate_layout_score(layout):
        W = max(x + w for x, y, w, h in layout)
        H = max(y + h for x, y, w, h in layout)
        W_prime = np.random.normal(W, sigma)
        H_prime = np.random.normal(H, sigma)
        W_prime = max(1, min(W_prime, 10**9))
        H_prime = max(1, min(H_prime, 10**9))
        return W_prime + H_prime, W_prime, H_prime

    layout = simulate_layout(operations)
    score = calculate_layout_score(layout)
    return score

def query(prdb):
    global T
    global min_score
    global min_status
    global thete

    curr_score, _, _ = calculate_score(N, T, sigma, wh, prdb)
    for _ in range(30):
        tmp = generater()
        tmp_score, _, _ = calculate_score(N, T, sigma, wh, tmp)
        if tmp_score < min_score and tmp_score < curr_score:
            curr_score = tmp_score
            prdb = tmp
    
    print(len(prdb))
    for p, r, d, b in prdb:
        print(p, r, d, b)
    score, estimate_W, estimate_H = calculate_score(N, T, sigma, wh, prdb)
    print(f"# socre: {score}")
    W, H = map(int, input().split())
    # testcase
    testcase = 1
    if testcase:
        print(f"# estimate_W: {estimate_W}, W:{W}")
        print(f"# estimate_H: {estimate_H}, W:{H}")
        print(f"# calc_W:{estimate_W+W}")
        print(f"# calc_H:{estimate_H+H}")
        score += (W + H)
        if score < min_score:
            min_score = score
            min_status = prdb[:]
    # submit
    else:
        score = W+H
        if score < min_score:
            min_score = score
            min_status = prdb[:]

def generater():
    global N
    global thete
    global min_status

    prdb = []
    choices = set(random.sample(range(N), int(N*thete)))
    for i in range(N):
        if i in choices:
            prdb.append((
            i,
            rng.randint(0, 1),
            ['U', 'L'][rng.randint(0, 1)],
            rng.randint(-1, i - 1),
            ))
        else:
            prdb.append(min_status[i])

    return prdb

def main():
    global T
    global min_status
    
    # 初期配置
    for i in range(N):
        min_status.append((i, 0, 'U', -1))

    # ランダムに調整
    prdb = generater()
    while 0 < T:   
        query(prdb)
        T -= 1

if __name__ == '__main__':
    main()
