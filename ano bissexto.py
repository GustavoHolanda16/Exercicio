ano=int(input('Digite o ano que quer saber se é bissexto: '))

#ja que para o ano ser bissexto ele deve ser uma divisão exata por 4 e uma divisão com resto por 100.

if ano%4 == 0 and ano//100 != 0:
    print ('É bissexto!')
else:
    print ('Não é bissexto!')