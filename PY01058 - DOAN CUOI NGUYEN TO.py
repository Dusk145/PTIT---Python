import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        temp = n[len(n) - 4] + n[len(n) - 3] + n[len(n) - 2] + n[len(n) - 1]
        if nt(int(temp)):
            print ("YES")
        else:
            print ("NO")