import random
bc=[]
bu=[]
pontos=0
#Cria matriz aleatória
def retornaMatriz(l=2, c=2):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            if j == c-1:
                linha.append(str(random.randint(1, 10))+"\n")
                bc.append(linha[j])
            else:
                linha.append(str(random.randint(1, 10))+"\t")
                bc.append(linha[j])
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
                linha.append(input('Digite o seus numeros: ')+"\n")
                bu.append(linha[j])
            else:
                linha.append(input('Digite o seus numeros: ')+"\t")
                bu.append(linha[j])
        n.append(linha)

    y = ""
    for i in n:
        y += "".join(i)
    return y


arquivo = open("bingo_cpu.txt", "w")
arquivo.write( retornaMatriz(3,3) )
arquivo.close()
print('Bingo CPU pronto!')
arquivo = open("bingo_User.txt", "w")
arquivo.write( retornaMatriz2(3,3) )
arquivo.close()
print('Bingo User pronto!')
print(bc)
print(bu)

for i in range (len(bc)):
    if bc[i]==bu[i]:
        pontos+=1
print('Você acertou %s ponto(s)!'%pontos)
