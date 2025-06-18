if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        ok = True
        for i in range(len(s)):
            if s[i] != '0' and s[i] != '1' and s[i] != '2':
                ok = False
                print ("NO")
                break
        if ok:
            print ("YES")