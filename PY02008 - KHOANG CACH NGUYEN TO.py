import math

def nt():
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(10000)) + 1):
        if a[i]:
            for j in range(i * i, 10000, i):
                a[j] = False

if __name__ == "__main__":
    a = [True] * 10000
    nt()
    b = []
    for i in range(10000):
        if a[i]:
            b.append(i)
    n, m = map(int, input().split())
    temp = int(m)
    print (temp, end = " ")
    for i in range(n):
        print (temp + b[i], end = " ")
        temp += b[i]