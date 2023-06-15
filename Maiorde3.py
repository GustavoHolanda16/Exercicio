<<<<<<< HEAD
#Maior entre 3!
print('Digite três numeros:')
x=float(input('Numero 1: '))
y=float(input('Numero 2: '))
z=float(input('Numero 3: '))

if x>y and x>z:
    print (x,'Maior que',y,z)
elif y>z and y>x:
    print (y,'Maior que',z,x)
else:
=======
#Maior entre 3!
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
>>>>>>> 3acbc76 (novos testes)
    print(z,'Maior que',x,y)