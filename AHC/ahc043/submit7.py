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
import re
import sys
import time
from typing import Generic, Iterable, Iterator, \
    List, Tuple, Dict, TypeVar, Optional, Any, Callable

# setting
Pos = tuple[int, int]
T = TypeVar('T')
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
SEARCH_ZONE = [(0, -2), (-1, -1), (0, -1), (1, -1), (2, 0), (1, 0), (0, 0), 
               (-1, 0), (-2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)]
INF = 1 << 60
SEARCH_CNT = 0
SEARCH_TIME = []
BUILD_CNT = 0
BUILD_TIME = []
BUILD_NOTHING_CNT = 0


def calc_time_search(f):
    def in_func(*args, **kwargs):
        global SEARCH_CNT
        s_time = time.time()
        SEARCH_CNT += 1
        res = f(*args, **kwargs)
        SEARCH_TIME.append(time.time()-s_time)
        return res
    return in_func

def calc_time_build(f):
    def in_func(*args, **kwargs):
        global BUILD_CNT
        s_time = time.time()
        BUILD_CNT += 1
        res = f(*args, **kwargs)
        BUILD_TIME.append(time.time()-s_time)
        return res
    return in_func    

def count_build_nothing(f):
    def in_func(*args, **kwargs):
        global BUILD_NOTHING_CNT
        BUILD_NOTHING_CNT += 1
        res = f(*args, **kwargs)
        return res
    return in_func

