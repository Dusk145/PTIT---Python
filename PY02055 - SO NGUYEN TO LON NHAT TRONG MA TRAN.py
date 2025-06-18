import math

def nt():
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(1001)) + 1):
        if a[i]:
            for j in range(i * i, 1001, i):
                a[j] = False

if __name__ == "__main__":
    a = [True] * 1001
    nt()
    n, m = map(int, input().split())
    b = []
    c = set()
    for i in range(n):
        temp = input().split()
        for j in temp:
            c.add(int(j))
        b.append(temp)
    temp = 0
    c = sorted(c)
    for i in range(len(c) - 1, -1, -1):
        if a[c[i]]:
            temp = c[i]
            break
    if temp == 0:
        print ("NOT FOUND")
    else:
        print (temp)
        for i in range(n):
            for j in range(m):
                if int(b[i][j]) == temp:
                    print ("Vi tri [" + str(i) + "][" + str(j) + "]")