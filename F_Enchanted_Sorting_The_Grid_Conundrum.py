t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]
    g_sorted = [sorted(row) for row in grid]

    bi = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] != g_sorted[i][j]:
                bi.append(j)
        if len(bi) >= 2:
            break

    if len(bi) == 0:
        print("1 1")  
    elif len(bi) != 2:
        print("-1")   
    else:
        for i in range(n):
            grid[i][bi[0]], grid[i][bi[1]] = grid[i][bi[1]], grid[i][bi[0]]

        for i in range(n):
            for j in range(m):
                if grid[i][j] != g_sorted[i][j]:
                    print("-1")  
                    break
            else:
                continue
            break
        else:
            print(f"{bi[0]+1} {bi[1]+1}")
