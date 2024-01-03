def find_balanced_substring(t, testcases):
    results = []

    for _ in range(t):
        n, s = testcases[_]
        prefix_count = [0] * (n + 1)
        l, r = -1, -1

        for i in range(n):
            prefix_count[i + 1] = prefix_count[i] + (s[i] == 'a')

        for i in range(n):
            for j in range(i, n):
                a_count = prefix_count[j + 1] - prefix_count[i]
                b_count = (j - i + 1) - a_count

                if a_count == b_count:
                    l, r = i + 1, j + 1
                    break

        results.append((l, r))

    return results


t = int(input())
testcases = []

for _ in range(t):
    n = int(input())
    s = input()
    testcases.append((n, s))

results = find_balanced_substring(t, testcases)

for result in results:
    if result == (-1, -1):
        print(-1, -1)
    else:
        print(result[0], result[1])
