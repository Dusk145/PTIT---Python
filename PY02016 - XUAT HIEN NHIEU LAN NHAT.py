if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = [0] * 2000000
        for i in range(len(a)):
            b[a[i]] += 1
        if max(b) > len(a) / 2:
            print (b.index(max(b)))
        else:
            print ("NO")