import sys
import time

from random import randint
from heapq import heappush, heappop


def read_input():

    N = int(sys.stdin.readline().rstrip())
    SB = []
    IW = []

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        SB.append((a, b))

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        IW.append((a, b))

    return SB, IW


def check(FISH, lft, rgt, btm, top):
    fish = 0
    for x, y in FISH:
        if lft <= x <= rgt and btm <= y <= top:
            fish += 1

    return fish


def calc_score(SB, IW, rect):
    saba = check(SB, *rect)
    iwashi = check(IW, *rect)

    return max(0, saba - iwashi + 1)


def net_random(SB, IW):
    lft = randint(0, 10**5)
    rgt = randint(0, 10**5)
    btm = randint(0, 10**5)
    top = randint(0, 10**5)

    if lft > rgt:
        lft, rgt = rgt, lft

    if btm > top:
        btm, top = top, btm

    score = calc_score(SB, IW, (lft, rgt, btm, top))

    return score, (lft, rgt, btm, top)


def update_best(best_score, best_pos, score, pos):
    if best_score >= score:
        return best_score, best_pos

    return score, pos


def is_overlapped(rect1, rect2):
    lft1, rgt1, btm1, top1 = rect1
    lft2, rgt2, btm2, top2 = rect2
    if min(rgt1, rgt2) <= max(lft1, lft2) and min(top1, top2) <= max(btm1, btm2):
        return True

    else:
        return False


# def merge_rect(rect1, rect2):
#     if is_overlapped(rect1, rect2):
#         poly1 = parse_to_rect(rect1)
#         poly2 = parse_to_rect(rect2)

#         poly1

def parse_to_rect(pos):

    return (pos[0], pos[2]), (pos[1], pos[2]), (pos[1], pos[3]), (pos[0], pos[3])


def main():

    st_main = time.time()

    SB, IW = read_input()

    R = []

    best_score = 0
    best_pos = (0, 100000, 0, 100000)

    heappush(R, (best_score, best_pos))

    cnt = 0
    while time.time() - st_main < 1.0:
        score, pos = net_random(SB, IW)
        if len(R) < 5:
            heappush(R, (score, pos))

        else:
            if R[0][0] < score:
                heappop(R)
                heappush(R, (score, pos))

        best_score, best_pos = update_best(best_score, best_pos, score, pos)
        cnt += 1

    print(time.time() - st_main, cnt, file=sys.stderr)

    for score, pos in R:
        st = time.time()

        # 座標中心だけ使って、微調整
        cx = (pos[0] + pos[1]) // 2
        cy = (pos[2] + pos[3]) // 2

        cnt = 0
        while time.time() - st < 0.15:
            w = randint(0, min(cx - pos[0], pos[1] - cx))
            h = randint(0, min(cy - pos[2], pos[3] - cy))

            pos = (cx - w, cx + w, cy - h, cy + h)

            score = calc_score(SB, IW, pos)

            best_score, best_pos = update_best(best_score, best_pos, score, pos)
            cnt += 1

        print(time.time() - st_main, cnt, file=sys.stderr)

    rect = parse_to_rect(best_pos)

    print(4)
    for x, y in rect:
        print(x, y)


if __name__ == "__main__":
    main()
