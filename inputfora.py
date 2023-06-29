def processar_string(string):
    resultado = ""
    for i, caractere in enumerate(string):
        if caractere.isdigit():
            resultado += '%'
        elif i % 2 == 0:
            resultado += caractere.lower()
        else:
            resultado += caractere.upper()
    return resultado


entrada = input("Digite uma palavra ou frase: ")
resultado = processar_string(entrada)
print("Resultado: ", resultado)
