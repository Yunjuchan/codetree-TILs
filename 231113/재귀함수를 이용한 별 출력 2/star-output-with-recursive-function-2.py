N = int(input())
def star(i) :
    if i == 2*N :
        return
    print('* '*int(abs(N-0.5-i)+1))
    star(i+1)
star(0)