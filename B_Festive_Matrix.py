n = int(input())
arr = []
ans = 0

for _ in range(n):
    arr.append(input().split())

l, r = n - 1, 0

while l >= 0:
    ans += int(arr[r][l])
    l -= 1
    r += 1


l, r = 0, 0

while l < n:
    ans += int(arr[l][r])
    l += 1
    r += 1

for col in range(n):
    ans += int(arr[(n // 2)][col])

for row in range(n):
    ans += int(arr[row][(n // 2)])

ans -= 3 * int(arr[(n // 2)][(n // 2)])

print(ans)
