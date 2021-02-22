fname = 'example.txt'
fh = open(fname, encoding="utf-8")
arquivo = open('produtos.txt','w')
for i in fh:
    if not i.startswith('|0200|'):
        continue

    form = i.rstrip()
    form = form[6:]
    loc = form.find('|')
    form = form[loc+1:]
    loc = form.find('|')
    form = form[:loc-1]
    print(form)
    arquivo.write('|'+ form + '|' + '\n')
arquivo.close()
