def solve(tc):
    n, k = map(int, input().split())
    s = input().strip()
    
    mp = {}
    for ch in s:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] = 1

    even = 0
    odd = 0

    for count in mp.values():
        if count % 2 == 0:
            even += 1
        else:
            odd += 1

    if k < odd - 1:
        print("NO")
    else:
        print("YES")

t = int(input())
for i in range(1, t + 1):
    solve(i)
