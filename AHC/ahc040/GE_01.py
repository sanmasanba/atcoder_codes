import random
import numpy as np

# 初期設定
s_time = 0
rng = random.Random()
thete = 0.5
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
        return W + H, W, H

    layout = simulate_layout(operations)
    score = calculate_layout_score(layout)
    return score

def query():
    global T
    global min_score
    global min_status
    global thete

    curr_score, _, _ = calculate_score(N, T, sigma, wh, min_status)
    prdb = min_status
    for _ in range(50):
        tmp = generater()
        tmp_score, _, _ = calculate_score(N, T, sigma, wh, tmp)
        if tmp_score < min_score and tmp_score < curr_score:
            curr_score = tmp_score
            prdb = tmp
    
    print(len(prdb), flush=True)
    for p, r, d, b in prdb:
        print(p, r, d, b, flush=True)
    score, estimate_W, estimate_H = calculate_score(N, T, sigma, wh, prdb)
    print(f"# score: {score}")
    W, H = map(int, input().split())
    # testcase
    testcase = 1
    if testcase:
        print(f"# estimate_W: {estimate_W}, W:{W}", flush=True)
        print(f"# estimate_H: {estimate_H}, H:{H}", flush=True)
        print(f"# calc_W:{estimate_W+W}", flush=True)
        print(f"# calc_H:{estimate_H+H}", flush=True)
        # 計測誤差を補正
        corrected_W = (estimate_W + W) / 2
        corrected_H = (estimate_H + H) / 2
        score = corrected_W + corrected_H
        if score < min_score:
            min_score = score
            min_status = prdb[:]
    # submit
    else:
        score = W + H
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

def genetic_algorithm():
    population_size = 30  # 集団サイズを増やす
    generations = 10  # 世代数を増やす
    mutation_rate = 0.1  # 突然変異率を調整

    # 初期集団の生成
    population = [generater() for _ in range(population_size)]

    for generation in range(generations):
        # 適応度の評価
        scores = [(calculate_score(N, T, sigma, wh, individual)[0], individual) for individual in population]
        scores.sort(key=lambda x: x[0])
        population = [individual for _, individual in scores]

        # 選択（トーナメント選択）
        selected = []
        for _ in range(population_size // 2):
            tournament = random.sample(population, 5)
            tournament.sort(key=lambda x: calculate_score(N, T, sigma, wh, x)[0])
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

    # 最良の個体を返す
    best_individual = population[0]
    return best_individual

def main():
    global T
    global min_status
    
    # 初期配置
    for i in range(N):
        min_status.append((i, 0, 'U', -1))

    # 遺伝的アルゴリズムで最適化
    min_status = genetic_algorithm()
    while 0 < T:   
        query()
        T -= 1

if __name__ == '__main__':
    main()
