import math

def main():
    T = int(input())
    L, X, Y = map(int, input().split(' '))
    Q = int(input())

    Es = []
    for _ in range(Q):
        Es.append(int(input()))
     
    for E in Es:
        theta = E/T * 2.0 * math.pi
        x = 0
        y = - L/2.0 * math.sin(theta)
        z = L/2 * (1.0 - math.cos(theta))
 
        res_l = math.sqrt((x-X)**2 + (y-Y)**2)
        res_h = z
        
        res = math.atan(res_h / res_l) / math.pi * 180 
        print(res)

if __name__ == '__main__':
    main()