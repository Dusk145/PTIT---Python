if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ok = False
        for i in range(1000):
            if n % 7 == 0:
                print (n)
                ok = True
                break
            temp = int(''.join(reversed(str(n))))
            n += temp
        if not ok:
            print ("-1")