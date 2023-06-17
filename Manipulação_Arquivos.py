arquivo = open ('sabado.txt','w')
for i in range (5):
    arquivo.write(input('Digite nome: ')+'\n')
    
arquivo.close
print('ok!')