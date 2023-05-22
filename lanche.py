id,quantidade = map(int, input().split())
valor=0
if id==1:
    valor=4.0
elif id==2:
    valor=4.5
elif id==3:
    valor=5.0
elif id==4:
    valor=2.0
elif id==5:
    valor=1.5
print("Total: R$ %0.2f"%(valor*quantidade))