import math

a = [True] * 600

def nt():
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(600)) + 1):
        if a[i]:
            for j in range(i * i, 600, i):
                a[j] = False

def check(n):
    for i in range(len(n)):
        if n[i] == "2" or n[i] == "3" or n[i] == "5" or n[i] == "7":
            if not a[i]:
                return False
    return True

if __name__ == "__main__":
    t = int(input())
    nt()
    for _ in range(t):
        n = input()
        if check(n):
            print ("YES")
        else:
            print ("NO")