class SortedSet(Generic[T]):
    #
    # https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
    #
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[T] = []) -> None:
        # Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self.size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return 'SortedSet' + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return '{' + s[1 : len(s) - 1] + '}'

    def _position(self, x: T) -> Tuple[List[T], int, int]:
        # return the bucket, index of the bucket and position in which x should be. self must not be empty.
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        # Add an element and return True if added. / O(√N)
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a: List[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        # Remove an element and return True if removed. / O(√N)
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def lt(self, x: T) -> Optional[T]:
        # Find the largest element < x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]
    def le(self, x: T) -> Optional[T]:
        # Find the largest element <= x, or None if it doesn't exist.
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        # Find the smallest element > x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        # Find the smallest element >= x, or None if it doesn't exist.
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        # Return the i-th element.
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        # Pop and return the i-th element.
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        # Count the number of elements < x.
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        # Count the number of elements <= x.
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

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
    
    def rail_type(self, r: int, c: int) -> int:
        return self.rail[r*self.N+c]

    def collect_stations(self, pos: Pos) -> list[Pos]:
        return list(self.has_station[pos[0]*self.N+pos[1]])


class Solver:
    def __init__(self, N: int, M: int, K: int, T: int, home: list[Pos], workplace: list[Pos]):
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
        self.person_idxs = SortedSet()
        self.station = []
        self.candidate_place = []
        self.around_home_workplace = [set() for _ in range(N*N)]
        self.pos2home = {}
        self.pos2workplace = {}
        self.connected = [0]*M
        self.weight = [1.001**(self.M-i) for i in range(1, self.M+1)]
        
        for person_idx in range(self.M):
            home_pos, workplace_pos = self.home[person_idx], self.workplace[person_idx]
            person_dist = distance(home_pos, workplace_pos)
            self.person_idxs.add((-person_dist, person_idx))
            self.pos2home[home_pos] = person_idx
            self.pos2workplace[workplace_pos] = person_idx 
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    hr, hc = home_pos[0]+dr, home_pos[1]+dc 
                    wr, wc = workplace_pos[0]+dr, workplace_pos[1]+dc
                    if 0 <= hr < self.N and 0 <= hc < self.N:
                        self.around_home_workplace[hr*self.N+hc].add(person_idx)
                    if 0 <= wr < self.N and 0 <= wc < self.N:
                        self.around_home_workplace[wr*self.N+wc].add(person_idx)

    def calc_income(self) -> int:
        income = 0
        for i in range(self.M):
            if self.field.is_connected(self.home[i], self.workplace[i]):
                income += distance(self.home[i], self.workplace[i])
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

    @count_build_nothing
    def build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
    
    def is_quit(self) -> None:
        return not (len(self.actions) < self.T)

    @calc_time_search
    def search_station(self) -> tuple[int, int, int, int, int, int]:
        self.calc_income()
        max_score = 0

        is_connected_cache = defaultdict(bool)
        def is_connected(s: Pos, t: Pos):
            k = (s, t) if s <= t else (t, s)
            if k in is_connected_cache:
                return is_connected_cache[k]
            res = self.field.is_connected(s, t)
            is_connected_cache[k] = res
            return res

        def in_func(person_dist, person_idx, max_score):
            r0, c0, r1, c1 = -1, -1, -1, -1
            dist = person_dist*-1
            if self.connected[person_idx] or is_connected(self.home[person_idx], self.workplace[person_idx]):
                self.connected[person_idx] = 1
                return -1, -1, -1, -1, max_score

            rest_of_turn = self.T - (len(self.actions)+1+dist)
            
            home_around_station = self.field.collect_stations(self.home[person_idx])
            workplace_around_station = self.field.collect_stations(self.workplace[person_idx])

            if home_around_station and workplace_around_station:
                rail_count = self.money // COST_RAIL   
                for home in home_around_station:
                    for workplace in workplace_around_station:    
                        dist = distance(home, workplace)
                        tmp_cost = (dist-1)*COST_RAIL
                        return_money = dist*rest_of_turn
                        if ((dist < rail_count or 100 < self.income) and
                            tmp_cost < return_money and 
                            not is_connected(home, workplace) and
                            max_score < return_money/tmp_cost
                        ):
                            r0, c0, r1, c1 = *home, *workplace
                            max_score = return_money/tmp_cost

            elif home_around_station or workplace_around_station:
                rail_count = (self.money - COST_STATION) // COST_RAIL  
                new_station = self.home[person_idx] if not home_around_station else self.workplace[person_idx] 
                return_money = distance(self.home[person_idx], self.workplace[person_idx])*rest_of_turn
                
                new_around_h_w = self.around_home_workplace[new_station[0]*self.N+new_station[1]]
                for exist_station in self.station:    
                    if is_connected(new_station, exist_station):
                        continue
                    dist = distance(new_station, exist_station)
                    tmp_cost = COST_STATION + (dist-1)*COST_RAIL
                    distinct_people = 1.5*len(new_around_h_w & self.around_home_workplace[exist_station[0]*self.N+exist_station[1]])
                    if ((dist < rail_count or 100 < self.income) and
                        tmp_cost < return_money and
                        max_score < (return_money+distinct_people)/tmp_cost
                    ):
                        r0, c0, r1, c1 = *new_station, *exist_station
                        max_score = (return_money+distinct_people)/tmp_cost
            else:
                tmp_cost = 2*COST_STATION + (dist-1)*COST_RAIL
                rail_count = (self.money - 2*COST_STATION) // COST_RAIL
                if (dist < rail_count and tmp_cost < dist*rest_of_turn):
                    r0, c0, r1, c1 = *self.home[person_idx], *self.workplace[person_idx]
            return r0, c0, r1, c1, max_score

        cnt = 0
        r0, c0, r1, c1, person_dist, person_idx = -1, -1, -1, -1, -1, -1
        for p_dist, p_idx in self.person_idxs:
            if 20 < cnt:
                break
            rr0, cc0, rr1, cc1, new_score = in_func(p_dist, p_idx, max_score)
            if max_score < new_score:
                r0, c0, r1, c1, max_score = rr0, cc0, rr1, cc1, new_score
                person_dist, person_idx = p_dist, p_idx
            cnt += 1
        while cnt < 30:
            p_dist, p_idx = random.choices(self.person_idxs, k=1, weights=self.weight[:len(self.person_idxs)])[0]
            rr0, cc0, rr1, cc1, new_score = in_func(p_dist, p_idx, max_score)
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

    @calc_time_build
    def build_route(self, path: list[list[int, Pos]]) -> None:
        r0, c0, r1, c1 = path[0][1], path[0][2], path[-1][1], path[-1][2]
        self.calc_income()
        path: deque = deque(path)
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
                    self.money += self.income
                    if self.is_quit():
                        print(Result(self.actions, self.money))
                        sys.exit(0)
                self.build_station(r, c)
                self.calc_income()
                if flg != EMPTY:
                    self.money += self.income
                    return
            elif type == PASS:
                pass
            else:
                while self.money <= COST_RAIL:
                    self.build_nothing()
                    self.money += self.income
                    if self.is_quit():
                        print(Result(self.actions, self.money))
                        sys.exit(0)
                self.build_rail(type, r, c)
            self.money += self.income

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
        max_return_mony = 0
        self.search_candidate_place()
        cnt = 0
        while r0 < 0 or cnt < 10000:
            if time.time()-S_TIME > 2.6:
                return r0, c0, r1, c1
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
                max_return_mony/min_cost < return_money*(self.T-(dist))/cost):
                r0, c0, r1, c1 = fromr, fromc, tor, toc
                min_cost = cost       
                max_return_mony = return_money*(self.T-(dist-1)) 
            cnt += 1
        return r0, c0, r1, c1

    def solve(self) -> Result:
        global SEARCH_CNT
        global SEARCH_TIME
        global BUILD_CNT
        global BUILD_TIME

        # main loop
        # 最初の探索のみランダム
        r0, c0, r1, c1 = self.init_search()
        if r0 < 0:
            pass
        else:
            path = self.find_best_rectangular_route(r0, c0, r1, c1)
            self.build_route(path)
            while len(self.actions) < self.T:   
                if time.time()-S_TIME > 2.70:
                    print(f'# in {len(self.actions)}')
                    break 
                self.calc_income()
                # 経路探索
                r0, c0, r1, c1, person_dist, person_idx = self.search_station()  
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
                    self.connected[person_idx] = 1
                    self.person_idxs.discard((person_dist, person_idx))
                self.calc_income()

        # あとは待機
        self.calc_income()
        print(f"# {len(self.actions)}") 
        while len(self.actions) < self.T:
            self.build_nothing()
            self.money += self.income

        print(Result(self.actions, self.money))
        sys.exit(0)
    
    def __del__(self):
        search_time = sum(SEARCH_TIME)
        search_time_mean = search_time/SEARCH_CNT
        search_time_var = sum([(s-search_time_mean)**2 for s in SEARCH_TIME])/SEARCH_CNT
        build_time = sum(BUILD_TIME)
        build_time_mean = build_time/BUILD_CNT
        build_time_var = sum([(s-build_time_mean)**2 for s in BUILD_TIME])/BUILD_CNT

        print(f"# NOTHING_CNT: {BUILD_NOTHING_CNT}", flush=True)
        print(f"# NAME     CNT  SUM     AVE     MAX     STD", flush=True)
        if 1 < SEARCH_CNT:
            print(f"# SEARCH : {SEARCH_CNT:04} {search_time:.1e} {search_time_mean:.1e} {max(SEARCH_TIME):.1e} {search_time_var:.1e}", flush=True)
        print(f"# BUILD  : {BUILD_CNT:04} {build_time:.1e} {build_time_mean:.1e} {max(BUILD_TIME):.1e} {build_time_var:.1e}", flush=True)
        print(f"# TOTAL_TIME: {time.time()-S_TIME:02.4}")

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
