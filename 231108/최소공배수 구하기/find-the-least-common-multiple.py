n, m = map(int, input().split())
total = n*m
while m :
    tmp = m
    m = n % m
    n = tmp
print(total // n)