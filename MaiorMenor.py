#Maior e Menor entre 3!
print('Digite três numeros:')
x=float(input('Numero 1: '))
y=float(input('Numero 2: '))
z=float(input('Numero 3: '))

if x>y:
    print (x,'Maior que',y,z)
elif y>z:
    print (y,'Maior que',z,x)
elif x>z:
    print (x,'Maior que',y,z)
else:
    print(z,'Maior que',x,y)
if x<y:
    print (x,'Menor que',y,z)
elif y<z:
    print (y,'Menor que',z,x)
elif x<z:
    print (x,'Menor que',y,z)
else:
    print(z,'Menor que',x,y)