import math

if __name__ == "__main__":
    a, b = map(int, input().split())
    for i in range(a, b - 1):
        for j in range(i + 1, b):
            if math.gcd(i, j) == 1:
                for k in range(j + 1, b + 1):
                    if math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                        print ("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")