<<<<<<< HEAD
horas=int(input('Horas trabalhadas: '))
valor=float(input('Valor da Hora em R$: '))
salarioB=(horas*20)*valor
ir=salarioB*0.11
inss=salarioB*0.08
sindi=salarioB*0.05
salarioL=salarioB-ir-inss-sindi
print('Salario Bruto = R$%0.2f'%salarioB)
print('Imposto de Renda = R$%0.2f'%ir)
print('INSS = R$%0.2f'%inss)
print('Sindicato = R$%0.2f'%sindi)
=======
horas=int(input('Horas trabalhadas: '))
valor=float(input('Valor da Hora em R$: '))
salarioB=(horas*20)*valor
ir=salarioB*0.11
inss=salarioB*0.08
sindi=salarioB*0.05
salarioL=salarioB-ir-inss-sindi
print('Salario Bruto = R$%0.2f'%salarioB)
print('Imposto de Renda = R$%0.2f'%ir)
print('INSS = R$%0.2f'%inss)
print('Sindicato = R$%0.2f'%sindi)
>>>>>>> 3acbc76 (novos testes)
print('Salario Liquido = R$%0.2f'%salarioL)