#media de aproveitamento.
x = float(input('Digite a 1º Nota! '))
y = float(input('Digite a 2º Nota! '))
media = (x+y)/2

print ('1ª Nota:',x)
print ('2º Nota:',y)
print(media)

if media <=10 and media>9:
    print('A')
    print('Aprovado!')
elif media <=9 and media>7.5:
    print('B')
    print('Aprovado!')
elif media <= 7.5 and media > 6:
    print('C')
    print('Aprovado!')
elif media<=6.0 and media>4:
    print('D')
    print('Reprovado!')
else:
    print('E')
    print('Reprovado!')