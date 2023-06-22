import random

#Cria matriz aleatória
def retornaMatriz(l=2, c=2):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            if j == c-1:
                linha.append(str(random.randint(1, 10))+"\n")
            else:
                linha.append(str(random.randint(1, 10))+"\t")
        m.append(linha)

    x = ""
    for i in m:
        x += "".join(i)
    return x
#Cria Matriz Inputada
def retornaMatriz2(l=2, c=2):
    n = []
    for i in range(l):
        linha = []
        for j in range(c):
            if j == c-1:
                linha.append(input()+"\n")
            else:
                linha.append(input()+"\t")
        n.append(linha)

    y = ""
    for i in n:
        y += "".join(i)
    return y

arquivo = open("bingo_cpu.txt", "w")
arquivo.write( retornaMatriz(3,3) )
arquivo.close()
arquivo = open("bingo_User.txt", "w")
arquivo.write( retornaMatriz2(3,3) )
arquivo.close()
