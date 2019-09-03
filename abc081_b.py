
N = int(input())
A = list(map(int, input().split()))

iteral = 0
odd = 0
while True:
    for i in range(N):
        if A[i] % 2 != 0:
            odd += 1
        A[i] /= 2

    if odd != 0:
        break

    iteral += 1

print(iteral)
