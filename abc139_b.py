## 2 ##
# A, B = map(int, input().split())
#
# count = 0
# if B != 1:
#     count += 1
#     tap = A
#     while tap < B:
#         count += 1
#         tap = count * (A - 1) + 1
#
# print(count)


# 別解
A, B = map(int, input().split())

count = 0
outlet = 1

while outlet < B:
    outlet -= 1
    outlet += A
    count += 1

print(count)

