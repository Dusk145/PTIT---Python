if __name__ == "__main__":
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        res = ""
        while n:
            res += s[n % k]
            n //= k
        print ("".join(reversed(res)))