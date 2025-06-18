def change1(n):
    if n <= 9:
        return str(n)
    return chr(ord("A") + n - 10)

def change2(n, m):
    res = ""
    while n != 0:
        res = change1(n % m) + res
        n //= m
    return res

if __name__ == "__main__":
    temp = open("DATA.in", "r")
    for i in range(int(temp.readline())):
        m = int(temp.readline())
        n = temp.readline().strip()
        S = 0
        for i in range(len(n)):
            S += int(n[i]) * (2 ** (len(n) - i - 1))
        print (change2(S, m))