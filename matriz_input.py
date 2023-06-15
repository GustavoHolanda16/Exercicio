m = [] #matriz vazia
#Leitura da Matriz:
#linhas
for i in range(int(input("Linhas?"))):
    linha = []
    #colunas
    for j in range(int(input("Colunas?"))):
        linha.append(input("M%i%i: " % (i, j)))
    m.append(linha) #adicionando a linha

#Impressão da matriz:
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end="\t")
    print()