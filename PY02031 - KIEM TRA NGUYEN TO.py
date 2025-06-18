def nt():
    ok[0] = ok[1] = False
    for i in range(2, int(1000 ** 0.5) + 1):
        if ok[i]:
            for j in range(i * i, 1001, i):
                ok[j] = False

if __name__ == "__main__":
    ok = [True] * 1001
    nt()
    n, m = map(int, input().split())
    a = [input().split() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if ok[int(a[i][j])]:
                print ("1", end = " ")
            else:
                print ("0", end = " ")
        print ()