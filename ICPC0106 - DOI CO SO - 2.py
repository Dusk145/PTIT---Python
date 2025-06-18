if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        if n == 2:
            print (s)
        else:
            if n == 4:
                if len(s) % 2 != 0:
                    s = "0" + s
                for i in range(0, len(s), 2):
                    temp = int(s[i]) * (2 ** 1) + int(s[i + 1]) * (2 ** 0)
                    print (str(temp), end = "")
            elif n == 8:
                if len(s) % 3 == 1:
                    s = "00" + s
                elif len(s) % 3 == 2:
                    s = "0" + s
                for i in range(0, len(s), 3):
                    temp = int(s[i]) * (2 ** 2) + int(s[i + 1]) * (2 ** 1) + int(s[i + 2]) * (2 ** 0)
                    print (str(temp), end = "")
            elif n == 16:
                a = "0123456789ABCDEF"
                if len(s) % 4 == 1:
                    s = "000" + s
                elif len(s) % 4 == 2:
                    s = "00" + s
                elif len(s) % 4 == 3:
                    s = "0" + s
                for i in range(0, len(s), 4):
                    temp = int(s[i]) * (2 ** 3) + int(s[i + 1]) * (2 ** 2) + int(s[i + 2]) * (2 ** 1) + int(s[i + 3]) * (2 ** 0)
                    print (a[temp], end = "")
            print ()