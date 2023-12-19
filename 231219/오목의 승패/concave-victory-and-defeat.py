def check(y, x, tp) :

    for i in range(3) :
        level = 1
        dy, dx = y, x
        if y-direct_y[i] >= 0 and x-direct_x[i] >= 0 and arr[y][x] == arr[y-direct_y[i]][x-direct_x[i]] :
            continue
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