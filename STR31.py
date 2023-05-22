x=input()
num=0
for i in range(len(x)):
    if x[i].isnumeric():
        num+=1
print(num)