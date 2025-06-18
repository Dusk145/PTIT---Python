import math

def nt(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for i in range(2, n + 1):
        if a[i]:
            b.append(i)
            for j in range(i * i, n + 1, i):
                a[j] = False

if __name__ == "__main__":
    n = int(input())
    b = []
    nt(int(math.sqrt(n)) + 1)
    cnt = 0
    for i in b:
        if i ** 8 <= n:
            cnt += 1
        else:
            break
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            if (b[i] * b[i]) * (b[j] * b[j]) <= n:
                cnt += 1
            else:
                break
    print (cnt)