def res(i):
    for j in range(i, len(a)):
        b.append(a[j])
        if len(b) == k:
            for l in b:
                print (l, end = " ")
            print ()
        else:
            res(j + 1)
        b.pop()

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = sorted(set(list(map(int, input().split()))))
    b = []
    res(0)