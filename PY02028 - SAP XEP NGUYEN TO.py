def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if nt(a[i]):
            for j in range(i + 1, n):
                if nt(a[j]) and a[j] < a[i]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
        print (a[i], end = " ")