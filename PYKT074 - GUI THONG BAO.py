if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().split()
        res = s[0]
        for i in range(1, len(s)):
            if len(res) + len(s[i]) + 1 > 100:
                break
            res += (" " + s[i])
        print (res)