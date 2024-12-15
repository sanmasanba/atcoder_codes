import random
import numpy as np
import time

# 初期設定
rng = random.Random(42)
s_time = time.process_time()

# 入力
N, T, sigma = map(int, input().split())
wh = []
for _ in range(N):
    w, h = map(int, input().split())
    wh.append((w, h))

def calculate_score(rectangles, operations):
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
        W = max(x + w for x, _, w, _ in layout)
        H = max(y + h for _, y, _, h in layout)
        return W + H, W, H

    layout = simulate_layout(operations)
    score = calculate_layout_score(layout)
    return score

def query(prdb):    
    print(len(prdb), flush=True)
    for p, r, d, b in prdb:
        print(p, r, d, b, flush=True)
    score, estimate_W, estimate_H = calculate_score(wh, prdb)
    print(f"# score: {score}")
    
    # 計測値を受け取る
    W, H = map(int, input().split())

def generater():
    prdb = []
    for i in range(N):
        prdb.append((
        i,
        rng.randint(0, 1),
        ['U', 'L'][rng.randint(0, 1)],
        rng.randint(-1, i - 1),
        ))
    return prdb

def simulated_annealing(estimate_wh):
    global N
    global T
    global s_time

    # 初期解を生成
    current_solution = generater()
    current_score, _, _ = calculate_score(estimate_wh, current_solution)
    temperature = 100.0
    cooling_rate = 0.99

    while temperature > 1.0 and 2.5 > time.process_time() - s_time:
        new_solution = current_solution[:]
        # ランダムに一部の長方形の位置を変更
        i = random.randint(0, N - 1)
        new_solution[i] = (
            new_solution[i][0],
            rng.randint(0, 1),
            ['U', 'L'][rng.randint(0, 1)],
            rng.randint(-1, i - 1),
        )
        new_score, _, _ = calculate_score(estimate_wh, new_solution)

        if new_score < current_score or random.random() < np.exp((current_score - new_score) / temperature):
            current_solution = new_solution
            current_score = new_score

        temperature *= cooling_rate

    return current_solution

def main():

    # ブロックの大きさを推定する
    key_wh = [(i, k) for i, k in enumerate(wh)]
    key_wh.sort(reverse=True, key=lambda x: max(x[1]))
    estimate_blocks = [[a] for a in wh]
    def estimate(i):
        i %= len(key_wh)
        print(1)
        print(i, 0, 'U', -1, flush=True)
        W, H = map(int, input().split(' '))
        estimate_blocks[i].append([W, H])

    for i in range(T - 1): 
        estimate(i)
    
    last_block_status = []
    for status in estimate_blocks:
        n = len(status)
        w, h = 0, 0
        for i, j in status:
            w, h = w + i, h + j
        last_block_status.append([w//n, h//n])

    # 最後の試行で最小のスコアを適用
    prdb = simulated_annealing(last_block_status)
    query(prdb)

if __name__ == '__main__':
    main()
