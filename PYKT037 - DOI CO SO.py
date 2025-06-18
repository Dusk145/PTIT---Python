if __name__ == "__main__":
    t = int(input())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(t):
        n, k = map(int, input().split())
        res = ""
        while n != 0:
            temp = n % k
            if temp >= 10:
                res += s[temp - 10]
            else:
                res += str(temp)
            n //= k
        print ("".join(reversed(res)))