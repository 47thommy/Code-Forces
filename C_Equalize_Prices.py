def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        tk = a[0] + k
        if abs(tk - a[0]) <= k and abs(tk - a[-1]) <= k:
            print(tk)
        else:
            print(-1)

if __name__ == "__main__":
    main()
