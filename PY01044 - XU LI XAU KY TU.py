if __name__ == "__main__":
    a = input().lower()
    b = input().lower()
    x = set(list(a.split()))
    y = set(list(b.split()))
    for i in sorted(x.union(y)):
        print (i, end = " ")
    print ()
    for i in sorted(x.intersection(y)):
        print (i, end = " ")