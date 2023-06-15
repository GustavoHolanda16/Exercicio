#Maior e Menor entre 3!
print('Digite três numeros:')
ArrozCarvalho=float(input('Valor Arroz Carvalho: '))
ArrozVitoria=float(input('Valor Arroz Vitoria: '))
ArrozChines=float(input('Valor Arroz Chinês: '))

if ArrozCarvalho<ArrozVitoria:
    print(ArrozCarvalho,'Logo o Arroz Carvalho é mais barato que Arroz Carvalho e o Arroz Chinês')
elif ArrozVitoria<ArrozChines:
    print (ArrozVitoria,'Logo o Arroz Vitoria é mais barato que Arroz Carvalho e o Arroz Chinês')
elif ArrozChines<ArrozVitoria:
    print(ArrozChines, 'Logo o Arroz Chinês é mais barato que Arroz Carvalho e o Arroz Vitoria')
