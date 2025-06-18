if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = set(input())
        ok = True
        for i in a:
            if i != '4' and i != '7':
                print ("NO")
                ok = False
                break
        if ok:
            print ("YES")