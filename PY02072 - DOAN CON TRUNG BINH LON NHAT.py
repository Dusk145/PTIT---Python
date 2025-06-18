if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    maxi = max(a)
    res, i = 0, 0
    while i < n:
        if a[i] == maxi:
            cnt = 0
            while i < n and a[i] == maxi:
                cnt += 1
                i += 1
            res = max(res, cnt)
        else:
            i += 1
    print (res)