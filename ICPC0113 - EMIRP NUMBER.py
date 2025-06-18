import math

def nt():
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(10 ** 6) + 1)):
        if a[i]:
            for j in range(i * i, 10 ** 6, i):
                a[j] = False

def check(n):
    s = str(n)
    return s != s[::- 1]

def change(n):
    s = str(n)
    return int(s[::- 1])

if __name__ == "__main__":
    a = [True] * (10 ** 6)
    nt()
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = [True] * (n + 1)
        for i in range(10, n):
            temp = change(i)
            if a[i] and check(i) and temp < n and a[temp] and b[temp]:
                print (i, temp, end = " ")
                b[temp] = False
                b[i] = False
        print ()