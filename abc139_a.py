## 1 ##
S = input().split()
T = input().split()
S = list(S[0])
T = list(T[0])

count = 0
for i in range(3):

    if S[i] == T[i]:
        count += 1


print(count)



