x=int(input('Digite um valor: '))
y=int(input('Digite outro valor'))
z=input('Digite A ou S: ')

if z=='a' or z=='A':
    print ('Soma de X + Y: ',(x+y))
elif z=='s' or z=='S':
    print ('Subtração de', x ,'-', y,': ',(x-y))
else:
    print('Digite A ou S!')
