a=int(input('Digite a população do pais A: ' ))
b=int(input('Digite a população do pais B: ' ))
ano=0
while a<=b:
    b=b+(b*(0.015))
    a=a+(a*(0.03))
    ano+=1
print(ano,'Anos')
print('pais A: %0.0f'%a)
print('Pais B: %0.0f'%b)
