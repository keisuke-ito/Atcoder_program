a,b = input().split()

r = int(a + b)
ma = 0
for i in range(1,1000):
    if r == i*i:
        ma = 1

if ma == 1:
    print("Yes")
else:
    print("No")




