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
            if i < j:
                S1 += a[i][j]
            elif i > j:
                S2 += a[i][j]
    if abs(S1 - S2) < m:
        print ("YES")
    else:
        print ("NO")
    print (abs(S1 - S2))