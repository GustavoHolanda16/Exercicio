arquivo = open ('sabado.txt','w')
for i in range (1,101):
    i=str(i)
    arquivo.write(i+'\n')
    
arquivo.close
print('ok!')