if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        i = 0
        while i < len(s):
            c = s[i]
            cnt = 1
            i += 1
            while i < len(s) and c == s[i]:
                cnt += 1
                i += 1
            print (str(cnt) + c, end = "")
        print ()