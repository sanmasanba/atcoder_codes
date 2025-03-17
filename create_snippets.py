snippets = []
with open('./input.txt', 'r', encoding='utf8') as f:
    txt = f.readlines()
    for t in txt:
        t = t.replace('\\', '\\\\')
        t = t.replace('"', '\\"')
        t = t.replace('    ', '\\t').rstrip()
        cnt = t.count('\\t')
        t = '"' + t + '",' + '\n'
        t = "    " * cnt + t
        snippets.append(t)

with open('./output.txt', 'w', encoding='utf8') as f:
    f.writelines(snippets)