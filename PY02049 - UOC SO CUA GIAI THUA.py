if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        cnt = 0
        for i in range(p, n + 1, p):
            temp = i
            while temp % p == 0:
                cnt += 1
                temp //= p
        print (cnt)