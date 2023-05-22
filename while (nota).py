x=int(input('Digite um numeoro aqui: '))
while x<0 or x>10:
    print('esta errado!')
    x=int(input("digite novamente: "))
print('Numero é: ',x)