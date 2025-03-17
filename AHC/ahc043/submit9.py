# -*- coding: utf-8 -*-

#library
from heapq import heappush, heappop
from collections import deque
import random
import sys
import time
S_TIME = time.time()

# setting
input = sys.stdin.readline
random.seed(42)

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
SEARCH_ZONE = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), 
               (0, 0), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)]
SEARCH_ZONE_WEIGHT = [1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1]
RAIL_MAPPING = {
        ("LEFT", "RIGHT"): RAIL_HORIZONTAL, ("RIGHT", "LEFT"): RAIL_HORIZONTAL,
        ("UP", "DOWN"): RAIL_VERTICAL, ("DOWN", "UP"): RAIL_VERTICAL,
        ("LEFT", "DOWN"): RAIL_LEFT_DOWN, ("DOWN", "LEFT"): RAIL_LEFT_DOWN,
        ("LEFT", "UP"): RAIL_LEFT_UP, ("UP", "LEFT"): RAIL_LEFT_UP,
        ("RIGHT", "UP"): RAIL_RIGHT_UP, ("UP", "RIGHT"): RAIL_RIGHT_UP,
        ("RIGHT", "DOWN"): RAIL_RIGHT_DOWN, ("DOWN", "RIGHT"): RAIL_RIGHT_DOWN
    }
INF = 1 << 30

def timer(f):
    def in_f(*args, **kwargs):
        s = time.time()
        res = f(*args, **kwargs)
        print(f"# {time.time()-s}")
        return res
    return in_f

