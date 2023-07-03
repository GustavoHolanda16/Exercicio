def vogais(string):
    nova=''
    for i in (string):
        if i=='a' or i== 'e' or i=='o' or i=='u':
            nova+=i.upper()
        else:
            nova+=i
    return nova
x=input()
print(vogais(x))

 
