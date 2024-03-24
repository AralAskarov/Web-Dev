# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1 = set()  
for i in range(0,n):
    a=input()
    set1.add(a)
m=int(input())
set2 = set()  
for i in range(0,m):
    a=input()
    set2.add(a)
union_set = set1.union(set2) 
print(len(union_set))  