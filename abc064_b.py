import sys

N = int(input())
a = list(map(int, input().split()))
a.sort()
print(a)

d = 0
for i in range(1,N):
    D = abs(a[i] - a[i-1])
    d += D

print(d)

#########
#  別解 #
#########
# 一番早い

N = int(input())
a = list(map(int, input().split()))

d = max(a) - min(a)
print(d)



