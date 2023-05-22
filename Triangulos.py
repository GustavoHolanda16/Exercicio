x=int(input('Digite um lado do Triangulo: '))
y=int(input('Digite um lado do Triangulo: '))
z=int(input('Digite um lado do Triangulo: '))
if (y-z)<x and x<(y+z) and (x-z)<y and y<(x+z) and (x-y)<z and z<(x+y) :
    print('é triângulo')

    if x==y and y==z and x==z:
        print(x,y,z,'esse triangulo é equilatero!')
    elif x==y and x!=z:
        print(x,y,z,'esse triangulo é isoceles!')
    elif y==z and y!=x:
        print(x,y,z,'esse triangulo é isoceles!')
    elif x==z and x!=y:
        print(x,y,z,'esse triangulo é isoceles!')
    elif x!=y and y!=z and x!=z:
        print(x,y,z,'esse triangulo é escaleno!')
else:
    print (x,('-'),y,('-'),z,'Esses valores não representam um triangulo!')
