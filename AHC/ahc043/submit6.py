# -*- coding: utf-8 -*-

import sys
from collections import deque, defaultdict
from functools import lru_cache
import random
import time

Pos = tuple[int, int]
S_TIME = time.time()
EMPTY = -1
PASS = -1
DO_NOTHING = -1
STATION = 0
RAIL_HORIZONTAL = 1
RAIL_VERTICAL = 2
RAIL_LEFT_DOWN = 3
RAIL_LEFT_UP = 4
RAIL_RIGHT_UP = 5
RAIL_RIGHT_DOWN = 6
COST_STATION = 5000
COST_RAIL = 100
SEARCH_ZONE = [(0, -2), (-1, -1), (0, -1), (1, -1), (2, 0), (1, 0), (0, 0), 
               (-1, 0), (-2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)]
INF = 1 << 60
input = sys.stdin.readline
random.seed(42)

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1 for _ in range(n * n)]

    def _find_root(self, idx: int) -> int:
        if self.parents[idx] < 0:
            return idx
        self.parents[idx] = self._find_root(self.parents[idx])
        return self.parents[idx]

    def is_same(self, p: Pos, q: Pos) -> bool:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        return self._find_root(p_idx) == self._find_root(q_idx)

    def unite(self, p: Pos, q: Pos) -> None:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        p_root = self._find_root(p_idx)
        q_root = self._find_root(q_idx)
        if p_root != q_root:
            p_size = -self.parents[p_root]
            q_size = -self.parents[q_root]
            if p_size > q_size:
                p_root, q_root = q_root, p_root
            self.parents[q_root] += self.parents[p_root]
            self.parents[p_root] = q_root


# @lru_cache(None)
def distance(a: Pos, b: Pos) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Action:
    def __init__(self, type: int, pos: Pos):
        self.type = type
        self.pos = pos

    def __str__(self):
        if self.type == DO_NOTHING:
            return "-1"
        else:
            return f"{self.type} {self.pos[0]} {self.pos[1]}"


class Result:
    def __init__(self, actions: list[Action], score: int):
        self.actions = actions
        self.score = score

    def __str__(self):
        return "\n".join(map(str, self.actions))

class Field:
    def __init__(self, N: int):
        self.N = N
        self.rail = [EMPTY for _ in range(N*N)]
        self.uf = UnionFind(N)
        self.has_station = [set() for _ in range(N*N)]

    def build(self, type: int, r: int, c: int) -> None:
        if 1 <= type <= 6:
            if self.rail[r*self.N+c] != EMPTY:
                raise ValueError(f"Rail type {type} cannot be built on non-empty cell ({r}, {c})")
        self.rail[r*self.N+c] = type

        # 隣接する区画と接続
        # 上
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
            if r > 0 and self.rail[(r-1)*self.N+c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
                self.uf.unite((r, c), (r - 1, c))
        # 下
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
            if r < self.N - 1 and self.rail[(r+1)*self.N+c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r + 1, c))
        # 左
        if type in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
            if c > 0 and self.rail[r*self.N+c-1] in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r, c - 1))
        # 右
        if type in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
            if c < self.N - 1 and self.rail[r*self.N+c+1] in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
                self.uf.unite((r, c), (r, c + 1))

    def is_connected(self, s: Pos, t: Pos) -> bool:
        stations0 = self.collect_stations(s)
        stations1 = self.collect_stations(t)
        for station0 in stations0:
            for station1 in stations1:
                if self.uf.is_same(station0, station1):
                    return True
        return False
    
    def rail_type(self, r, c):
        return self.rail[r*self.N+c]

    def collect_stations(self, pos: Pos) -> list[Pos]:
        return list(self.has_station[pos[0]*self.N+pos[1]])


