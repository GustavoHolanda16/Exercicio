import random

tentativa = 7
palavras = 'TESTE','PROGRAMA','SHOW','OVO','VIVAOLINUX','PYTHON','LUCAS','LINUX','LIMOSINE','FERRARI','CAMARO','BRANCO','PESQUISAR'
sorteado = random.choice(palavras)
while tentativa != 0:
    embaralha = random.sample(sorteado, len(sorteado))
    juntar_palavra_embaralhada = ''.join(embaralha)
    print(juntar_palavra_embaralhada)
    print("="*20)
    tent = input("Digite a palavra: ").upper()
    if tent == sorteado:
        print("\nParabens! Voce venceu!")
        break
    else:
        tentativa -= 1
        print("\nVoce errou! Tentativas restantes {tentativa}")
        print("="*20)