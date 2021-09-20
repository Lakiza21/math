from random import randint

k,m,l = 0, 0, 0
n = 100
for i in range(0, n):
    x = randint (0, 10)
    l=l+1
    if x<5:
        k = k + 1
    else:
        m = m + 1
if k+m==l:
  print(True)
else:
  print(False)
print(k,m,l)