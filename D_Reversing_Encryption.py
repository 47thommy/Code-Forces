n = int(input())
s = input().strip()

rev = []
for i in range(1, n + 1):
    if n % i == 0:
        rev.append(i)

n = len(rev)
for i in range(n):
    m = rev[i]
    t = s[:m][::-1]
    s = t + s[m:]

print(s)
