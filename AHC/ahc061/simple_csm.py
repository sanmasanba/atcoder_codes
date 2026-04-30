from collections import deque
import random

random.seed(0)
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

def clamp(x, lo, hi):
    return max(lo, min(x, hi))

def read_initial_input():
    """
    入力と初期化

    Returns:
        N (int): 盤面の縦横(10)
        M (int): プレイヤー数([2, 8])
        T (int): 総ターン数(100)
        U (int): レベル上限([1, 5])
        V (list[list[int]]): 各領土の価値(sum(V) = 1000 * N^2)
        owner (list[list[int]]): 各領土の所有者
        level (list[list[int]]): 各領土のレベル
        px (list[int]): 各プレイヤーの位置(x)
        py (list[int]): 各プレイヤーの位置(y)
    """
    N, M, T, U = map(int, input().split())
    V = [list(map(int, input().split())) for _ in range(N)]
    sx, sy = [0] * M, [0] * M
    for p in range(M):
        sx[p], sy[p] = map(int, input().split())

    owner = [[-1] * N for _ in range(N)]
    level = [[0] * N for _ in range(N)]
    px, py = list(sx), list(sy)
    for p in range(M):
        owner[sx[p]][sy[p]] = p
        level[sx[p]][sy[p]] = 1

    return N, M, T, U, V, owner, level, px, py

def get_candidates(
        N: int, 
        M: int, 
        owner: list[list[int]], 
        px: list[int], 
        py: list[int], 
        p: int) -> set[tuple[int, int]]:
    """
    候補集合の作成

    Args:
        N (int): 盤面の縦横
        M (int): プレイヤー数
        owner (list[list[int]]): 各領土の所有者
        px (list[int]): 各プレイヤーの位置(x)
        py (list[int]): 各プレイヤーの位置(y)
        p (int): 対象のプレイヤー

    Returns:
        set[tuple[int, int]]: 移動可能な領土集合
    """
    reachable = {(px[p], py[p])}
    queue = deque([(px[p], py[p])])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in reachable and owner[nx][ny] == p:
                reachable.add((nx, ny))
                queue.append((nx, ny))

    candidates = set(reachable)
    for x, y in reachable:
        for d in range(4):
            nx, ny = x + DX[d], y + DY[d]
            if 0 <= nx < N and 0 <= ny < N:
                candidates.add((nx, ny))

    for q in range(M):
        if p == q:
            continue
        candidates.discard((px[q], py[q]))

    return candidates

def read_turn_result(
        N: int, 
        M: int, 
        owner: list[list[int]], 
        level: list[list[int]], 
        px: list[int], 
        py: list[int]):
    """
    インタラクティブな入力を受け取る

    Args:
        p (int): 対象のプレイヤー
        N (int): 盤面の縦横
        M (int): プレイヤー数
        owner (list[list[int]]): 各領土の所有者
        level (list[list[int]]): 各領土のレベル
        px (list[int]): 各プレイヤーの位置(x)
        py (list[int]): 各プレイヤーの位置(y)
    """
    txs, tys = [0]*M, [0]*M
    for m in range(M):
        txs[m], tys[m] = map(int, input().split())

    for p in range(M):
        px[p], py[p] = map(int, input().split())
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            owner[i][j] = row[j]
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            level[i][j] = row[j]
    
    return txs, tys

def sample_enemy_params():
    """
    相手のパラメータを生成する

    Returns:
        tuple[float]: 相手のパラメータ
    """
    return (
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.1, 0.5)
        )

def enemy_policy_sampled(N, M, U, V, owner, level, px, py, p, params):
    candidates = get_candidates(N, M, owner, px, py, p)
    if not candidates:
        return px[p], py[p]

    candidates = sorted(candidates)
    wa, wb, wc, wd, eps = params

    # ランダム行動
    if random.random() < eps:
        return random.choice(candidates)

    # 貪欲行動
    best = None
    best_score = -1e30
    for x, y in candidates:
        own = owner[x][y]
        lev = level[x][y]
        val = V[x][y]

        if own == -1:
            sc = val * wa
        elif own == p:
            sc = val * wb if lev < U else 0.0
        else:
            sc = val * (wc if lev == 1 else wd)

        if sc > best_score:
            best_score = sc
            best = (x, y)

    return best

