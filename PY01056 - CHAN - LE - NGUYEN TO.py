import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    S = 0
    for i in range(len(n)):
        if (i % 2 == 0 and int(n[i]) % 2 == 1) or (i % 2 == 1 and int(n[i]) % 2 == 0):
            return False
        S += int(n[i])
    if nt(S):
        return True
    return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if check(n):
            print ("YES")
        else:
            print ("NO")