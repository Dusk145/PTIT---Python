if __name__ == "__main__":
    x = open("DATA1.in", "r")
    y = open("DATA2.in", "r")
    a = set(x.read().lower().split())
    b = set(y.read().lower().split())
    print (" ".join(sorted(a.difference(b))))
    print (" ".join(sorted(b.difference(a))))