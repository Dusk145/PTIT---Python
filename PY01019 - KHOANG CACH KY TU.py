if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        temp = ''.join(reversed(s))
        ok = True
        for i in range(1, len(s)):
            if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(temp[i]) - ord(temp[i - 1])):
                print ("NO")
                ok = False
                break
        if ok:
            print ("YES")