def simulate_turn(N, M, U, owner, level, px, py, txs, tys):

    # cell occupancy
    cell = [[[] for _ in range(N)] for __ in range(N)]
    for p in range(M):
        x, y = txs[p], tys[p]
        cell[x][y].append(p)

    # conflict resolution
    remain = [False] * M
    pickup = set()
    for i in range(N):
        for j in range(N):
            ps = cell[i][j]
            if not ps:
                continue
            if len(ps) == 1:
                remain[ps[0]] = True
                continue
            # multiple pieces
            own = owner[i][j]
            if own in ps:
                # owner stays, others picked up
                remain[own] = True
                for p in ps:
                    if p != own:
                        pickup.add(p)
            else:
                # all picked up
                for p in ps:
                    pickup.add(p)

    # territory update
    new_owner = [row[:] for row in owner]
    new_level = [row[:] for row in level]

    for p in range(M):
        if not remain[p]:
            continue
        x, y = txs[p], tys[p]
        cur_owner = owner[x][y]
        cur_level = level[x][y]
        if cur_owner == -1:
            new_owner[x][y] = p
            new_level[x][y] = 1
        elif cur_owner == p:
            new_level[x][y] = min(cur_level + 1, U)
        else:
            # attack
            if cur_level == 1:
                new_owner[x][y] = p
                new_level[x][y] = 1
            else:
                new_level[x][y] = cur_level - 1
                pickup.add(p)
                remain[p] = False

    # pieces return
    new_px = [0] * M
    new_py = [0] * M
    for p in range(M):
        if remain[p]:
            new_px[p], new_py[p] = txs[p], tys[p]
        else:
            new_px[p], new_py[p] = px[p], py[p]

    return new_owner, new_level, new_px, new_py

def simulate_one_step(N, M, T, U, V, owner, level, px, py,
                      t, move, enemy_cand_params):

    # 敵パラメータをサンプリング
    enemy_params = [None] * M
    for p in range(1, M):
        enemy_params[p] = random.choice(enemy_cand_params[p-1])

    txs = [0] * M
    tys = [0] * M
    txs[0], tys[0] = move

    # 敵の行動
    for p in range(1, M):
        txs[p], tys[p] = enemy_policy_sampled(
            N, M, U, V, owner, level, px, py, p, enemy_params[p]
        )

    # 1ターン進める
    new_owner, new_level, new_px, new_py = simulate_turn(
        N, M, U, owner, level, px, py, txs, tys
    )

    return new_owner, new_level, txs, tys, enemy_params

def evaluate(N, M, V, owner, level):
    scores = [0] * M
    for i in range(N):
        for j in range(N):
            own = owner[i][j]
            if own != -1: scores[own] += V[i][j] * level[i][j]
    return scores[0]/(max(scores[1:]) + 1)

def choose_with_simulation(candidates, N, M, T, U, V,
                           owner, level, px, py, 
                           t, 
                           enemy_cand_params):

    best_score = -1e30
    best_move = candidates[0]
    samples = 7

    for move in candidates:
        total = 0
        for _ in range(samples):
            owner2, level2, txs, tys, enemy_params = simulate_one_step(
                N, M, T, U, V, owner, level, px, py, 
                t, 
                move, 
                enemy_cand_params
            )
            total += evaluate(N, M, V, owner2, level2)
        avg_score = total / samples 
        if avg_score > best_score:
            best_score = avg_score
            best_move = move

    return best_move

