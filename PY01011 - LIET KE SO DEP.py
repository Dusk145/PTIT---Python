def check(n):
    if len(n) % 2 == 1 or n != n[::-1]:
        return False
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(22, n):
            if check(str(i)):
                print (i, end = " ")
        print ()