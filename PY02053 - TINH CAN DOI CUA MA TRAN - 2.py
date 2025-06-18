if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        temp = list(map(int, input().split()))
        a.append(temp)
    m = int(input())
    S1 = S2 = 0
    for i in range(n):
        for j in range(n):
            if i + j + 1 < n:
                S1 += a[i][j]
            elif i + j + 1 > n:
                S2 += a[i][j]
    temp = abs(S1 - S2)
    if temp <= m:
        print ("YES")
    else:
        print ("NO")
    print (temp)