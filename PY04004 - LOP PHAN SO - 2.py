import math

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    tu = a * d + c * b
    mau = b * d
    temp = math.gcd(tu, mau)
    print (f"{tu // temp}/{mau // temp}")