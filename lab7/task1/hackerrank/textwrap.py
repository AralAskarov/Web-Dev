# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
list = []
flag=False

for i in range(0,n):
    a=int(input())
    
    list.append(a)
    
for i in list:
    
    a=str(i)
    b=''.join(reversed(str(i)))
    if(a==b):
        flag=True
for i in list:
    if(i<0):
        flag=False
if(flag==True):
    print("True")
else:
    print("False")