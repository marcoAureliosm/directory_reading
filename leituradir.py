from os import getcwd, listdir
print(getcwd())
doc=[]
for c in listdir():
    doc.append(c)
    print(c)
with open('Arquivos_pasta.txt', 'w') as arquivo:
    arquivo.write(str(doc))
