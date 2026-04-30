import heapq
import random
import time
from math import sqrt

RANGE = 10**6

def rand():
    return random.randint(0, 100000)

def make_hash(i, j):
    return i * (1 << 20) + j

h = []
for _ in range(RANGE):
    i, j = rand(), rand()
    heapq.heappush(h, make_hash(i, j))

def main():
    for _ in range(RANGE):
        heapq.heappop(h)
        i, j = rand(), rand()
        heapq.heappush(h, make_hash(i, j))

if __name__ == '__main__':
    res = []
    for _ in range(10):
        start = time.time()
        main()
        res.append(time.time() - start)
    ave = sum(res)/len(res)
    var = sqrt(sum([(ele-ave)**2 for ele in res]))
    print(ave, var)