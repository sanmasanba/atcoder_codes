from collections import deque
import random
import sys
import run
import math
import os

random.seed(0)
NEI = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def read_local_inputs():
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

    # wa/wb/wc/wd/eps: store at index p (0..M-1), but inputs are given for players 1..M-1
    wa = [0.0] * M
    wb = [0.0] * M
    wc = [0.0] * M
    wd = [0.0] * M
    eps = [0.0] * M
    for p in range(1, M):
        wa[p], wb[p], wc[p], wd[p], eps[p] = map(float, input().split())

    # r1, r2: make them T x M so we can use r1[t][p], r2[t][p] directly; p=0 stays 0.0
    r1 = [[0.0] * M for _ in range(T)]
    r2 = [[0.0] * M for _ in range(T)]
    for t in range(T):
        for p in range(1, M):
            v1, v2 = map(float, input().split())
            r1[t][p] = v1
            r2[t][p] = v2

    return N, M, T, U, V, owner, level, px, py, wa, wb, wc, wd, eps, r1, r2

def get_candidates(N, M, owner, px, py, p):
    """
    Match Rust get_candidates:
    - BFS starting from current pos
    - visited grid
    - when popping (x,y): check if any other player's piece is at (x,y); if none, add to reachable
    - only expand neighbors if owner[x][y] == p
    - return reachable as a list in BFS order
    """
    start = (px[p], py[p])
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    reachable = []  # keep BFS order

    while q:
        x, y = q.popleft()

        # check if any other player's piece is at (x,y)
        ok = True
        for i in range(M):
            if i != p and (px[i], py[i]) == (x, y):
                ok = False
                break
        if ok:
            reachable.append((x, y))

        # expand only if this cell is owned by player p
        if owner[x][y] == p:
            for dx, dy in NEI:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return reachable

