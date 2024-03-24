n = int(input())
elements = list(map(int, input().split()))
for element in elements:
    if element % 2 == 0:
        print(element, end=' ')