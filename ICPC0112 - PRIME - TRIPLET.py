import math

def nt(n, a):
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [True] * (n + 1)
        nt(n + 1, a)
        b = []
        for i in range(len(a)):
            if a[i]:
                b.append(i)
        cnt = 0
        for i in range(len(b) - 2):
            if b[i] + 6 == b[i + 2]:
                if b[i] + 2 == b[i + 1] or b[i] + 4 == b[i + 1]:
                    cnt += 1
        print (cnt)