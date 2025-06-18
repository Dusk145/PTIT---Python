if __name__ == "__main__":
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    b, c = [], []
    for i in a:
        if i % 2 == 0:
            b.append(i)
        else:
            c.append(i)
    b, c = sorted(b), sorted(c)
    idx1, idx2 = 0, len(c) - 1
    for i in a:
        if i % 2 == 0:
            print (b[idx1], end = " ")
            idx1 += 1
        else:
            print (c[idx2], end = " ")
            idx2 -= 1