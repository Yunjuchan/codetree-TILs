N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N) :
    B.append(A[i])
    if not i % 2 :
        B.sort()
        print(B[i//2], end=' ')