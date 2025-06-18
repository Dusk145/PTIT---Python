def res(i):
    for j in range(i, len(a)):
        b.append(a[j])
        if len(b) == k:
            print (" ".join(b))
        else:
            res(j + 1)
        b.pop()

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = sorted(set(input().split()))
    b = []
    res(0)