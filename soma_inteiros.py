a,n = input().split()
a = int(a)
n = int(n)


while n<=0:
    n = int(input())
    
soma = 0

for i in range(n):
   soma+=(a+i)

print(soma)