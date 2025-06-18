import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        temp = ''.join(reversed(n))
        if math.gcd(int(n), int(temp)) == 1:
            print ("YES")
        else:
            print ("NO")