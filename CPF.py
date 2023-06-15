cpf = input("CPF(xxx.xxx.xxx-xx) :") #3 7 11

for letra in cpf:
    if(cpf[3] !=".") or (cpf[7] !=".") or (cpf[11] !="-"):
        cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")
print("O 'CPF' está no formato correto")