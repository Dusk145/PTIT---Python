def div(n, k, temp):
    if k == 1:
        print ("A")
    elif k == temp:
        print (chr(ord("A") + n))
    else:
        if k > temp:
            k -= temp
        div(n - 1, k, temp // 2)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        div(n, k, 2 ** n)