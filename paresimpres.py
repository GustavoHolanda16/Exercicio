#pares
x=[]
y=[]
z=[]
for i in range(6):
    x.append(int(input('Digite aqui um valor: ')))
    if x[i] % 2==0:
        y.append(x[i]) 
    else:
        z.append(x[i])
print ('Esses são os valores informados:',x)
print ('Esses são os valores pares: ',y)
print ('Esses são os valores impares: ',z)