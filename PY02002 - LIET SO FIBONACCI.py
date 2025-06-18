def fibo():
    a.append(1)
    a.append(1)
    for i in range(2, 93):
        a.append(a[i - 1] + a[i - 2])

if __name__ == "__main__":
    t = int(input())
    a = []
    fibo()
    for _ in range(t):
        n, m = map(int, input().split())
        for i in range(n, m + 1):
            print (a[i - 1], end = " ")
        print ()