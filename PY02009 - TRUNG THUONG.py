if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = {}
        for i in range(n):
            temp = int(input())
            if temp in a:
                a[temp] += 1
            else:
                a[temp] = 1
        a = sorted(a, key = lambda x: (-a[x], x))
        print (a[0])