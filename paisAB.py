a=80000
b=200000
ano=0
while a<=b:
    b=b+(b*(0.015))
    a=a+(a*(0.03))
    ano+=1
    print('pais A: %0.0f'%a)
    print('Pais B: %0.0f'%b)

print(ano,'Anos')
print('pais A: %0.0f'%a)
print('Pais B: %0.0f'%b)
