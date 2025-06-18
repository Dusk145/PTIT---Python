if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        a = set(list(n))
        ok = True
        if len(a) == 2:
            for i in range(len(n) - 2):
                if n[i] == n[i + 2]:
                    continue
                ok = False
        else:
            ok = False
        if ok:
            print ("YES")
        else:
            print ("NO")