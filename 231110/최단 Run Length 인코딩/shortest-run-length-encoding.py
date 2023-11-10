word = input()
N = len(word)
i = 0
while i < N :
    if word[0] != word[-1] : break
    word = word[-1] + word[:-1]
    i += 1
cnt = 1
result = 0
for i in range(N-1) :
    if word[i] != word[i+1] :
        result += len(str(cnt))+1
        cnt = 1
    else : cnt += 1
result += len(str(cnt))+1
print(result)