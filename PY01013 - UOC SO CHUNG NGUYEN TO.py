import math

def digit_sum(n):
    S = 0
    temp = str(n)
    for i in range(len(temp)):
        S += int(temp[i])
    return S

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        temp = math.gcd(a, b)
        if nt(digit_sum(temp)):
            print ("YES")
        else:
            print ("NO")