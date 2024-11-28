# import
import numpy as np
import random as rd
import time


# 入力を受け取る
#print("入力")
n = int(input())
get = [ list(map(int,input().split(" "))) for _ in range(n)]
get = np.array(get)

start_time = time.time()

# i列を追加してr順にソート
i = np.arange(0, n)
get_i = np.insert(get, 0, i, axis=1)
get_i = get_i[get_i[:, 3].argsort()[::-1]]

def iou(a, b):
    # a, bは矩形を表すリストで、a=[xmin, ymin, xmax, ymax]
    rec_t = True
    ax_mn, ay_mn, ax_mx, ay_mx = a[0], a[1], a[2], a[3]
    bx_mn, by_mn, bx_mx, by_mx = b[0], b[1], b[2], b[3]

    a_area = (ax_mx - ax_mn + 1) * (ay_mx - ay_mn + 1)
    b_area = (bx_mx - bx_mn + 1) * (by_mx - by_mn + 1)

    abx_mn = max(ax_mn, bx_mn)
    aby_mn = max(ay_mn, by_mn)
    abx_mx = min(ax_mx, bx_mx)
    aby_mx = min(ay_mx, by_mx)
    w = max(0, abx_mx - abx_mn + 1)
    h = max(0, aby_mx - aby_mn + 1)
    intersect = w*h

    iou = intersect / (a_area + b_area - intersect)
    if iou > 0:
        rec_t = False
    return rec_t

# 長方形の作成
test = np.zeros(5, dtype=int)
out = np.empty((0, 5), dtype=int)

rate = 100
counter = 0

for j in get_i:
    a = j[1]
    b = j[2]
    c = j[1]+1
    d = j[2]+1
    test[0] = a
    test[1] = b
    test[2] = c
    test[3] = d
    test[4] = j[0]
    out = np.append(out, [test], axis=0)

while time.time() - start_time < 4.3:
    #print(end_time - start_time)
    for k in out:
        #print(k)
        random = rd.randint(0, 3)

        if counter >= 800 and rate != 1:
            rate -= 30
            if rate <= 0:
                rate = 1
            #print("change rate",rate)
            counter = 0

        if random == 0 and (k[0]-rate) >= 0:
            a = k[0] - rate
            b = k[1]
            c = k[2]
            d = k[3]
        elif random == 1 and (k[1]-rate) >= 0:
            a = k[0]
            b = k[1] - rate
            c = k[2]
            d = k[3]
        elif random == 2 and (k[2]+rate) <= 10000:
            a = k[0]
            b = k[1]
            c = k[2] + rate
            d = k[3]
        elif random == 3 and (k[3]+rate) <= 10000:
            a = k[0]
            b = k[1]
            c = k[2]
            d = k[3] + rate

        check = False

        for m in get_i:
            if m[0] == k[4]:
                if (c-a)*(d-b) > m[3]:
                    check = True
                    counter += 1
                    #print("counter",counter)
                    #print("reached r")
                    break

                # 他の企業の核を内包しない
                """
                if a <= m[1] and m[1]+1 <= c and b <= m[2] and m[2]+1 <= d:
                    check = True
                    break
                """


        for l in out:
            if l[4] != k[4]:
                o = [a, b, c, d]
                p = [l[0], l[1], l[2], l[3]]
                
                if iou(o,p) == False:
                    check = True
                    break
            
        #print(check)

        if check == False:
            k[0] = a
            k[1] = b
            k[2] = c
            k[3] = d
            #print("k is",k)

out = out[out[:, 4].argsort()[::1]]

out = np.delete(out, 4, 1)

for s in out:
    print(s[0],s[1],s[2],s[3])