def distance(a, b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.history =[]
        self.inner_snap = 0
        self.parents = [-1 for _ in range(n * n)]
    
    def _find_root(self, idx: int) -> int:
        while 0 <= self.parents[idx]:
            idx = self.parents[idx]
        return idx

    def is_same(self, p: tuple[int, int], q: tuple[int, int]) -> bool:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        return self._find_root(p_idx) == self._find_root(q_idx)
    
    def unite(self, p: tuple[int, int], q: tuple[int, int]) -> None:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        p_root = self._find_root(p_idx)
        q_root = self._find_root(q_idx)
        self.history.append((p_root, self.parents[p_root], q_root, self.parents[q_root]))
        if p_root != q_root:
            p_size = -self.parents[p_root]
            q_size = -self.parents[q_root]
            if p_size > q_size:
                p_root, q_root = q_root, p_root
            self.parents[q_root] += self.parents[p_root]
            self.parents[p_root] = q_root
    
    def snapshot(self):
        self.inner_snap = len(self.history)

    def undo(self):
        if not self.history:
            return
        p, dp, q, dq = self.history.pop()
        self.parents[q] = dq
        self.parents[p] = dp
    
    def rollback(self, state: int=-1):
        if state == -1:
            state = self.inner_snap
        assert state <= len(self.history)
        while state < len(self.history):
            self.undo()


class Action:
    def __init__(self, type: int, pos: tuple[int, int]):
        self.type = type
        self.pos = pos

    def __str__(self):
        if self.type == DO_NOTHING:
            return "-1"
        else:
            return f"{self.type} {self.pos[0]} {self.pos[1]}"


class Result:
    def __init__(self, actions: list[Action], score: int):
        self.actions = actions[:800]
        self.score = score

    def __str__(self):
        return "\n".join(map(str, self.actions))

class Field:
    def __init__(self, N: int):
        self.N = N
        self.rail = [EMPTY for _ in range(N*N)]
        self.uf = UnionFind(N)
        self.stations = set()
    
    def build(self, type: int, r: int, c: int) -> None:
        if 1 <= type <= 6:
            if self.rail[r*self.N+c] != EMPTY:
                raise ValueError(f"Rail type {type} cannot be built on non-empty cell ({r}, {c})")
        self.rail[r*self.N+c] = type

        if type == STATION:
            self.stations.add((r, c))
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
    
    def is_connected(self, s: tuple[int, int], t: tuple[int, int]) -> bool:
        stations0 = self.collect_stations(s)
        stations1 = self.collect_stations(t)
        for station0 in stations0:
            for station1 in stations1:
                if self.uf.is_same(station0, station1):
                    return True
        return False
    
    def rail_type(self, r: int, c: int) -> int:
        return self.rail[r*self.N+c]

    def collect_stations(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        return [s for s in self.stations if distance(pos, s) <= 2]


class Solver:
    def __init__(self, N: int, M: int, K: int, T: int, home: list[tuple[int, int]], workplace: list[tuple[int, int]]):
        self.N = N
        self.M = M
        self.K = K
        self.T = T
        self.income = 0
        self.home = home
        self.workplace = workplace
        self.field = Field(N)
        self.money = K
        self.actions = []
        self.person_idxs = []
        self.station = []
        self.candidate_place = []
        self.around_home_workplace = [set() for _ in range(N*N)]
        self.pos2home = [-1]*(self.N*self.N)
        self.pos2workplace = [-1]*(self.N*self.N)
        self.dist_cache = [0]*self.M
        
        # prepare
        for person_idx in range(self.M):
            home_pos, workplace_pos = self.home[person_idx], self.workplace[person_idx]
            person_dist = distance(home_pos, workplace_pos)
            self.pos2home[home_pos[0]*self.N+home_pos[1]] = person_idx
            self.pos2workplace[workplace_pos[0]*self.N+workplace_pos[1]] = person_idx 
            self.dist_cache[person_idx] = person_dist
            for dr, dc in SEARCH_ZONE:
                hr, hc = home_pos[0]+dr, home_pos[1]+dc 
                wr, wc = workplace_pos[0]+dr, workplace_pos[1]+dc
                if 0 <= hr < self.N and 0 <= hc < self.N:
                    self.around_home_workplace[hr*self.N+hc].add(person_idx)
                if 0 <= wr < self.N and 0 <= wc < self.N:
                    self.around_home_workplace[wr*self.N+wc].add(person_idx)
        for person_idx in range(self.M):
            (hr, hc), (wr, wc) = self.home[person_idx], self.workplace[person_idx]
            total_dist = 0
            for around_idx in (self.around_home_workplace[hr*self.N+hc] & self.around_home_workplace[wr*self.N+wc]):
                total_dist += self.dist_cache[around_idx]
            heappush(self.person_idxs, (-total_dist, person_idx))
    @timer
    def calc_income(self) -> int:
        income = 0
        for i in range(self.M):
            if self.field.is_connected(self.home[i], self.workplace[i]):
                income += self.dist_cache[i]
        self.income = income

    def build_rail(self, type: int, r: int, c: int) -> None:
        self.field.build(type, r, c)
        self.money -= COST_RAIL
        self.actions.append(Action(type, (r, c)))

    def build_station(self, r: int, c: int) -> None:
        self.field.build(STATION, r, c)
        self.money -= COST_STATION
        self.station.append((r, c))
        self.actions.append(Action(STATION, (r, c)))

    def build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
    
    def is_quit(self) -> None:
        return not (len(self.actions) < self.T)

    def is_connected(self, s: tuple[int, int], t: tuple[int, int]):
        return self.field.is_connected(s, t)
    
    def calc_score(self, nhr: int, nhc: int, nwr: int, nwc: int):
        # 最適なパスの計算と前状態の保存
        path = self.find_best_rectangular_route(nhr, nhc, nwr, nwc)
        pre_state = self.field.rail[nhr*self.N+nhc]
        _r0, _c0, _r1, _c1 = *path[0][1:], *path[-1][1:]
        # 接続した場合
        if (_r0, _c0) not in self.field.stations:
            self.field.stations.add((_r0, _c0))
        self.field.uf.unite((_r0, _c0), (_r1, _c1))
        self.calc_income()
        _income = self.income
        # rollback
        self.field.uf.rollback(-1)
        if pre_state != STATION:
            self.field.stations.discard((_r0, _c0))
        self.calc_income()
        # calc 
        tmp0 = 0 if self.field.rail_type(_r0, _c0) == EMPTY else 1
        tmp1 = 0 if self.field.rail_type(_r1, _c1) == EMPTY else 1
        cost = COST_STATION*(tmp0+tmp1) + (len(path)-2)*COST_RAIL
        score = self.money - cost + _income*(self.T-(len(self.actions)+len(path)-2))

        return score, cost, path
    
    def single_simulater(self, person_idx: int, max_score: int) -> list[tuple[int,int]]:
        max_path = None
        if self.is_connected(self.home[person_idx], self.workplace[person_idx]):
            return max_score, max_path

        home_around_station = self.field.collect_stations(self.home[person_idx])
        workplace_around_station = self.field.collect_stations(self.workplace[person_idx])

        self.field.uf.snapshot()
        if home_around_station or workplace_around_station:
            (nhr, nhc) = self.home[person_idx] if not home_around_station else self.workplace[person_idx] 
            (nwr, nwc) = random.choice(self.station)
            if not self.is_connected((nhr, nhc), (nwr, nwc)):            
                score, cost, path = self.calc_score(nhr, nhc, nwr, nwc)
                if (self.money < cost or 100 < self.income) and max_score < score:
                    max_score, max_path = score, path
        
        home, workplace = self.home[person_idx], self.workplace[person_idx]
        hr, hc, wr, wc = *home, *workplace
        nhr, nhc ,nwr, nwc = -1, -1, -1, -1

        # ランダムに座標をずらす
        while not (0 <= nhr < self.N) or not (0 <= nhc < self.N):
            (dhr, dhc) = random.choices(SEARCH_ZONE, k=1, weights=SEARCH_ZONE_WEIGHT)[0]
            nhr, nhc = hr+dhr, hc+dhc
        while not (0 <= nwr < self.N) or not (0 <= nwc < self.N):
            (dwr, dwc) = random.choices(SEARCH_ZONE, k=1, weights=SEARCH_ZONE_WEIGHT)[0]
            nwr, nwc = wr+dwr, wc+dwc                  

        # スコアの算出
        score, cost, path = self.calc_score(nhr, nhc, nwr, nwc)
        if (cost < self.money or 100 < self.income) and max_score < score:
            max_score, max_path = score, path
        return max_score, max_path
    
    def search_station(self) -> tuple[int, int, int, int]:
        self.calc_income()
        max_score = self.money + self.income*(self.T-len(self.actions))                          
        max_path = None
        stack = []
        for _ in range(30):
            p_score, p_idx = heappop(self.person_idxs)
            if self.field.is_connected(self.home[p_idx], self.workplace[p_idx]):
                continue
            stack.append((p_score, p_idx))
            new_score, path = self.single_simulater(p_idx, max_score)
            if max_score < new_score:
                max_score, max_path = new_score, path
        for (p_score, p_idx) in stack: 
            heappush(self.person_idxs, (p_score, p_idx))
        return max_path
    
    def find_best_rectangular_route(self, r0: int, c0: int, r1: int, c1: int) -> list[tuple[int, int, int]]:
        def generate_path(path: list[tuple[int, int]]) -> list[tuple[int, int, int]]:
            typed_path = [[STATION, path[0][0], path[0][1]]]
            for (pr, pc), (r, c), (nr, nc) in zip(path, path[1:], path[2:]):

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

                cell_type = self.field.rail_type(r, c)
                if cell_type == STATION:
                    typed_path.append([PASS, r, c])
                    return typed_path
                elif cell_type == EMPTY:
                    rail_type = RAIL_MAPPING[(from_dir, to_dir)]
                else:
                    rail_type = STATION
                    typed_path.append([rail_type, r, c])
                    return typed_path
                typed_path.append([rail_type, r, c])


            typed_path.append([STATION, path[-1][0], path[-1][1]])
            return typed_path

        # 縦→横ルート
        vertical_first = [[r, c0] for r in (range(r0, r1 + 1) if r0 <= r1 else range(r0, r1 - 1, -1))]
        vertical_first.extend([[r1, c] for c in (range(c0 + 1, c1 + 1) if c0 <= c1 else range(c0 - 1, c1 - 1, -1))])

        # 横→縦ルート
        horizontal_first = [[r0, c] for c in (range(c0, c1 + 1) if c0 <= c1 else range(c0, c1 - 1, -1))]
        horizontal_first.extend([[r, c1] for r in (range(r0 + 1, r1 + 1) if r0 <= r1 else range(r0 - 1, r1 - 1, -1))])

        # ルートのスコアを評価
        typed_vertical = generate_path(vertical_first)
        typed_horizontal = generate_path(horizontal_first)

        score_v = self.evaluate_route(typed_vertical)
        score_h = self.evaluate_route(typed_horizontal)

        # スコアが低い方を選択
        return typed_vertical if score_v < score_h else typed_horizontal
    
    def evaluate_route(self, path: list[tuple[int, int]]) -> int:
        score = 0
        for _, r, c in path:
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

    def build_route(self, path: list[list[int, tuple[int, int]]]) -> None:
        r1, c1 = path[-1][1], path[-1][2]
        self.calc_income()
        path: deque = deque(path)
        pre_state = []
        while path:
            type, r, c = path.popleft()
            if self.field.rail_type(r, c) == STATION:
                continue

            if type == STATION:
                flg = self.field.rail_type(r, c)
                if self.money < COST_STATION:
                    if not self.field.is_connected((r, c), (r1, c1)):
                        while self.money < COST_STATION:
                            if (path and path[0][0] not in (PASS, STATION) 
                                and COST_RAIL < self.money):
                                nt, nr, nc = path.popleft()                                    
                                pre_state.append((nr, nc, self.field.rail_type(nr, nc)))
                                self.build_rail(nt, nr, nc)
                            else:
                                self.build_nothing()
                            self.money += self.income
                            if self.is_quit():
                                return pre_state
                    else:
                        wait_turn = (COST_STATION-self.money+self.income)//self.income
                        for _ in range(wait_turn):
                            self.build_nothing()
                            self.money += self.income
                pre_state.append((r, c, flg))
                self.build_station(r, c)
                self.calc_income()
                if flg != EMPTY:
                    self.money += self.income
                    return pre_state
            elif type == PASS:
                pass
            else:
                while self.money < COST_RAIL:
                    self.build_nothing()
                    self.money += self.income
                    if self.is_quit():
                        return pre_state
                pre_state.append((r, c, EMPTY))
                self.build_rail(type, r, c)
            self.money += self.income

            if self.is_quit():
                return pre_state
        return pre_state

    def search_candidate_place(self) -> list[tuple[int, int]]:
        weight = []
        w = 0
        for r in range(self.N):
            for c in range(self.N):
                home_set = set()
                work_set = set()
                for dr, dc in SEARCH_ZONE:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < self.N) or not (0 <= nc < self.N):
                        continue
                    if -1 < self.pos2home[nr*self.N+nc]:
                        home_set.add(self.pos2home[nr*self.N+nc])
                    if -1 < self.pos2workplace[nr*self.N+nc]:
                        work_set.add(self.pos2workplace[nr*self.N+nc])
                    
                if home_set or work_set:
                    self.candidate_place.append([r, c, home_set, work_set])
                    w += len(home_set | work_set)
                    weight.append(w)
        return weight

    def init_search(self) -> tuple[int, int, int, int]:
        r0, c0, r1, c1 = -1, -1, -1, -1
        max_score = 0.0
        weight = self.search_candidate_place()
        cnt = 0
        while r0 < 0 or cnt < 3000:
            if time.time()-S_TIME > 1.0:
                return r0, c0, r1, c1
            (fromr, fromc, from_homes, from_works), (tor, toc, to_homes, to_works) = random.choices(self.candidate_place, k=2, cum_weights=weight)
            dist = distance((fromr, fromc), (tor, toc))
            cost = COST_STATION*2 + (dist-1)*COST_RAIL
            if self.money < cost or dist < 5:
                continue
            disconnected_people = (from_homes & to_works) | (to_homes & from_works)
            if not disconnected_people:
                continue

            return_money = sum(self.dist_cache[idx]
                                for idx in disconnected_people)
            score = return_money*(self.T-(dist))/cost
            if (cost < return_money*(self.T-dist) and max_score < score):
                r0, c0, r1, c1 = fromr, fromc, tor, toc
                max_score = score
            cnt += 1
        return r0, c0, r1, c1

    def solve(self) -> None:
        # main loop
        # 最初の探索のみランダム
        r0, c0, r1, c1 = self.init_search()
        if r0 < 0:
            pass
        else:
            path = self.find_best_rectangular_route(r0, c0, r1, c1)
            self.build_route(path)
            while len(self.actions) < self.T:   
                if time.time()-S_TIME > 2.7:
                    break 
                self.calc_income()
                # 経路探索
                path = self.search_station()  
                if path is None:
                    if self.money < COST_STATION:
                        rest_turn = (COST_STATION-self.money + self.income)//self.income
                        for _ in range(rest_turn):
                            self.build_nothing()
                            self.money += self.income                            
                        continue
                    else:
                        self.build_nothing()
                        self.money += self.income
                        continue                  
                # 経路評価
                self.build_route(path)
                self.calc_income()

        # あとは待機
        self.calc_income()
        print(f"# {len(self.actions)}") 
        while len(self.actions) < self.T:
            self.build_nothing()
            self.money += self.income

        print(Result(self.actions, self.money))
        return
    
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
