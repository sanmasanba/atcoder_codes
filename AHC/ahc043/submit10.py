# -*- coding: utf-8 -*-

#library
from bisect import bisect, bisect_left, bisect_right
from collections import deque, Counter, defaultdict
import copy
from functools import lru_cache, cmp_to_key, reduce
from heapq import heappush, heappop
from itertools import permutations, combinations, accumulate
import math
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial
from operator import mul
import random
import sys
import time
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
input = sys.stdin.readline
random.seed(42)

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
SEARCH_ZONE = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), 
               (0, 0), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)]
SEARCH_ZONE_WEIGHT = [1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1]
INF = 1 << 60

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [-1 for _ in range(n * n)]
    
    def _find_root(self, idx: int) -> int:
        if self.parents[idx] < 0:
            return idx
        self.parents[idx] = self._find_root(self.parents[idx])
        return self.parents[idx]

    def is_same(self, p: tuple[int, int], q: tuple[int, int]) -> bool:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        return self._find_root(p_idx) == self._find_root(q_idx)

    def unite(self, p: tuple[int, int], q: tuple[int, int]) -> None:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        p_idx = self._find_root(p_idx)
        q_idx = self._find_root(q_idx)
        if p_idx != q_idx:
            if self.parents[p_idx] > self.parents[q_idx]:
                p_idx, q_idx = q_idx, p_idx
            self.parents[p_idx] += self.parents[q_idx]
            self.parents[q_idx] = p_idx

