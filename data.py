dd=int(input('Digite o dia: '))
mm=int(input('Digite o mês: '))
aa=int(input('Digite o ano: '))

if 1 <= dd <=31 and 1 <= mm <= 12 and 1 <= aa <= 9999:
    if mm == 2 and 1 <= dd <= 28:
        print(dd, '/', mm, '/', aa)
        print('É uma data valida!')
    elif mm!=2 and 1 <= dd <= 31:
        print(dd, '/', mm, '/', aa)
        print('É uma data valida!')
    else:
        print('Data invalida!')
