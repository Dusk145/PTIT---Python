def res(n, a, b, c):
    if n == 0:
        return
    res(n - 1, a, c, b)
    print (a + " -> " + c)
    res(n - 1, b, a, c)

if __name__ == "__main__":
    n = int(input())
    res(n, "A", "B", "C")