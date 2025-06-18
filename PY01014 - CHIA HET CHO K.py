if __name__ == "__main__":
    a, k, n = map(int, input().split())
    if a >= n:
        print ("-1")
    else:
        temp = (a // k + 1) * k - a
        if temp > n - a:
            print ("-1")
        else:
            for i in range(temp, n - a + 1, k):
                print (i, end = " ")
            print ()