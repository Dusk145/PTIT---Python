if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(len(a)):
        if len(b) == 0 or (a[i] + b[-1]) % 2 != 0:
            b.append(a[i])
        else:
            b.pop()
    print (len(b))