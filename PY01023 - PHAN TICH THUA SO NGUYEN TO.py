import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print ("1", end = "")
        for i in range(2, int(math.sqrt(n)) + 1):
            cnt = 0
            while n % i == 0:
                cnt += 1
                n /= i
            if cnt != 0:
                print (" * " + str(i) + "^" + str(cnt), end = "")
        if n != 1:
            print (" * " + str(int(n)) + "^1", end = "")
        print ()