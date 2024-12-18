import random
import numpy as np
import time
import math

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
    
    # 計測値を受け取る
    W, H = map(int, input().split())

def generater(est_wh):
    target_W = math.sqrt(sum(w*h for w, h in est_wh))
    res = []
    crr_w = 0
    crr_target = -1
    for i, wh in enumerate(est_wh):
        w, _ = wh
        if crr_w + w <= target_W:
            res.append((i, rng.randint(0, 1), 'L', crr_target))
            crr_w += w
        else:
            res.append((i, rng.randint(0, 1), 'U', -1))
            crr_target = i
            crr_w = w
    return res

def genetic_algorithm(est_wh):
    population_size =  30     
    mutation_rate = 0.1

    # 初期集団の生成
    population = [generater(est_wh) for _ in range(population_size)]
    generation = 0
    while time.process_time() - s_time < 2.0:
        # 適応度の評価
        scores = [(calculate_score(est_wh, individual)[0], individual) for individual in population]
        scores.sort(key=lambda x: x[0])
        population = [individual for _, individual in scores]

        # 選択（トーナメント選択）
        selected = []
        for _ in range(population_size // 2):
            tournament = random.sample(population, 5)
            tournament.sort(key=lambda x: calculate_score(est_wh, x)[0])
            selected.append(tournament[0])

        # 交叉（一様交叉）
        offspring = []
        for _ in range(population_size // 2):
            parent1 = random.choice(selected)
            parent2 = random.choice(selected)
            child = []
            for i in range(N):
                if random.random() < 0.5:
                    child.append(parent1[i])
                else:
                    child.append(parent2[i])
            offspring.append(child)

        # 突然変異
        for individual in offspring:
            if random.random() < mutation_rate:
                mutation_point = random.randint(0, N - 1)
                individual[mutation_point] = (
                    individual[mutation_point][0],
                    rng.randint(0, 1),
                    ['U', 'L'][rng.randint(0, 1)],
                    rng.randint(-1, mutation_point - 1),
                )

        # 次世代への移行
        population = selected + offspring
        generation += 1

    # 最良の個体を返す
    best_individual = population[0]
    return best_individual

def main():

    # ブロックの大きさを推定する
    key_wh = [(i, k) for i, k in enumerate(wh)]
    key_wh.sort(key=lambda x: max(x[1]))
    estimate_blocks = [[a] for a in wh]
    def estimate(i):
        i %= len(key_wh)
        print(1)
        print(key_wh[i][0], 0, 'U', -1, flush=True)
        W, H = map(int, input().split(' '))
        estimate_blocks[key_wh[i][0]].append([W, H])

    for i in range(T - 1): 
        estimate(i)
    
    last_block_status = []
    for status in estimate_blocks:
        n = len(status)
        w, h = 0, 0
        for i, j in status:
            w, h = w + i, h + j
        last_block_status.append([w//n, h//n])

    # 最小のスコアを適用
    prdb = genetic_algorithm(last_block_status)
    query(prdb)

if __name__ == '__main__':
    main()
