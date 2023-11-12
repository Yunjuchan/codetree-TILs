a, b = map(int, input().split())
if a > b : a, b = b, a
a += 10
b *= 2
print(a, b)