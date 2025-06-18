def fee(s, n):
    if s == "Xe_con":
        if n == 5:
            return 10000
        elif n == 7:
            return 15000
    elif s == "Xe_tai" and n == 2:
        return 20000
    elif s == "Xe_khach":
        if n == 29:
            return 50000
        elif n == 45:
            return 70000

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        temp = input().split()
        a.append(temp)
    idx = 0
    while idx < len(a):
        temp = a[idx][-1]
        S = 0
        while idx < len(a) and a[idx][-1] == temp:
            if a[idx][-2] == "IN":
                S += fee(a[idx][1], int(a[idx][2]))
            idx += 1
        print (temp + ": " + str(S))