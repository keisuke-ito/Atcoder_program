
a = list(input())
count = 0

for i in range(len(a)):
    if a[i] == '1':
        count += 1

print(count)