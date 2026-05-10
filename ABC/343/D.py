def main():
    N, T = map(int, input().split(' '))
    scores = [0] * N
    player = {0:N}
    res = []

    for _ in range(T):
        a, b = map(int, input().split(' '))
        #print(player)
        player[scores[a-1]] -= 1
        #print(player)
        if player[scores[a-1]] == 0:
            del player[scores[a-1]]
        scores[a-1] += b
        if  scores[a-1] not in player:
            player[scores[a-1]] = 1    
        else:
            player[scores[a-1]] += 1
        #print(player)
        res.append(len(player))

    for i in res:
        print(i)    
        
if __name__ == '__main__':
    main()