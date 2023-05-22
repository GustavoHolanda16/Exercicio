#maior pelo menor
x=int(input('Digite o 1º : '))
y=int(input('Digite o 2º : '))


if x==y:
    print('São Iguais!')
elif x>y:
    print('o 1º numero é o maior: ',x-y)
else:
    print('o 2º numero é o maior: ',y-x)