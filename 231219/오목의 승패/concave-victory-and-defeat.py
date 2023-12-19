def check(y, x, tp) :

    for i in range(3) :
        level = 1
        dy, dx = y, x
        while True :
            dy += direct_y[i]
            dx += direct_x[i]
            if dy > 18 or dx > 18 : break
            if arr[dy][dx] == tp :
                level += 1
            else : break
        if level == 5 :
            return True
    return False

result = False
direct_y = [1,0,1]
direct_x = [0,1,1]
arr = [list(map(int, input().split())) for _ in range(19)]

for i in range(19) :
    for j in range(19) :
        if arr[i][j] :
            ret = check(i, j, arr[i][j])
            if ret : result = [arr[i][j], i+1, j+1]
        if result : break
    if result : break

if result :
    print(result[0])
    print(*result[1:])
else :
    print(0)

# print(check(1, 2, 1))

# N, tp = map(int, input().split())
# visited = [False] * 7

# def f1(level, N, path) :
#     if level == N : 
#         print(*path)
#         return

#     for i in range(1,7) :
#         f1(level+1, N, path+[i])


# def f2(level, N, start, path) :
#     if level == N :
#         print(*path)
#         return

#     for i in range(start, 7) :
#         f2(level+1, N, i, path+[i])


# def f3(level, N, path) :
#     if level == N :
#         print(*path)
#         return

#     for i in range(1, 7) :
#         if visited[i] : continue
#         visited[i] = True 
#         f3(level+1, N, path+[i])
#         visited[i] = False


# if tp == 1 :
#     f1(0, N, [])
# elif tp == 2 :
#     f2(0, N, 1, [])
# elif tp == 3 :
#     f3(0, N, [])