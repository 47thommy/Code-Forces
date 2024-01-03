def solve():
    n = int(input())
    a = list(map(int, input().split()))
    v = []
    s = set()
    
    no = False
    c = 1
    i = 0
    while i < n:
        if i == n - 1 or a[i] != a[i + 1]:
            if c < 2:
                print("-1")
                no = True
                break
            else:
                if i == n - 1:
                    v.append(i + 1)
                    for j in range(i - c + 2, i + 1):
                        v.append(j)
                else:
                    v.append(i + 1)
                    for j in range(i - c + 2, i + 1):
                        v.append(j)
            c = 0
        c += 1
        i += 1
    
    if not no:
        print(*v)

t = int(input())
for _ in range(t):
    solve()
