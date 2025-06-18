def sum_digit(n):
    n = str(n)
    S = 0
    for i in n:
        S += int(i)
    return S

if __name__ == "__main__":
    while True:
        s = input()
        if s == "-1":
            break
        n, h = map(int, s.split())
        cnt = 0
        for i in range(h, n):
            if sum_digit(i) == h:
                cnt += 1
        print (cnt)