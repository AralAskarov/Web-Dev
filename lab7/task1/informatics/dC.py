n = int(input())
elements = list(map(int, input().split()))
positive_count = sum(1 for element in elements if element > 0)
print(positive_count)