if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = 0.0
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                S += (1 / i)
        else:
            for i in range(1, n + 1, 2):
                S += (1 / i)
        print (format(S, ".6f"))