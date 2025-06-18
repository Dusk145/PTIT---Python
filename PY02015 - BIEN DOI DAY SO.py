if __name__ == "__main__":
    while True:
        a = list(map(int, input().split()))
        if a[0] == 0 and len(set(a)) == 1:
            break
        b = []
        for i in range(4):
            b.append(a[i])
        cnt = 0
        while len(set(a)) != 1:
            for i in range(4):
                a[i] = abs(b[i] - b[(i + 1) % 4])
            for i in range(4):
                b[i] = a[i]
            cnt += 1
        print (cnt)