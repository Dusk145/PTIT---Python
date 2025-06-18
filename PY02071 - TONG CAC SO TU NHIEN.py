def res(i, n, a, b):
    for j in range(i, n + 1):
        a.append(j)
        if sum(a) == n:
            b.append(a[::-1])
        elif sum(a) < n:
            res(j, n, a, b)
        a.pop()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        b = []
        res(1, n, a, b)
        print (len(b))
        b.sort(reverse = True)
        for i in b:
            print ("(", end = "")
            print (*i, end = "")
            print (")", end = " ")
        print ()