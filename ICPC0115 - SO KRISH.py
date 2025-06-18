def temp():
    a.append(1)
    a.append(1)
    for i in range(2, 10):
        a.append(a[i - 1] * i)

if __name__ == "__main__":
    t = int(input())
    a = []
    temp()
    for _ in range(t):
        n = input()
        S = 0
        for i in range(len(n)):
            S += a[int(n[i])]
        if S == int(n):
            print ("Yes")
        else:
            print ("No")