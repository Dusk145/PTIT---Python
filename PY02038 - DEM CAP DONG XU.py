import math

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    b = []
    for i in range(n):
        cnt1, cnt2 = 0, 0
        for j in range(n):
            if a[i][j] == "C":
                cnt1 += 1
            if a[j][i] == "C":
                cnt2 += 1
        b.append(cnt1)
        b.append(cnt2)
    res = 0
    for i in b:
        if i > 1:
            res += math.comb(i, 2)
    print (res)