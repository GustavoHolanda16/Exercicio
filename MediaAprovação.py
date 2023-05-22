#Media de Notas!
print('Digite Duas Notas:')
x=float(input('Nota 1: '))
y=float(input('Nota 2: '))
media=(x+y)/2
print(media)
if media==10:
    print ('Aprovado com Distinção!')
elif media>=7:
    print ('Aprovado!')
else:
    print('Reprovado!')