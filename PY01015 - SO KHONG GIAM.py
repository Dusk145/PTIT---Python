if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        ok = True
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                ok = False
                print ("NO")
                break
        if ok:
            print ("YES")