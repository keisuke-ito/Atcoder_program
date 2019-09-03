import sys

N = int(input())
a = list(map(int, input().split()))
color = [0,0,0,0,0,0,0,0,0]

for i in range(N):
    if 1 <= a[i] <= 399:
        color[0] = 1
    elif 400 <= a[i] <= 799:
        color[1] = 1
    elif 800 <= a[i] <= 1199:
        color[2] = 1
    elif 1200 <= a[i] <= 1599:
        color[3] = 1
    elif 1600 <= a[i] <= 1999:
        color[4] = 1
    elif 2000 <= a[i] <= 2399:
        color[5] = 1
    elif 2400 <= a[i] <= 2799:
        color[6] = 1
    elif 2800 <= a[i] <= 3199:
        color[7] = 1
    else:
        color[8] += 1
co = color[:8]
zero = co.count(0)
one = co.count(1)
max = one + color[8]

if one == 0 and color[8] > 0:
    min = 1
else:
    min = one

print("{} {}".format(min, max))