@lru_cache(None)
def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
        return list(self.has_station[pos[0]*self.N+pos[1]])


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
        self.around_home_work = [set() for _ in range(N*N)]
        self.pos2home = [-1]*(self.N*self.N)
        self.pos2workplace = [-1]*(self.N*self.N)
        self.dist_cache = [0]*self.M
        self.weight = [0]*self.M
        
        # prepare
        for person_idx in range(self.M):
            home_pos, workplace_pos = self.home[person_idx], self.workplace[person_idx]
            person_dist = distance(home_pos, workplace_pos)
            self.person_idxs.append((-person_dist, person_idx))
            self.pos2home[home_pos[0]*self.N+home_pos[1]] = person_idx
            self.pos2workplace[workplace_pos[0]*self.N+workplace_pos[1]] = person_idx 
            self.dist_cache[person_idx] = person_dist
            for dr, dc in SEARCH_ZONE:
                hr, hc = home_pos[0]+dr, home_pos[1]+dc 
                wr, wc = workplace_pos[0]+dr, workplace_pos[1]+dc
                if 0 <= hr < self.N and 0 <= hc < self.N:
                    self.around_home_work[hr*self.N+hc].add(person_idx)
                if 0 <= wr < self.N and 0 <= wc < self.N:
                    self.around_home_work[wr*self.N+wc].add(person_idx)
        for person_idx in range(self.M):
            (hr, hc), (wr, wc) = self.home[person_idx], self.workplace[person_idx]
            total_dist = 0
            for around_idx in (self.around_home_work[hr*self.N+hc] & self.around_home_work[wr*self.N+wc]):
                total_dist += self.dist_cache[around_idx]
            self.weight[person_idx] = total_dist

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

    def is_connected(self, s: tuple[int, int], t: tuple[int, int]):
        return self.field.is_connected(s, t)

    def calc_param(self, places1, places2):
            return len([i for i in places1 & places2 if not self.field.is_connected(self.home[i], self.workplace[i])])

    def calc_score(self, unique_people_num: int, cost: int, return_money: int) -> float:
        return (return_money*(1+0.01*unique_people_num))/cost

    def select_target_stations(self, new_station, k):
        distances = []
        for station in self.station:
            dist = distance(new_station, station)
            if 2 < dist:
                distances.append((dist, station))
        distances.sort()
        target_stations = [station for _, station in distances[:k]]
        return target_stations

    def single_simulater(self, person_dist, person_idx, max_score):
        r0, c0, r1, c1 = -1, -1, -1, -1
        dist = person_dist*-1
        if self.is_connected(self.home[person_idx], self.workplace[person_idx]):
            self.weight[person_idx] = 0
            return -1, -1, -1, -1, max_score

        rest_of_turn = self.T - (len(self.actions)+1+dist)
        home_around_station = self.field.collect_stations(self.home[person_idx])
        workplace_around_station = self.field.collect_stations(self.workplace[person_idx])

        if home_around_station:
            rail_count = (self.money - COST_STATION) // COST_RAIL  
            (r, c) = self.workplace[person_idx] 
            dr, dc = random.choices(SEARCH_ZONE, k=1, weights=SEARCH_ZONE_WEIGHT)[0]
            new_station = (r, c)
            if 0 <= r+dr < self.N and 0 <= c+dc < self.N:
                new_station = (r+dr, c+dc)
            new_around_h_w = self.around_home_work[new_station[0]*self.N+new_station[1]]
            target_station = self.select_target_stations(new_station, k=min(3, len(self.station)))
            for exist_station in target_station:    
                if self.is_connected(new_station, exist_station):
                    continue
                dist = distance(new_station, exist_station)
                tmp_cost = COST_STATION + (dist-1)*COST_RAIL
                distinct_people = self.calc_param(new_around_h_w, self.around_home_work[exist_station[0]*self.N+exist_station[1]])
                return_money = self.dist_cache[person_idx]*(rest_of_turn-dist)
                score = self.calc_score(distinct_people, tmp_cost, return_money)
                if ((dist < rail_count or 100 < self.income) and
                    tmp_cost < return_money and
                    max_score < score
                ):
                    r0, c0, r1, c1 = *new_station, *exist_station
                    max_score = score
                    
        if workplace_around_station:
            rail_count = (self.money - COST_STATION) // COST_RAIL  
            (r, c) = self.home[person_idx]
            dr, dc = random.choices(SEARCH_ZONE, k=1, weights=SEARCH_ZONE_WEIGHT)[0]
            new_station = (r, c)
            if 0 <= r+dr < self.N and 0 <= c+dc < self.N:
                new_station = (r+dr, c+dc)
            new_around_h_w = self.around_home_work[new_station[0]*self.N+new_station[1]]
            target_station = self.select_target_stations(new_station, k=min(5, len(self.station)))
            for exist_station in target_station:    
                if self.is_connected(new_station, exist_station):
                    continue
                dist = distance(new_station, exist_station)
                tmp_cost = COST_STATION + (dist-1)*COST_RAIL
                distinct_people = self.calc_param(new_around_h_w, self.around_home_work[exist_station[0]*self.N+exist_station[1]])
                return_money = self.dist_cache[person_idx]*(rest_of_turn-dist)
                score = self.calc_score(distinct_people, tmp_cost, return_money)
                if ((dist < rail_count or 100 < self.income) and
                    tmp_cost < return_money and
                    max_score < score
                ):
                    r0, c0, r1, c1 = *new_station, *exist_station
                    max_score = score

        home, workplace = self.home[person_idx], self.workplace[person_idx]
        hr, hc, wr, wc = *home, *workplace
        k = 2
        for (dhr, dhc) in random.choices(SEARCH_ZONE, k=k, weights=SEARCH_ZONE_WEIGHT):          
            nhr, nhc = hr+dhr, hc+dhc
            if not (0 <= nhr < self.N) or not (0 <= nhc < self.N):
                    continue
            for (dwr, dwc) in random.choices(SEARCH_ZONE, k=k, weights=SEARCH_ZONE_WEIGHT):
                nwr, nwc = wr+dwr, wc+dwc
                dist = distance((nhr, nhc), (nwr, nwc))
                if not (0 <= nwr < self.N) or not (0 <= nwc < self.N) or dist < 5:
                    continue
                distinct_people = self.calc_param(self.around_home_work[nhr*self.N+nhc], self.around_home_work[nwr*self.N+nwc])
                return_money = self.dist_cache[person_idx]*(rest_of_turn-dist)
                tmp_cost = 2*COST_STATION + (dist-1)*COST_RAIL
                rail_count = (self.money - 2*COST_STATION) // COST_RAIL
                score = self.calc_score(distinct_people, tmp_cost, return_money)
                if (max_score < score and dist < rail_count and tmp_cost < return_money):
                    r0, c0, r1, c1 = nhr, nhc, nwr, nwc
                    max_score = score
        return r0, c0, r1, c1, max_score
    
    def search_station(self) -> tuple[int, int, int, int, int, int]:
        self.calc_income()
        max_score = 0                           
        cnt = 0
        r0, c0, r1, c1, person_dist, person_idx = -1, -1, -1, -1, -1, -1
        while cnt < 50:
            p_dist, p_idx = random.choices(self.person_idxs, k=1, weights=self.weight)[0]
            if self.field.is_connected(self.home[p_idx], self.workplace[p_idx]):
                self.weight[p_idx] = 0
                continue
            rr0, cc0, rr1, cc1, new_score = self.single_simulater(p_dist, p_idx, max_score)
            if max_score < new_score:
                r0, c0, r1, c1, max_score = rr0, cc0, rr1, cc1, new_score
                person_dist, person_idx = p_dist, p_idx
            cnt += 1
        return r0, c0, r1, c1, person_dist, person_idx

    def find_best_rectangular_route(self, r0: int, c0: int, r1: int, c1: int) -> list[tuple[int, int, int]]:
        
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

                cell_type = self.field.rail_type(r, c)
                if cell_type == STATION:
                    rail_type = PASS
                elif cell_type == EMPTY:
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
        r0, c0, r1, c1 = path[0][1], path[0][2], path[-1][1], path[-1][2]
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
                            if path:
                                nt, nr, nc = path.popleft()
                                if (nt not in (PASS, STATION) and 
                                    COST_RAIL < self.money):
                                    pre_state.append((nr, nc, self.field.rail_type(nr, nc)))
                                    self.build_rail(nt, nr, nc)
                                else:
                                    path.appendleft((nt, nr, nc))
                                    self.build_nothing()
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
                return pre_state
            else:
                while self.money <= COST_RAIL:
                    self.build_nothing()
                    self.money += self.income
                    if self.is_quit():
                        return pre_state
                pre_state.append((r, c, EMPTY))
                self.build_rail(type, r, c)
            self.money += self.income

            if self.field.is_connected((r0, c0), (r1, c1)):
                return pre_state

            if self.is_quit():
                return pre_state
        return pre_state

    def search_candidate_place(self):
        weight = []
        for r in range(self.N):
            for c in range(self.N):
                tmp = {"home": set(), "workplace": set()}
                for dr, dc in SEARCH_ZONE:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < self.N) or not (0 <= nc < self.N):
                        continue
                    if -1 < self.pos2home[nr*self.N+nc]:
                        tmp["home"].add(self.pos2home[nr*self.N+nc])
                    if -1 < self.pos2workplace[nr*self.N+nc]:
                        tmp["workplace"].add(self.pos2workplace[nr*self.N+nc])
                    
                if tmp["home"] or tmp["workplace"]:
                    weight.append(len(tmp["home"] | tmp["workplace"]))
                    self.candidate_place.append([r, c, tmp])
        return weight

    def init_search(self) -> tuple[int, int, int, int]:
        r0, c0, r1, c1 = -1, -1, -1, -1
        max_score = 0.0
        weight = self.search_candidate_place()
        cnt = 0
        while r0 < 0 or cnt < 10000:
            if time.time()-S_TIME > 1.0:
                return r0, c0, r1, c1
            (fromr, fromc, frominfo), (tor, toc, toinfo) = random.choices(self.candidate_place, k=2, weights=weight)
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

            return_money = sum(self.dist_cache[idx]
                                for idx in disconnected_people)
            score = return_money*(self.T-(dist))/cost
            if (cost < return_money*(self.T-dist) and max_score < score):
                r0, c0, r1, c1 = fromr, fromc, tor, toc
                max_score = score

            cnt += 1
        return r0, c0, r1, c1

    def solve(self) -> Result:
        # main loop
        # 最初の探索のみランダム
        r0, c0, r1, c1 = self.init_search()
        if r0 < 0:
            pass
        else:
            path = self.find_best_rectangular_route(r0, c0, r1, c1)
            self.build_route(path)
            while len(self.actions) < self.T:   
                if time.time()-S_TIME > 2.75:
                    break 
                self.calc_income()
                # 経路探索
                r0, c0, r1, c1, _, person_idx = self.search_station()  
                if r0 < 0:
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
                path = self.find_best_rectangular_route(r0, c0, r1, c1)
                self.build_route(path)
                if self.field.is_connected((r0, c0), (r1, c1)):
                    self.weight[person_idx] = 0
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
