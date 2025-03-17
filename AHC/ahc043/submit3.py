# -*- coding: utf-8 -*-

import sys
from collections import deque
from itertools import combinations, combinations_with_replacement
from functools import lru_cache
from bisect import bisect_left
import time
import copy

Pos = tuple[int, int]
EMPTY = -1
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
INF = 1 << 60
input = sys.stdin.readline

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


@lru_cache(None)
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
        self.rail = [[EMPTY] * N for _ in range(N)]
        self.uf = UnionFind(N)

    def build(self, type: int, r: int, c: int) -> None:
        if 1 <= type <= 6:
            if self.rail[r][c] != EMPTY:
                raise ValueError(f"Rail type {type} cannot be built on non-empty cell ({r}, {c})")
        self.rail[r][c] = type

        # 隣接する区画と接続
        # 上
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
            if r > 0 and self.rail[r - 1][c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
                self.uf.unite((r, c), (r - 1, c))
        # 下
        if type in (STATION, RAIL_VERTICAL, RAIL_LEFT_DOWN, RAIL_RIGHT_DOWN):
            if r < self.N - 1 and self.rail[r + 1][c] in (STATION, RAIL_VERTICAL, RAIL_LEFT_UP, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r + 1, c))
        # 左
        if type in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
            if c > 0 and self.rail[r][c - 1] in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
                self.uf.unite((r, c), (r, c - 1))
        # 右
        if type in (STATION, RAIL_HORIZONTAL, RAIL_RIGHT_DOWN, RAIL_RIGHT_UP):
            if c < self.N - 1 and self.rail[r][c + 1] in (STATION, RAIL_HORIZONTAL, RAIL_LEFT_DOWN, RAIL_LEFT_UP):
                self.uf.unite((r, c), (r, c + 1))

    def is_connected(self, s: Pos, t: Pos) -> bool:
        stations0 = self.collect_stations(s)
        stations1 = self.collect_stations(t)
        for station0 in stations0:
            for station1 in stations1:
                if self.uf.is_same(station0, station1):
                    return True
        return False

    def collect_stations(self, pos: Pos) -> list[Pos]:
        stations = []
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if abs(dr) + abs(dc) > 2:
                    continue
                r = pos[0] + dr
                c = pos[1] + dc
                if 0 <= r < self.N and 0 <= c < self.N and self.rail[r][c] == STATION:
                    stations.append((r, c))
        return stations


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
        self.pos2station = [-1]*(N*N)
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
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                if abs(dr) + abs(dc) > 2:
                    continue
                tr = r + dr
                tc = c + dc
                if 0 <= tr < self.N and 0 <= tc < self.N:
                    if (tr, tc) in self.pos2home:
                        self.pos2station[tr*self.N+tc] = (r, c)
                    if (tr, tc) in self.pos2workplace:
                        self.pos2station[tr*self.N+tc] = (r, c)
        self.actions.append(Action(STATION, (r, c)))

    def build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
    
    def is_quit(self) -> None:
        return not (len(self.actions) < self.T)

    def search_station(self):
        r0, c0, r1, c1 = -1, -1, -1, -1
        tmp_idx = self.M-1
        while -1 < tmp_idx:
            dist, person_idx = self.person_idxs[tmp_idx]
            if self.field.is_connected(self.home[person_idx], self.workplace[person_idx]):
                tmp_idx -= 1
                continue
            rest_of_turn = 800-(len(self.actions)+1+dist)
            
            home_around_station = self.field.collect_stations(self.home[person_idx])
            workplace_around_station = self.field.collect_stations(self.workplace[person_idx])
            flg = 0
            if home_around_station and workplace_around_station:
                rail_count = self.money // COST_RAIL   
                min_cost = INF
                for home in home_around_station:
                    for workplace in workplace_around_station:    
                        dist = distance(home, workplace)
                        tmp_cost = (dist-1)*COST_RAIL
                        if dist < rail_count\
                            and tmp_cost < dist*rest_of_turn\
                            and not self.field.is_connected(home, workplace):
                            if tmp_cost < min_cost:
                                r0, c0 = home
                                r1, c1 = workplace
                                min_cost = tmp_cost
                                flg = 1
            elif home_around_station or workplace_around_station:
                rail_count = (self.money - COST_STATION) // COST_RAIL   
                if not home_around_station:
                    new_station = self.home[person_idx]
                if not workplace_around_station:
                    new_station = self.workplace[person_idx]                    
                min_cost = INF
                tmp_return = distance(self.home[person_idx], self.workplace[person_idx])*rest_of_turn
                # print(f"# {len(set(self.station))}")
                for exist_station in self.station:    
                    dist = distance(new_station, exist_station)
                    tmp_cost = COST_STATION + (dist-1)*COST_RAIL
                    # print(f"# {tmp_cost < min_cost} {dist < rail_count} {tmp_cost < dist*rest_of_turn} {not self.field.is_connected(new_station, exist_station)}, {new_station}, {exist_station}")
                    if dist < rail_count\
                        and tmp_cost < tmp_return\
                        and not self.field.is_connected(new_station, exist_station):
                        if tmp_cost < min_cost:
                            r0, c0 = new_station
                            r1, c1 = exist_station
                            min_cost = tmp_cost
                            flg = 1
            else:
                tmp_cost = 2*COST_STATION + (dist-1)*COST_RAIL
                rail_count = (self.money - 2*COST_STATION) // COST_RAIL
                if dist < rail_count\
                    and tmp_cost < dist*rest_of_turn\
                    and not self.field.is_connected(self.home[person_idx], self.workplace[person_idx]):
                    r0, c0 = self.home[person_idx]
                    r1, c1 = self.workplace[person_idx]
                    flg = 1
            if flg:
                break
            tmp_idx -= 1
        # print(f"#({r0}, {c0}), ({r1}, {c1})")
        return r0, c0, r1, c1

    def build_vertical(self, r0, c0, r1, c1):
        income = self.calc_income()
        rr0, cc0, rr1, cc1 = r0, c0, r1, c1
        # r0 < r1に固定
        if r1 < r0:
            r0, c0, r1, c1 = r1, c1, r0, c0
        # r0 -> r1
        r = r0 + 1
        while r < r1:
            if self.field.rail[r][c0] == EMPTY:
                if COST_RAIL <= self.money:
                    self.build_rail(RAIL_VERTICAL, r, c0)
                    r += 1
                else:
                    self.build_nothing()
            elif self.field.rail[r][c0] == STATION:
                r += 1
                continue
            else:
                if 0 < r < self.N-1\
                    and self.field.rail[r-1][c0] in (STATION, RAIL_VERTICAL)\
                    and self.field.rail[r][c0] in (STATION, RAIL_VERTICAL)\
                    and self.field.rail[r+1][c0] in (STATION, RAIL_VERTICAL):
                    r += 1
                    continue
                if self.field.rail[r][c0] == RAIL_VERTICAL:
                    r += 1
                    continue
                elif COST_STATION <= self.money:
                    self.build_station(r, c0)
                    income = self.calc_income()
                    if self.field.is_connected((rr0, cc0), (rr1, cc1)):
                        self.money += income
                        return True
                    r += 1
                else:
                    self.build_nothing()
            self.money += income
            if self.is_quit():
                print(Result(self.actions, self.money))
                sys.exit(0)
        return False

    def init_station(self, r0, c0, r1, c1):
            income = self.calc_income()
            if self.field.rail[r0][c0] != STATION:
                while self.money < COST_STATION:
                    self.build_nothing()
                    self.money += income
                    if self.is_quit():
                        print(Result(self.actions, self.money))
                        sys.exit(0)
                self.build_station(r0, c0)
                income = self.calc_income()
                self.money += income
                if self.is_quit():
                    print(Result(self.actions, self.money))
                    sys.exit(0)
            return self.field.is_connected((r0, c0), (r1, c1))

    def build_joint(self, r0, c0, r1, c1):
        income = self.calc_income()
        rr0, cc0, rr1, cc1 = r0, c0, r1, c1
        if r1 < r0:
            r0, c0, r1, c1 = r1, c1, r0, c0
        if self.field.rail[r1][c0] != STATION:
            while 1:
                if self.field.rail[r1][c0] == EMPTY:
                    if COST_RAIL < self.money:
                        if c0 < c1 :
                            self.build_rail(RAIL_RIGHT_UP, r1, c0)
                        elif c0 > c1:
                            self.build_rail(RAIL_LEFT_UP, r1, c0)
                        self.money += income
                        if self.is_quit():
                            print(Result(self.actions, self.money))
                            sys.exit(0)
                        break
                    else:
                        self.build_nothing()           
                else:
                    if COST_STATION < self.money:
                        self.build_station(r1, c0)
                        income = self.calc_income()
                        self.money += income
                        if self.is_quit():
                            print(Result(self.actions, self.money))
                            sys.exit(0)
                        break
                    else:
                        self.build_nothing()
                self.money += income
                if self.is_quit():
                    print(Result(self.actions, self.money))
                    sys.exit(0)
        return self.field.is_connected((rr0, cc0), (rr1, cc1))

    def build_horizontal(self, r0, c0, r1, c1):
        income = self.calc_income()
        rr0, cc0, rr1, cc1 = r0, c0, r1, c1
        if r1 < r0:
            r0, c0, r1, c1 = r1, c1, r0, c0
        if c1 < c0:
            c0, c1 = c1, c0 
        c = c0+1
        while c < c1:
            if self.field.rail[r1][c] == EMPTY:
                if COST_RAIL < self.money:
                    self.build_rail(RAIL_HORIZONTAL, r1, c)
                    c += 1
                else:
                    self.build_nothing()
            elif self.field.rail[r1][c] == STATION:
                c += 1
                continue
            else:                    
                if 0 < c < self.N-1\
                    and self.field.rail[r1][c-1] in (STATION, RAIL_HORIZONTAL)\
                    and self.field.rail[r1][c] in (STATION, RAIL_HORIZONTAL)\
                    and self.field.rail[r1][c+1] in (STATION, RAIL_HORIZONTAL):
                    c += 1
                    continue
                if self.field.rail[r1][c] ==RAIL_HORIZONTAL:
                    c += 1
                    continue
                elif COST_STATION < self.money:
                        self.build_station(r1, c)
                        income = self.calc_income()
                        c += 1
                else:
                    self.build_nothing()
            self.money += income
            if self.field.is_connected((rr0, cc0), (rr1, cc1)):
                return
            if self.is_quit():
                print(Result(self.actions, self.money))
                sys.exit(0)

    def solve(self) -> Result:
        # main loop
        income = 0
        init = 1
        while len(self.actions) < self.T:
            if self.money < 2*COST_STATION:
                self.build_nothing()
                self.money += income
                continue         

            r0, c0, r1, c1 = self.search_station()
            if r0 < 0:
                if init:
                    break
                self.build_nothing()
                self.money += income
                continue
            init = 0
                
            # 駅の配置
            if self.init_station(r0, c0, r1, c1):
                continue
            if self.init_station(r1, c1, r0, c0):
                continue

            # 縦方向に設置
            if self.build_vertical(r0, c0, r1, c1):
                continue

            if self.build_joint(r0, c0, r1, c1):
                continue

            self.build_horizontal(r0, c0, r1, c1)
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
