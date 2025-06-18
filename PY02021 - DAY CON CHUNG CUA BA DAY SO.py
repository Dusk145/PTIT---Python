if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = sorted(map(int, input().split()))
        b = sorted(map(int, input().split()))
        c = sorted(map(int, input().split()))
        idx1 = idx2 = idx3 = 0
        ok = False
        while idx1 < n and idx2 < m and idx3 < k:
            if a[idx1] == b[idx2] == c[idx3]:
                print (a[idx1], end = " ")
                idx1 += 1
                idx2 += 1
                idx3 += 1
                ok = True
            elif a[idx1] > b[idx2]:
                idx2 += 1
            elif b[idx2] > c[idx3]:
                idx3 += 1
            elif c[idx3] > a[idx1]:
                idx1 += 1
        if not ok:
            print ("NO")
        else:
            print ()