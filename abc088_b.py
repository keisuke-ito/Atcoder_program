N = int(input())
number = list(map(int, input().split()))

Alice = 0
Bob = 0

number.sort(reverse=True)

for i in range(N):
    if (i % 2) == 0:
        Alice += number[i]
    else:
        Bob   += number[i]

print(Alice - Bob)