def decide_action(N, M, U, V, owner, level, px, py,
                  wa, wb, wc, wd, eps, r1, r2, t, p):
    candidates = get_candidates(N, M, owner, px, py, p)
    if not candidates:
        return px[p], py[p]

    r1_tp = r1[t][p]
    r2_tp = r2[t][p]

    # compute scores
    scores = []
    for (x, y) in candidates:
        own = owner[x][y]
        lev = level[x][y]
        val = float(V[x][y])
        if own == -1:
            sc = val * wa[p]
        elif own == p:
            sc = val * wb[p] if lev < U else 0.0
        else:
            sc = val * (wc[p] if lev == 1 else wd[p])
        scores.append(sc)

    if r1_tp < eps[p]:
        idx = int((r2_tp * len(candidates)) // 1)
        idx = min(idx, len(candidates) - 1)
        return candidates[idx]
    else:
        max_score = max(scores)
        tol = 1e-9 * max(abs(max_score), 1.0)
        best_indices = [i for i, s in enumerate(scores) if s >= max_score - tol]
        idx = int((r2_tp * len(best_indices)) // 1)
        idx = min(idx, len(best_indices) - 1)
        chosen = candidates[best_indices[idx]]
        return chosen

def read_turn_result(N, M, T, U, V, owner, level, px, py,
                     wa, wb, wc, wd, eps, r1, r2, tx, ty, t):
    # set my move
    txs = [0] * M
    tys = [0] * M
    txs[0], tys[0] = tx, ty

    # decide other players' moves using Rust-like AI
    for p in range(1, M):
        txs[p], tys[p] = decide_action(N, M, U, V, owner, level, px, py,
                                       wa, wb, wc, wd, eps, r1, r2, t, p)

    # simulate turn
    new_owner, new_level, new_px, new_py = run.simulate_turn_fast(N, M, U, owner, level, px, py, txs, tys)
    return new_owner, new_level, txs, tys, new_px, new_py

import math

def _mean(xs):
    return sum(xs) / max(1, len(xs))

def _median(xs):
    xs = sorted(xs)
    n = len(xs)
    if n == 0:
        return 0.0
    if n % 2 == 1:
        return xs[n // 2]
    return 0.5 * (xs[n // 2 - 1] + xs[n // 2])

def _l2(a, b):
    # a,b: tuple/list length 5
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(5)))

def _l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(5))

def summarize_particle_error(particles, true_params):
    """
    particles: list[tuple(wa,wb,wc,wd,eps)]
    true_params: tuple(wa,wb,wc,wd,eps)
    return: dict metrics
    """
    d2 = [_l2(th, true_params) for th in particles]
    d1 = [_l1(th, true_params) for th in particles]

    # 代表点（粒子平均）
    wa_m = _mean([th[0] for th in particles])
    wb_m = _mean([th[1] for th in particles])
    wc_m = _mean([th[2] for th in particles])
    wd_m = _mean([th[3] for th in particles])
    eps_m = _mean([th[4] for th in particles])
    mean_params = (wa_m, wb_m, wc_m, wd_m, eps_m)

    # 代表点（粒子中央値）
    wa_md = _median([th[0] for th in particles])
    wb_md = _median([th[1] for th in particles])
    wc_md = _median([th[2] for th in particles])
    wd_md = _median([th[3] for th in particles])
    eps_md = _median([th[4] for th in particles])
    median_params = (wa_md, wb_md, wc_md, wd_md, eps_md)

    # 「近い粒子の割合」：しきい値は適当に開始（あとで調整）
    # それぞれの次元範囲が0.7(wa~wd),0.4(eps)なので、L2で0.08〜0.12ぐらいから試すと見やすい
    th_l2 = 0.10
    near = sum(1 for x in d2 if x <= th_l2) / max(1, len(d2))

    return {
        "K": len(particles),
        "l2_mean": _mean(d2),
        "l2_med": _median(d2),
        "l2_min": min(d2) if d2 else 0.0,
        "l1_mean": _mean(d1),
        "near_frac_l2<=0.10": near,
        "mean_params_l2": _l2(mean_params, true_params),
        "median_params_l2": _l2(median_params, true_params),
        "mean_params": mean_params,
        "median_params": median_params,
    }

def print_enemy_param_tracking(t, M, true_params_list, enemy_particles):
    """
    true_params_list: list length M with None for player0 and tuple for enemies
    enemy_particles: list length (M-1), each is list of particles
    """
    print(f"# t={t} param_tracking", flush=True)
    for p in range(1, M):
        true_p = true_params_list[p]
        met = summarize_particle_error(enemy_particles[p-1], true_p)
        tp = true_p
        mp = met["mean_params"]
        print(
            f"  enemy{p}: "
            f"true=({tp[0]:.3f},{tp[1]:.3f},{tp[2]:.3f},{tp[3]:.3f},{tp[4]:.3f}) "
            f"mean=({mp[0]:.3f},{mp[1]:.3f},{mp[2]:.3f},{mp[3]:.3f},{mp[4]:.3f}) "
            f"l2mean={met['l2_mean']:.4f} l2min={met['l2_min']:.4f} "
            f"near={met['near_frac_l2<=0.10']:.2f} "
            f"meanL2={met['mean_params_l2']:.4f}",
            flush=True
        )

def main():
    K = 128
    N, M, T, U, V, owner, level, px, py, wa, wb, wc, wd, eps, r1, r2 = read_local_inputs()
    enemy_particles = [[run.sample_enemy_params() for _ in range(K)] for _ in range(M - 1)]

    for t in range(T):
        # You can replace this with your own AI for player 0.
        candidates = run.get_candidates(N, M, owner, px, py, 0)
        tx, ty = run.choose_with_simulation(
            list(candidates), N, M, T, U, V, owner, level, px, py, 
            t, 
            enemy_particles
            )        

        print(tx, ty, flush=True)

        owner, level, obs_txs, obs_tys, px, py = read_turn_result(N, M, T, U, V, owner, level, px, py,
                                                wa, wb, wc, wd, eps, r1, r2, tx, ty, t)

if __name__ == '__main__':
    main()
