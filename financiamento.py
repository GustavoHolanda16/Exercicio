salario=float(input('Digite aqui seu salario: '))
financiamento=float(input('Digite aqui o valor pretendido: '))

if financiamento <= (salario*5):
    print ('Financiamento aprovado!')
else:
    print ('Financiamento Reprovado!')

print ('Obrigado por nos consultar!')