Y , M, D = map(int, input().split())
def isYun(y) :
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0) :
        return True
    return False
days = [31, 29 if isYun(Y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def printWeather(m, d) :
    if d > days[m-1] :
        return -1

    if 1 <= m < 3 or m == 12 :
        return 'Winter'
    elif m < 6 : return 'Spring'
    elif m < 9 : return 'Summer'
    else : return 'Fall'

result = printWeather(M, D)
print(result)