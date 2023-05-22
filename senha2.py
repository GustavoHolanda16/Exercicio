nome=input('Nome do usuario: ')
senha=input('Digite a senha: ')

while senha==nome:
    print("Não é permitido a senha igual ao nome do usuario!")
    senha=input('Digite novamente a senha: ')