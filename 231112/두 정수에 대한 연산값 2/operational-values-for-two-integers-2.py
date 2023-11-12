a, b = map(int, input().split())
def f(a, b) :
    if a > b : a, b = b, a
    a += 10
    b *= 2
    return a, b
print(*f(a, b))