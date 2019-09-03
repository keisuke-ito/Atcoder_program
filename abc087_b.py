
money = [int(input()) for i in range(3)]
N = int(input())

res = 0

for l in range(money[0]+1):
    for m in range(money[1]+1):
        for n in range(money[2]+1):
            if N == 500*l + 100*m + 50*n:
                res += 1

print(res)