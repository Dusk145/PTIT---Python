if __name__ == "__main__":
    while True:
        s = input()
        if s == "-1":
            break
        y, z = s.split()
        a = map(int, list(y))
        print (int(z) // sum(a))