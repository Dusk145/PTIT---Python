if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(input().split())
        print (*a[k:], *a[:k])