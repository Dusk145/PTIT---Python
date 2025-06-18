if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        temp = input().split()
        a.append(temp)
    if n > m:
        b = set()
        cnt = 0
        for i in range(n - m):
            b.add(cnt)
            cnt += 2
        for i in range(n):
            if i not in b:
                print (*a[i])
    elif n < m:
        b = set()
        cnt = 1
        for i in range(m - n):
            b.add(cnt)
            cnt += 2
        for i in range(n):
            for j in range(m):
                if j not in b:
                    print (a[i][j], end = " ")
            print ()
    else:
        for i in range(n):
            print (*a[i])