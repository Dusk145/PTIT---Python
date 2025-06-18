def check(s):
    return s == s[::-1]

if __name__ == "__main__":
    f = open("VANBAN.in", "r")
    a, b = {}, []
    for i in f:
        for j in i.split():
            if check(j):
                if j in a:
                    a[j] += 1
                else:
                    a[j] = 1
                    b.append(j)
    b.sort(key = lambda x : (-len(x)))
    print (b[0], a[b[0]])
    for i in range(1, len(b)):
        if len(b[i]) == len(b[0]):
            print (b[i], a[b[i]])
        else:
            break