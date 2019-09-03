
N = int(input())
a = [int(input()) for _ in range(N)]

a.sort()

sum = 1
now = a[0]
for i in range(1,N):
    if now < a[i]:
        sum += 1
        now = a[i]

    elif now == a[i]:
        now = a[i]

    else:
        break

print(sum)
