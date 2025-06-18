def check(n):
    return len(n) >= 2 and n == n[:: -1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    b = set()
    for i in range(n):
        temp = input().split()
        a.append(temp)
        for j in temp:
            b.add(int(j))
    b = sorted(b)
    temp = -1
    for i in range(len(b) - 1, -1, -1):
        if check(str(b[i])):
            temp = b[i]
            break
    if temp == -1:
        print ("NOT FOUND")
    else:
        print (temp)
        for i in range(n):
            for j in range(m):
                if int(a[i][j]) == temp:
                    print ("Vi tri [" + str(i) + "][" + str(j) + "]")