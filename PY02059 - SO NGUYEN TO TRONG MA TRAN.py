def nt():
    ok[0] = ok[1] = False
    for i in range(2, int(1001 ** 0.5)):
        if ok[i]:
            for j in range(i * i, 1001, i):
                ok[j] = False

if __name__ == "__main__":
    ok = [True] * 1001
    nt()
    n, m = map(int, input().split())
    a = []
    b = set()
    for i in range(n):
        temp = input().split()
        a.append(temp)
        b.update(map(int, temp))
    temp = 0
    for i in sorted(b, reverse = True):
        if ok[i]:
            temp = i
            break
    if temp == 0:
        print ("NOT FOUND")
    else:
        print (temp)
        for i in range(n):
            for j in range(m):
                if a[i][j] == str(temp):
                    print (f"Vi tri [{i}][{j}]")