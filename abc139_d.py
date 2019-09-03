import sys
## 4 ##

N = int(input())
# pre = list(range(1,N+1))
# new = pre[:] # スライスを使うことでコピーを作成することができる。そのままの代入ではidは同一のため一つ変更すると同様に変更される。
# a0 = new[0]
# new.remove(a0)
# new.append(a0)

ans = (N * (N - 1)) // 2
print(ans)