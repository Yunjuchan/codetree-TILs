A = []
length = 0
for _ in range(int(input())) :
    c, *x = input().split()
    if c == 'push_back' :
        A += x
        length += 1
    elif c == 'get' :
        print(A[int(x[0])-1])
    elif c == 'size' :
        print(length)
    else :
        A.pop()
        length -= 1