n = int(input())
elements = list(map(int, input().split()))
count = 0
for i in range(1, n):
    if elements[i] > elements[i - 1]:
        count += 1
print(count)