n = int(input())
a = list(map(int, input().split()))
s, v = 0, 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        s, v = i, v + 1
if a[n - 1] > a[0]:
    s, v = n - 1, v + 1
if v == 0:
    print(0)
elif v > 1:
    print(-1)
else:
    print(n - 1 - s)