N, tp = map(int, input().split())
visited = [False] * 7

def f1(level, N, path) :
    if level == N : 
        print(*path)
        return

    for i in range(1,7) :
        f1(level+1, N, path+[i])


def f2(level, N, start, path) :
    if level == N :
        print(*path)
        return

    for i in range(start, 7) :
        f2(level+1, N, i, path + [i])


def f3(level, N, path) :
    if level == N :
        print(*path)
        return

    for i in range(1, 7) :
        if visited[i] : continue
        visited[i] = True 
        f3(level+1, N, path+[i])


if tp == 1 :
    f1(0, N, [])
elif tp == 2 :
    f2(0, N, 1, [])
elif tp == 3 :
    f3(0, N, [])