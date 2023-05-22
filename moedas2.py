valor = float(input()) # lê o valor monetário em ponto flutuante

notas = [100, 50, 20, 10, 5, 2] # lista de valores das notas disponíveis
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01] # lista de valores das moedas disponíveis

print("NOTAS:")
for nota in notas:
    qtd_notas = int(valor / nota) # calcula a quantidade de notas necessárias
    print(qtd_notas, "nota(s) de R$", format(nota, ".2f"))
    valor -= qtd_notas * nota # subtrai o valor das notas já contabilizadas

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = int(round(valor, 2) / moeda) # calcula a quantidade de moedas necessárias
    print(qtd_moedas, "moeda(s) de R$", format(moeda, ".2f"))
    valor = round(valor - qtd_moedas * moeda, 2) # subtrai o valor das moedas já contabilizadas