class Solver:
    def __init__(self, N: int, M: int, K: int, T: int, home: list[Pos], workplace: list[Pos]):
        self.N = N
        self.M = M
        self.K = K
        self.T = T
        self.home = home
        self.workplace = workplace
        self.field = Field(N)
        self.money = K
        self.actions = []
        self.person_idxs = []
        self.station = []
        self.candidate_place = []
        self.pos2home = {pos: i for i, pos in enumerate(self.home)}
        self.pos2workplace = {pos: i for i, pos in enumerate(self.workplace)}

        # prepare
        for person_idx in range(self.M):
            person_dist = distance(self.home[person_idx], self.workplace[person_idx])
            self.person_idxs.append([person_dist, person_idx])
        self.person_idxs.sort(key=lambda x: (x[0], x[1]))

    def calc_income(self) -> int:
        income = 0
        for i in range(self.M):
            if self.field.is_connected(self.home[i], self.workplace[i]):
                income += distance(self.home[i], self.workplace[i])
        return income

    def build_rail(self, type: int, r: int, c: int) -> None:
        self.field.build(type, r, c)
        self.money -= COST_RAIL
        self.actions.append(Action(type, (r, c)))

    def build_station(self, r: int, c: int) -> None:
        self.field.build(STATION, r, c)
        self.money -= COST_STATION
        self.station.append((r, c))
        for dr, dc in SEARCH_ZONE:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < self.N) or not (0 <= nc < self.N):
                continue
            self.field.has_station[self.N*nr+nc].add((r, c))
        self.actions.append(Action(STATION, (r, c)))

    def build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
    
    def is_quit(self) -> None:
        return not (len(self.actions) < self.T)

    def search_station(self) -> tuple[int, int, int, int]:
        income = self.calc_income()
        r0, c0, r1, c1 = -1, -1, -1, -1
        min_cost = INF

        is_connected_cache = defaultdict(bool)
        def is_connected(s: Pos, t: Pos):
            k = (s, t) if s <= t else (t, s)
            if k in is_connected_cache:
                return is_connected_cache[k]
            res = self.field.is_connected(s, t)
            is_connected_cache[k] = res
            return res

        for dist, person_idx in self.person_idxs[::-1]:
            if is_connected(self.home[person_idx], self.workplace[person_idx]):
                continue

            rest_of_turn = self.T - (len(self.actions)+1+dist)
            
            home_around_station = self.field.collect_stations(self.home[person_idx])
            workplace_around_station = self.field.collect_stations(self.workplace[person_idx])

            if home_around_station and workplace_around_station:
                rail_count = self.money // COST_RAIL   
                for home in home_around_station:
                    for workplace in workplace_around_station:    
                        dist = distance(home, workplace)
                        tmp_cost = (dist-1)*COST_RAIL
                        if ((dist < rail_count or 100 < income) and
                            tmp_cost < dist*rest_of_turn and 
                            not is_connected(home, workplace) and
                            tmp_cost < min_cost
                        ):
                            r0, c0, r1, c1 = *home, *workplace
                            min_cost = tmp_cost

            elif home_around_station or workplace_around_station:
                rail_count = (self.money - COST_STATION) // COST_RAIL  
                new_station = self.home[person_idx] if not home_around_station else self.workplace[person_idx] 
                tmp_return = distance(self.home[person_idx], self.workplace[person_idx])*rest_of_turn
                
                for exist_station in self.station:    
                    dist = distance(new_station, exist_station)
                    tmp_cost = COST_STATION + (dist-1)*COST_RAIL
                    if ((dist < rail_count or 100 < income) and
                        tmp_cost < tmp_return and
                        not is_connected(new_station, exist_station) and
                        tmp_cost < min_cost
                    ):
                        r0, c0, r1, c1 = *new_station, *exist_station
                        min_cost = tmp_cost
            else:
                tmp_cost = 2*COST_STATION + (dist-1)*COST_RAIL
                rail_count = (self.money - 2*COST_STATION) // COST_RAIL
                if (dist < rail_count and
                    tmp_cost < dist*rest_of_turn and
                    not is_connected(self.home[person_idx], self.workplace[person_idx])
                ):
                    r0, c0, r1, c1 = *self.home[person_idx], *self.workplace[person_idx]
            if -1 < r0:
                break
        return r0, c0, r1, c1
    
    def find_best_rectangular_route(self, r0, c0, r1, c1) -> list[tuple[int, int, int]]:
        
        def generate_path(path: list[tuple[int, int]]) -> list[tuple[int, int, int]]:
            typed_path = [[STATION, path[0][0], path[0][1]]]
            for i in range(1, len(path) - 1):
                pr, pc = path[i - 1]  # 1つ前の座標
                r, c = path[i]        # 現在の座標
                nr, nc = path[i + 1]  # 次の座標

                # どこから来たか
                if pr < r:  # 上から来た
                    from_dir = "UP"
                elif pr > r:  # 下から来た
                    from_dir = "DOWN"
                elif pc < c:  # 左から来た
                    from_dir = "LEFT"
                else:  # 右から来た
                    from_dir = "RIGHT"

                # どこへ行くか
                if nr > r:  # 下へ行く
                    to_dir = "DOWN"
                elif nr < r:  # 上へ行く
                    to_dir = "UP"
                elif nc > c:  # 右へ行く
                    to_dir = "RIGHT"
                else:  # 左へ行く
                    to_dir = "LEFT"

                if self.field.rail_type(r, c) == STATION:
                    rail_type = PASS
                elif self.field.rail_type(r, c) == EMPTY:
                    # 直線レール
                    if from_dir in ("LEFT", "RIGHT") and to_dir in ("LEFT", "RIGHT"):
                        rail_type = RAIL_HORIZONTAL
                    elif from_dir in ("UP", "DOWN") and to_dir in ("UP", "DOWN"):
                        rail_type = RAIL_VERTICAL
                    
                    # カーブレール
                    elif (from_dir == "LEFT" and to_dir == "DOWN") or (from_dir == "DOWN" and to_dir == "LEFT"):
                        rail_type = RAIL_LEFT_DOWN
                    elif (from_dir == "LEFT" and to_dir == "UP") or (from_dir == "UP" and to_dir == "LEFT"):
                        rail_type = RAIL_LEFT_UP
                    elif (from_dir == "RIGHT" and to_dir == "UP") or (from_dir == "UP" and to_dir == "RIGHT"):
                        rail_type = RAIL_RIGHT_UP
                    elif (from_dir == "RIGHT" and to_dir == "DOWN") or (from_dir == "DOWN" and to_dir == "RIGHT"):
                        rail_type = RAIL_RIGHT_DOWN
                else:
                    rail_type = STATION
                typed_path.append([rail_type, r, c])

            typed_path.append([STATION, path[-1][0], path[-1][1]])
            return typed_path

        # 縦→横ルート
        vertical_first = []
        if r0 <= r1:
            vertical_first += [[r, c0] for r in range(r0, r1 + 1)]
        else:
            vertical_first += [[r, c0] for r in range(r0, r1 - 1, -1)]

        if c0 <= c1:
            vertical_first.extend([[r1, c] for c in range(c0 + 1, c1 + 1)])
        else:
            vertical_first.extend([[r1, c] for c in range(c0 - 1, c1 - 1, -1)])

        # 横→縦ルート
        horizontal_first = []
        if c0 <= c1:
            horizontal_first += [[r0, c] for c in range(c0, c1 + 1)]
        else:
            horizontal_first += [[r0, c] for c in range(c0, c1 - 1, -1)]

        if r0 <= r1:
            horizontal_first.extend([[r, c1] for r in range(r0 + 1, r1 + 1)])
        else:
            horizontal_first.extend([[r, c1] for r in range(r0 - 1, r1 - 1, -1)])

        # ルートのスコアを評価
        typed_vertical = generate_path(vertical_first)
        typed_horizontal = generate_path(horizontal_first)

        score_v = self.evaluate_route(typed_vertical)
        score_h = self.evaluate_route(typed_horizontal)

        # スコアが低い方を選択
        return typed_vertical if score_v < score_h else typed_horizontal
    
    def evaluate_route(self, path: list[Pos]) -> int:
        score = 0
        for type, r, c in path:
            if self.field.rail_type(r, c) == STATION:
                if self.field.is_connected((r, c), path[-1]):
                    return score
            elif self.field.rail_type(r, c) == EMPTY:
                score += COST_RAIL
            else:
                score += COST_STATION
                if self.field.is_connected((r, c), path[-1]):
                    return score
        return score

    def build_route(self, path) -> None:
        r0, c0, r1, c1 = path[0][1], path[0][2], path[-1][1], path[-1][2]
        income = self.calc_income()
        path = deque(path)
        while path:
            type, r, c = path.popleft()
            if self.field.rail_type(r, c) == STATION:
                continue

            if type == STATION:
                flg = self.field.rail_type(r, c)
                while self.money < COST_STATION:
                    if path:
                        nt, nr, nc = path.popleft()
                        if (nt not in (PASS, STATION) and 
                            COST_RAIL < self.money):
                            self.build_rail(nt, nr, nc)
                        else:
                            path.appendleft((nt, nr, nc))
                            self.build_nothing()
                    else:
                        self.build_nothing()
                    self.money += income
                    if self.is_quit():
                        print(Result(self.actions, self.money))
                        sys.exit(0)
                self.build_station(r, c)
                income = self.calc_income()
                if flg != EMPTY:
                    self.money += income
                    return
            elif type == PASS:
                pass
            else:
                while self.money <= COST_RAIL:
                    self.build_nothing()
                    self.money += income
                    if self.is_quit():
                        print(Result(self.actions, self.money))
                        sys.exit(0)
                self.build_rail(type, r, c)
            self.money += income

            if self.field.is_connected((r0, c0), (r1, c1)):
                return

            if self.is_quit():
                print(Result(self.actions, self.money))
                sys.exit(0)

    def search_candidate_place(self):
        for r in range(self.N):
            for c in range(self.N):
                tmp = {"home": set(), "workplace": set()}
                for dr, dc in SEARCH_ZONE:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < self.N) or not (0 <= nc < self.N):
                        continue
                    if (nr, nc) in self.pos2home:
                        tmp["home"].add(self.pos2home.get((nr, nc)))
                    if (nr, nc) in self.pos2workplace:
                        tmp["workplace"].add(self.pos2workplace.get((nr, nc)))
                    
                if tmp["home"] or tmp["workplace"]:
                    self.candidate_place.append([r, c, tmp])

    def init_search(self) -> tuple[int, int, int, int]:
        r0, c0, r1, c1 = -1, -1, -1, -1
        min_cost = INF
        max_return_money = 0
        self.search_candidate_place()
        cnt = 0
        while r0 < 0 or cnt < 10000:
            if time.time()-S_TIME > 2.75:
                return -1, -1, -1, -1
            (fromr, fromc, frominfo), (tor, toc, toinfo) = random.sample(self.candidate_place, 2)
            dist = distance((fromr, fromc), (tor, toc))
            cost = COST_STATION*2 + (dist-1)*COST_RAIL
            if self.money < cost or dist < 5:
                continue
            from_homes: set = frominfo["home"]
            from_workplace: set = frominfo["workplace"]
            to_homes: set = toinfo["home"]
            to_workplace: set = toinfo["workplace"]
            disconnected_people = (from_homes & to_workplace) | (to_homes & from_workplace)
            if not disconnected_people:
                continue

            return_money = sum(distance((self.home[idx]), (self.workplace[idx]))
                                for idx in disconnected_people)

            if (cost < return_money*(self.T-dist) and
                max_return_money/min_cost < return_money*(self.T-(dist))/cost):
                r0, c0, r1, c1 = fromr, fromc, tor, toc
                min_cost = cost       
                max_return_money = return_money*(self.T-(dist-1)) 
            cnt += 1
        return r0, c0, r1, c1

    def solve(self) -> Result:
        # main loop
        income = 0
        # 最初の探索のみランダム
        r0, c0, r1, c1 = self.init_search()
        if r0 < 0:
            pass
        else:
            path = self.find_best_rectangular_route(r0, c0, r1, c1)
            self.build_route(path)
            while len(self.actions) < self.T:    
                if time.time()-S_TIME > 2.90:
                    break 
                income = self.calc_income()
                # 経路探索
                r0, c0, r1, c1 = self.search_station()  
                if r0 < 0:
                    if self.money < COST_STATION:
                        rest_turn = (COST_STATION-self.money + income)//income
                        for _ in range(rest_turn):
                            self.build_nothing()
                            self.money += income                            
                        continue
                    else:
                        self.build_nothing()
                        self.money += income
                        continue                  
                # 経路評価
                path = self.find_best_rectangular_route(r0, c0, r1, c1)
                self.build_route(path)
                income = self.calc_income()

        # あとは待機
        income = self.calc_income()
        while len(self.actions) < self.T:
            self.build_nothing()
            self.money += income

        print(Result(self.actions, self.money))
        sys.exit(0)

def main():
    N, M, K, T = map(int, input().split())
    home = []
    workplace = []
    for _ in range(M):
        r0, c0, r1, c1 = map(int, input().split())
        home.append((r0, c0))
        workplace.append((r1, c1))

    solver = Solver(N, M, K, T, home, workplace)
    solver.solve()

if __name__ == "__main__":
    main()
