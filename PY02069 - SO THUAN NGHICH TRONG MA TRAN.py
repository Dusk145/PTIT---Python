def check(n):
    return len(n) >= 2 and n == n[::-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input().split())
    b = []
    for i in range(n):
        for j in range(m):
            if check(a[i][j]):
                b.append(int(a[i][j]))
    if len(b) == 0:
        print ("NOT FOUND")
    else:
        res = max(b)
        print (res)
        for i in range(n):
            for j in range(m):
                if str(res) == a[i][j]:
                    print (f"Vi tri [{i}][{j}]")