if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        x = 0
        y = 1
        ok = False
        for i in range(len(n)):
            if i % 2 == 0:
                x += int(n[i])
            else:
                if n[i] != "0":
                    ok = True
                    y *= int(n[i])
        print (x, end = " ")
        if not ok:
            y = 0
        print (y)