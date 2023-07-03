def somapares(numeros):
    soma=0
    for i in range(numeros):
        num=int(input('Digite um numero: '))
        if num % 2 == 0:
            soma+=num
    return(soma)    

y=int(input('Quantos numeros voce quer: '))
print(somapares(y))
