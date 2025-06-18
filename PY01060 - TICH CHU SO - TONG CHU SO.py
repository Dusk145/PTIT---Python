if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        x = 1
        y = 0
        ok = False
        for i in range(len(n)):
            if i % 2 == 0:
                if n[i] != "0":
                    ok = True
                    x *= int(n[i])
            else:
                y += int(n[i])
        if not ok:
            x = 0
        print (x, y, sep = " ")