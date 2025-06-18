if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = {}
        for i in input().split():
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in a:
            if a[i] % 2 == 1:
                print (i)