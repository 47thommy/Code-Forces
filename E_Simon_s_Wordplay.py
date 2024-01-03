MAX_N = 2 * 100 * 1000 + 13
L = 5
balance = [[] for _ in range(L)]
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(L):
        balance[i].clear()

    for _ in range(n):
        s = input()
        init_balance = -len(s)
        for j in range(L):
            balance[j].append(init_balance)
        for c in s:
            balance[ord(c) - ord('a')][-1] += 2
    best_count = 0
    best_letter = 0
    for i in range(L):
        b = balance[i]
        b.sort(reverse=True)
        if b[0] <= 0:
            continue
        sum_balance = b[0]
        j = 1
        while j < n and sum_balance > 0:
            sum_balance += b[j]
            j += 1
        if sum_balance <= 0:
            j -= 1
        if j > best_count:
            best_count = j
            best_letter = i

    print(best_count)
