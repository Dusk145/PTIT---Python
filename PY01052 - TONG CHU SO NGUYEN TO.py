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
        a = list(map(int, input()))
        if nt(sum(a)):
            print ("YES")
        else:
            print ("NO")