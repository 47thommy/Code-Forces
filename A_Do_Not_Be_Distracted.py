t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    mp = {chr(i): 0 for i in range(65, 98)}
    found = False
    for i in range(n):
        if i != 0:
            if s[i] != s[i - 1] and mp[s[i]] > 0:
                found = True
                print("NO")
                break
        mp[s[i]] += 1
    if not found:
        print("YES")
