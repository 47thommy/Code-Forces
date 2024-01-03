full = 'Yes' * 50
t = int(input())
for _ in range(t):
    ans=input()
    if full.find(ans) >= 0:
        print('YES')
    else:
        print('NO')