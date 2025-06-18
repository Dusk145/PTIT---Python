if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        temp = input().split()
        a.append(temp)
    idx = 0
    b = []
    while idx < n:
        if len(a[idx]) == 6:
            b.append(1)
            while idx < n:
                if len(a[idx]) == 6 and idx + 1 < n and len(a[idx + 1]) == 8:
                    idx += 2
                else:
                    break
        elif len(a[idx]) == 7 and idx + 3 < n:
            b.append(2)
            idx += 4
    print (len(b))
    print (*b, sep = "\n")