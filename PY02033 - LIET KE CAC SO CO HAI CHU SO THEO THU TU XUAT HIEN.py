if __name__ == "__main__":
    n = input()
    a = set()
    b = []
    for i in range(0, len(n), 2):
        if i + 1 < len(n):
            temp = n[i] + n[i + 1]
            if int(temp) not in a:
                a.add(int(temp))
                b.append(int(temp))
    print (*b)