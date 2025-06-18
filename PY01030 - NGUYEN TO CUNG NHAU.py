import math

if __name__ == "__main__":
    n, k = map(int, input().split())
    cnt = 0
    for i in range(pow(10, k - 1), pow(10, k)):
        if math.gcd(i, n) == 1:
            print (i, end = " ")
            cnt += 1
            if cnt % 10 == 0:
                print ()