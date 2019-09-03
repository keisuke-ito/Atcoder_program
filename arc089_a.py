N = int(input())
All = [list(map(int, input().split())) for _ in range(N)]
t = [row[0] for row in All]
x = [row[1] for row in All]
y = [row[2] for row in All]
pre_x = 0
pre_y = 0
pre_t = 0

can = True
for n in range(N):
    can2 = False
    T  = abs(t[n] - pre_t)
    dx = abs(x[n] - pre_x)
    dy = abs(y[n] - pre_y)
    # print(T,dx,dy)
    if dx + dy == 0 and T % 2 == 0:
        can2 = True
        # print("成功")
    elif dx + dy == 0 and T % 2 != 0:
        can2 = False
        # print("失敗")
        break

    if (T % (dx + dy)) == 0:
        can2 = True
        # print("成功")

    if can2 == False:
        can = False
        # print("失敗")
        break

    pre_t = t[n]
    pre_x = x[n]
    pre_y = y[n]

if can == True:
    print("Yes")
else:
    print("No")


##############################
#          別解              #
##############################
# こっちの方が早い

N = int(input())
All = [list(map(int, input().split())) for _ in range(N)]
pre_x = 0
pre_y = 0
pre_t = 0

can = True
for n in range(N):
    can2 = False
    T = All[n][0] - pre_t
    d = abs(All[n][1] - pre_x) + abs(All[n][2] - pre_y)
    # print(T, d)
    if d <= T and T % 2 ==  d % 2:
        can2 = True

    if can2 == False:
        can = False
        break

    pre_t = All[n][0]
    pre_x = All[n][1]
    pre_y = All[n][2]

if can == True:
    print("Yes")
else:
    print("No")
