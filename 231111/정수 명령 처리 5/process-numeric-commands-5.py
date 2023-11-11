A = []
N = int(input())
for _ in range(N) :
    c, *x = input().split()
    if c == 'push_back' :
        A += x
    elif c == 'get' :
        print(A[int(x[0])-1])
    elif c == 'size' :
        print(len(A))
    else :
        A.pop()