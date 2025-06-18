if __name__ == "__main__":
    n = input()
    a = set()
    for i in range(0, len(n), 2):
        if i + 1 < len(n):
            a.add(int(n[i] + n[i + 1]))
    print (*sorted(a))