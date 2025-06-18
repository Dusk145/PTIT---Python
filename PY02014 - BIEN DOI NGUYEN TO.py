def nt():
    ok[0] = ok[1] = False
    for i in range(2, int(10001 ** 0.5)):
        if ok[i]:
            for j in range(i * i, 10001, i):
                ok[j] = False

if __name__ == "__main__":
    ok = [True] * 10001
    nt()
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    res = 0
    for i in a:
        if not ok[i]:
            temp1, temp2 = i, i
            while not ok[temp1] and not ok[temp2]:
                temp1 += 1
                temp2 -= 1
            if ok[temp1]:
                res = max(res, temp1 - i)
            elif ok[temp2]:
                res = max(res, i - temp2)
    print (res)