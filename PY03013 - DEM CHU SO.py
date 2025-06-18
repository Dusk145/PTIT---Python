if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = {}
        for i in range(0, 10):
            a[str(i)] = 0
        for i in range(n, m + 1):
            temp = str(i)
            for j in temp:
                a[j] += 1
        for i in a:
            print (a[i], end = " ")
        print ()