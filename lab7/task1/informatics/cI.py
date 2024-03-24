n=int(input())
m=int(0)
for i in range(1,n+1):
    if(n%i==0):
        m+=1
print(m)
