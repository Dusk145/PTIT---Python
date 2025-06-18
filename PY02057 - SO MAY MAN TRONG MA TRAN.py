if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    b = set()
    for i in range(n):
        temp = input().split()
        a.append(temp)
        for j in temp:
            b.add(int(j))
    temp = max(b) - min(b)
    ok = False
    for i in range(n):
        for j in range(m):
            if a[i][j] == str(temp):
                if not ok:
                    print (temp)
                print (f"Vi tri [{i}][{j}]")
                ok = True
    if not ok:
        print ("NOT FOUND")