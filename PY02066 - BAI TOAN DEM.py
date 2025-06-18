if __name__ == "__main__":
    n = int(input())
    a = set()
    cnt = 0
    while cnt < n:
        temp = input().split()
        a.update(map(int, temp))
        cnt += len(temp)
    ok = True
    for i in range(1, max(a) + 1):
        if i not in a:
            print (i)
            ok = False
    if ok:
        print ("Excellent!")