## 3 ##
N = int(input())
H = list(map(int, input().split()))

H = H[::-1] # リストをリバースする
ans = 0
val = 0

for i in range(1, N):
    if H[i-1] <= H[i]:
        val += 1
    else:
        val = 0
    ans = max(ans, val)

print(ans)

# max = 0
# for p in range(N-1):
#     print("H[p] = {}".format(H[p]))
#     count = 0
#     rest_num = len(H) - (p + 1)
#
#     if rest_num < max:
#         break
#     print("rest_num : {}".format(rest_num))
#
#     for q in range(rest_num):
#         if H[p + q] >= H[p + (q+1)]:
#             print("H[p+q] = {}, H[p+q+1] = {}".format(H[p+q], H[p+(q+1)]))
#             count += 1
#             print("count = {}".format(count))
#
#         if max < count:
#             print("change count: {}".format(count))
#             max = count
#
# print(max)
