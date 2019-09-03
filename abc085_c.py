"""
お札
10000
5000
1000
"""


N, Y = map(int, input().split())

count = 0
for a in range(N+1):
    y = 10000*a
    if y > Y:
        continue

    for b in range(N+1):
        c = N - a - b
        total = y + 5000*b + 1000*c

        if total == Y and c >= 0:
            print("{} {} {}".format(a,b,c))
            count += 1
            break
    else:
        continue
    break

if count == 0:
    print("-1 -1 -1")
