t = int(input())

for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))

    result = []

    for j in range(n // 2):
        result.append(ar[j])
        result.append(ar[n - j - 1])

    if n % 2 != 0:
        result.append(ar[n // 2])

    print(*result)
