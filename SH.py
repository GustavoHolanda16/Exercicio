N=int(input())
h=N//3600
N=N-h*3600
m=N//60
N=N-m*60
print("%i:%i:%i"%(h,m,N))