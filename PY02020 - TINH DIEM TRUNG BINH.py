if __name__ == "__main__":
    n = int(input())
    a = sorted(map(float, input().split()))
    mini = a[0]
    maxi = a[- 1]
    S = 0.0
    cnt = 0
    for i in a:
        if i != mini and i != maxi:
            S += i
            cnt += 1
    print (round(S / cnt, 2))