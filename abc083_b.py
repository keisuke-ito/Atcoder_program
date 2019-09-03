
def findsum(n):
    sum = 0 # 各桁の和
    while n > 0:
        q, mod = divmod(n, 10)
        sum += mod
        n = q
    return sum

N, A, B = map(int, input().split())

arr = range(1,N+1)

sum = 0 # 条件内の各桁の和の合計
for i in range(N):
    a = findsum(arr[i])

    if A <= a <= B:
        sum += arr[i]

print(sum)