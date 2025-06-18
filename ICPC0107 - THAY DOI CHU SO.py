def change(s, n, m):
    temp = ""
    for i in s:
        if i == n:
            temp += m
        else:
            temp += i
    return int(temp)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = input().split()
        a = input()
        if len(a.split()) > 1:
            a, b = a.split()
        else:
            b = input()
        if n > m:
            n, m = m, n
        print (change(a, m, n) + change(b, m, n), change(a, n, m) + change(b, n, m))