n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp1 = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp2 = [[0 for _ in range(m+1)] for _ in range(n+1)]

Max = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] < 1 : continue
        # 상하 연속
        dp1[i+1][j+1] = dp1[i][j+1]+1
        # 좌우 연속
        dp2[i+1][j+1] = dp2[i+1][j]+1
        t_y = dp1[i+1][j+1]
        t_x = dp2[i+1][j+1]
        for x in range(j+1, 0, -1) :
            if t_y > dp1[i+1][x] :
                t_y = dp1[i+1][x]
            if t_y == 0 : break
            if Max < t_y * (j-x+2) :
                Max = t_y * (j-x+2)
                
        for y in range(i+1, 0, -1) :
            if t_x > dp2[y][j+1] :
                t_x = dp2[y][j+1]
            if t_x == 0 : break
            if Max < t_x * (i-y+2) :
                Max = t_x * (i-y+2)

print(Max)