def enemy_action_prob(N, M, U, V, owner, level, px, py, p, params, a_obs):
    """
    パラメータ params のとき、
    観測された行動 a_obs が起きる確率を返す
    """

    candidates = get_candidates(N, M, owner, px, py, p)
    # 候補なしの場合、現在地に固定
    if not candidates:
        return 1.0 if a_obs == (px[p], py[p]) else 1e-12
    
    cand = sorted(candidates)

    wa, wb, wc, wd, eps = params

    # ランダム部分(eps)
    pr = eps / len(cand)

    # 貪欲部分(1-eps)
    best_score = -1e30
    best_actions = []

    for x, y in cand:
        own = owner[x][y]
        lev = level[x][y]
        val = V[x][y]

        if own == -1:
            sc = val * wa
        elif own == p:
            sc = val * wb if lev < U else 0.0
        else:
            sc = val * (wc if lev == 1 else wd)

        if sc > best_score + 1e-12:
            best_score = sc
            best_actions = [(x, y)]
        elif abs(sc - best_score) <= 1e-12:
            best_actions.append((x, y))

    pg = 0.0
    if a_obs in best_actions:
        pg = (1.0 - eps) / len(best_actions)

    # 合成確率
    return max(pr + pg, 1e-12)

def jitter_params(params, noise=0.02):
    # tuple (wa,wb,wc,wd,eps) に小さいノイズを加える
    wa, wb, wc, wd, eps = params
    def j(x):
        return x + (random.random() * 2 - 1) * noise
    wa = clamp(j(wa), 0.3, 1.0)
    wb = clamp(j(wb), 0.3, 1.0)
    wc = clamp(j(wc), 0.3, 1.0)
    wd = clamp(j(wd), 0.3, 1.0)
    eps = clamp(j(eps), 0.1, 0.5)
    return (wa, wb, wc, wd, eps)

def update_enemy_particles_cem(
    particles,  # list[tuple]
    N, M, U, V, owner, level, px, py, p,
    a_obs,
    elite_frac=0.25,
    noise=0.02
    ):
    # それぞれの候補に対して、確率を求める
    scored = []
    for th in particles:
        w = enemy_action_prob(N, M, U, V, owner, level, px, py, p, th, a_obs)
        scored.append((w, th))
    scored.sort(key=lambda x: x[0], reverse=True)

    top = scored[0][0]
    bottom = scored[-1][0]
    if top <= bottom * 1.05:
        return particles  

    # topPを残す
    elite_n = max(1, int(len(particles) * elite_frac))
    elites = [th for _, th in scored[:elite_n]]

    # 突然変異を混ぜる
    new_particles = []
    for _ in range(len(particles)):
        base = random.choice(elites)
        if noise > 0:
            base = jitter_params(base, noise=noise)
        new_particles.append(base)

    return new_particles

def avg_likelihood_for_enemy(particles, N, M, U, V, owner, level, px, py, p, a_obs):
    s = 0.0
    for th in particles:
        s += enemy_action_prob(N, M, U, V, owner, level, px, py, p, th, a_obs)
    return s / len(particles)

def main():
    K = 128
    N, M, T, U, V, owner, level, px, py = read_initial_input()
    enemy_cand_params = [[sample_enemy_params() for _ in range(K)] for _ in range(M-1)]

    for t in range(T):
        candidates = get_candidates(N, M, owner, px, py, 0)
        tx, ty = choose_with_simulation(
            list(candidates), 
            N, M, T, U, V, owner, level, px, py, 
            t, 
            enemy_cand_params
            )
        # copy before
        owner0 = [row[:] for row in owner]
        level0 = [row[:] for row in level]
        px0 = px[:]
        py0 = py[:]
        print(tx, ty, flush=True)
        obs_txs, obs_tys = read_turn_result(N, M, owner, level, px, py)

        for p in range(1, M):
            a_obs = (obs_txs[p], obs_tys[p])
            enemy_cand_params[p-1] = update_enemy_particles_cem(
                enemy_cand_params[p-1],
                N, M, U, V, owner0, level0, px0, py0, p, a_obs,
                elite_frac=0.25,  
                noise=0.02
            )

if __name__ == '__main__':
    main()
