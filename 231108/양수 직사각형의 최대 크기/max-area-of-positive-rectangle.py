n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0] for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1) :
    dp[i][0] = [i, 0]
for j in range(m+1) :
    dp[0][j] = [0, j]
Max = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] < 1 : continue
        dp[i+1][j+1] = [min(dp[i][j][0], dp[i][j+1][0])+1, min(dp[i][j][1], dp[i+1][j][1])+1]
        if Max < dp[i+1][j+1][0] * dp[i+1][j+1][1] :
            Max = dp[i+1][j+1][0] * dp[i+1][j+1][1]
if Max == 0 :
    print(-1)
else :
    print(Max)