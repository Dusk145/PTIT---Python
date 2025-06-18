if __name__ == "__main__":
    n = input()
    a = []
    b = [0] * 100
    c = set()
    for i in range(0, len(n), 2):
        if i + 1 < len(n):
            temp = n[i] + n[i + 1]
            b[int(temp)] += 1
            if int(temp) not in c:
                c.add(int(temp))
                a.append(int(temp))
    for i in a:
        print (i, b[i])