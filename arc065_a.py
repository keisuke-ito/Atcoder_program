import sys

S = input()
S = S[::-1]
li = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(len(li)):
    li[i] = li[i][::-1]

i = 0
can = True
while i < len(S):
    can2 = False
    # print("i: {}, len(S): {}".format(i, len(S)))
    for j in range(4):
        d = li[j]
        # print("d:{}".format(d))
        # print("len(d): {}".format(len(d)))
        # print("S[i:i+len(d)]: {}".format(S[i:i+len(d)]))
        if S[i:(i+len(d))] == d:
            can2 = True
            i += len(d)
            # print("成功, i:{}".format(i))
            break
        # print("失敗")

    if can2 == False:
        # print("失敗, i:{}".format(i))
        can = False
        break

if can:
    print('YES')
else:
    print('NO')









