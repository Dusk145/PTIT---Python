def res():
    for i in range(len(s)):
        if ok[i]:
            a.append(s[i])
            ok[i] = False
            if len(a) == len(s):
                print ("".join(a))
            else:
                res()
            a.pop()
            ok[i] = True

if __name__ == "__main__":
    s = input()
    ok = [True] * len(s)
    a = []
    res()