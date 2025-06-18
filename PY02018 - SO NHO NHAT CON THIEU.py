if __name__ == "__main__":
    n = int(input())
    a = sorted(map(int, input().split()))
    ok = [False] * 40000
    for i in a:
        ok[i] = True
    for i in range(1, 40000):
        if not ok[i]:
            print (i)
            break