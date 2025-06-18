if __name__ == "__main__":
    n = input()
    m = int(input())
    a = []
    b = set()
    c = [0] * 100
    for i in range(0, len(n), 2):
        if i + 1 < len(n):
            temp = int(n[i] + n[i + 1])
            c[temp] += 1
            if temp not in a:
                b.add(temp)
                a.append(temp)
    ok = False
    for i in sorted(a):
        if c[i] >= m:
            print (i, c[i])
            ok = True
    if not ok:
        print ("NOT FOUND")