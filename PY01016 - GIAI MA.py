if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        for i in range(0, len(s), 2):
            c = s[i]
            cnt = int(s[i + 1])
            for j in range(cnt):
                print (c, end = "")
        print ()