if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = list(map(int, input()))
        if len(a) < 2:
            print ("NO")
            continue
        idx_max = a.index(max(a))
        ok = True
        for i in range(idx_max):
            if a[i] >= a[i + 1]:
                ok = False
                break
        if ok:
            for i in range(idx_max, len(a) - 1):
                if a[i] <= a[i + 1]:
                    ok = False
                    break
        if ok:
            print ("YES")
        else:
            print ("NO")