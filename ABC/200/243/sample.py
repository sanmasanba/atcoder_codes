import os

res = 0
for i in ['000', '100', '200', '300']:
    for j in range(100):
        dirpath = f'./{i}/{int(i)+j:3}'
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)
        for k in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            filepath = f'./{i}/{int(i)+j:3}/ABC{int(i)+j}_{k}.py'
            if not os.path.isfile(filepath):
                f = open(filepath, 'w')
                f.write('')
                f.close()
                res += 1

print(res)