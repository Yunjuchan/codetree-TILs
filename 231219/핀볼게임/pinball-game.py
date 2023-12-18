direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
def dfs(direction, y, x) :
    level = 0
    while True :
        level += 1
        if y < 0 or x < 0 or y >= N or x >= N : 
            return level
        if arr[y][x] == 1 :
            direction += 1
        elif arr[y][x] == 2 :
            direction -= 1
        if direction < 0 or direction >= 4 :
            direction %= 4
        y += direct_y[direction]
        x += direct_x[direction]




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0

for i in range(N) :
    for j in range(N) :
        if i == 0 :
            tmp = dfs(0, i, j) 
            if Max < tmp :
                Max = tmp
        if i == N-1 :
            tmp = dfs(2, i, j)
            if Max < tmp :
                Max = tmp
        if j == 0 :
            tmp = dfs(1, i, j)
            if Max < tmp :
                Max = tmp
        if j == N-1 :
            tmp = dfs(3, i, j)
            if Max < tmp :
                Max = tmp
print(Max)