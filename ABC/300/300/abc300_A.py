import sys 

answers = list(map(int, input().split(' ')))
options = list(map(int, input().split(' ')))

answer = answers[1] + answers[2]

for i, v in enumerate(options):
    if v - answer == 0:
        print(i + 1)