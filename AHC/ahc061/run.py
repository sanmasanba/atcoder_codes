from collections import deque
import random

random.seed(0)
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def clamp(x, lo, hi):
    return max(lo, min(x, hi))


def read_initial_input():
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


def get_candidates(N: int, M: int, owner: list[list[int]], px: list[int], py: list[int], p: int) -> set[tuple[int, int]]:
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


def get_candidates_sorted(N, M, owner, px, py, p):
    cand = get_candidates(N, M, owner, px, py, p)
    if not cand:
        return []
    return sorted(cand)


def read_turn_result(N: int, M: int, owner: list[list[int]], level: list[list[int]], px: list[int], py: list[int]):
    txs, tys = [0] * M, [0] * M
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
        (wa, wb, wc, wd, eps)
    """
    return (
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.1, 0.5),
    )


def enemy_policy_sampled_from_cand(N, U, V, owner, level, px, py, p, params, cand, rng):
    if not cand:
        return px[p], py[p]

    wa, wb, wc, wd, eps = params

    # ランダム行動
    if rng.random() < eps:
        return cand[rng.randrange(len(cand))]

    # 貪欲行動
    best = None
    best_score = -1e30
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

        if sc > best_score:
            best_score = sc
            best = (x, y)

    return best


def simulate_turn_fast(N, M, U, owner, level, px, py, txs, tys):
    # cell occupancy: dict[(x,y)] -> list[p]
    cell = {}
    for p in range(M):
        key = (txs[p], tys[p])
        cell.setdefault(key, []).append(p)

    # conflict resolution (iterate only occupied cells)
    remain = [False] * M
    pickup = set()

    for (i, j), ps in cell.items():
        if len(ps) == 1:
            remain[ps[0]] = True
            continue

        own = owner[i][j]
        if own in ps:
            remain[own] = True
            for q in ps:
                if q != own:
                    pickup.add(q)
        else:
            for q in ps:
                pickup.add(q)

    # copy-on-write for owner/level
    new_owner = owner[:]  # shallow copy rows
    new_level = level[:]

    def ensure_row_own(x):
        if new_owner[x] is owner[x]:
            new_owner[x] = owner[x][:]

    def ensure_row_lev(x):
        if new_level[x] is level[x]:
            new_level[x] = level[x][:]

    # territory update: only for remaining pieces
    for p in range(M):
        if not remain[p]:
            continue
        x, y = txs[p], tys[p]
        cur_owner = owner[x][y]
        cur_level = level[x][y]

        if cur_owner == -1:
            ensure_row_own(x)
            ensure_row_lev(x)
            new_owner[x][y] = p
            new_level[x][y] = 1
        elif cur_owner == p:
            if cur_level < U:
                ensure_row_lev(x)
                new_level[x][y] = cur_level + 1
        else:
            # attack
            if cur_level == 1:
                ensure_row_own(x)
                ensure_row_lev(x)
                new_owner[x][y] = p
                new_level[x][y] = 1
            else:
                ensure_row_lev(x)
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


def evaluate(N, M, V, owner, level):
    scores = [0] * M
    for i in range(N):
        row_own = owner[i]
        row_lev = level[i]
        row_v = V[i]
        for j in range(N):
            own = row_own[j]
            if own != -1:
                scores[own] += row_v[j] * row_lev[j]
    return scores[0] / (max(scores[1:]) + 1)


def choose_with_simulation(candidates, N, M, T, U, V, owner, level, px, py, t, enemy_particles):
    best_score = -1e30
    best_move = candidates[0]
    samples = max(1, min(20, 600//len(candidates)))

    # (A) ターン内キャッシュ：敵candは move に依存しない
    enemy_cands = [None] * M
    for p in range(1, M):
        enemy_cands[p] = get_candidates_sorted(N, M, owner, px, py, p)

    # (B) CRN：サンプルごとの seed を固定
    base_seed = 10_000_000 + t * 10_000
    sample_seeds = [base_seed + s for s in range(samples)]

    # (C) サンプルごとに「敵パラメータ」と「敵の最終行動」を固定して事前計算
    enemy_moves_per_s = []  # list of (txs, tys)
    for s in range(samples):
        rng = random.Random(sample_seeds[s])

        txs = [0] * M
        tys = [0] * M

        for p in range(1, M):
            params = enemy_particles[p - 1][rng.randrange(len(enemy_particles[p - 1]))]
            txs[p], tys[p] = enemy_policy_sampled_from_cand(
                N, U, V, owner, level, px, py, p, params, enemy_cands[p], rng
            )

        enemy_moves_per_s.append((txs, tys))

    # (D) moveごとの評価：敵行動は使い回し、simulate_turn だけ回す
    for mx, my in candidates:
        total = 0.0
        for s in range(samples):
            txs, tys = enemy_moves_per_s[s]
            # 自分の手だけ差し替え（M<=8なのでコピー軽い）
            txs0 = txs[:]
            tys0 = tys[:]
            txs0[0], tys0[0] = mx, my

            owner2, level2, *_ = simulate_turn_fast(N, M, U, owner, level, px, py, txs0, tys0)
            total += evaluate(N, M, V, owner2, level2)

        avg_score = total / samples
        if avg_score > best_score:
            best_score = avg_score
            best_move = (mx, my)

    return best_move


def main():
    K = 128
    N, M, T, U, V, owner, level, px, py = read_initial_input()
    enemy_particles = [[sample_enemy_params() for _ in range(K)] for _ in range(M - 1)]

    for t in range(T):
        candidates = sorted(get_candidates(N, M, owner, px, py, 0))
        tx, ty = choose_with_simulation(
            candidates,
            N, M, T, U, V, owner, level, px, py,
            t,
            enemy_particles,
        )

        print(tx, ty, flush=True)
        _obs_txs, _obs_tys = read_turn_result(N, M, owner, level, px, py)

if __name__ == "__main__":
    main()