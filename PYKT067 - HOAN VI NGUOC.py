def res(a, b):
    idx = len(a) - 2
    while idx > 0 and a[idx] > a[idx + 1]:
        idx -= 1
    if idx == 0:
        b.append("".join(map(str, a)))
    else:
        cnt = len(a) - 1
        while a[idx] > a[cnt]:
            cnt -= 1
        a[idx], a[cnt] = a[cnt], a[idx]
        a[idx + 1:] = a[idx + 1:][::-1]
        b.append("".join(map(str, a)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 1
        a, b = [], []
        a.append(0)
        for i in range(1, n + 1):
            a.append(i)
            cnt *= i
        b.append("".join(map(str, a)))
        print (cnt)
        for i in range(cnt - 1):
            res(a, b)
        b = reversed(b)
        for i in b:
            print (i[1:], end = " ")
        print ()