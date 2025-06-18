if __name__ == "__main__":
    m = int(input())
    v = int(input())
    t = int(input())
    d = input()
    s = v * t
    if d == "A":
        print (-s % m)
    elif d == "C":
        print (s % m)