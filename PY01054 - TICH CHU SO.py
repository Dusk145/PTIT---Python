if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        S = 1
        for i in n:
            if i != '0':
                S *= int(i)
        print (S)