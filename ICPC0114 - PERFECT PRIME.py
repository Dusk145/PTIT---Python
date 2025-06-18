import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def change(n):
    s = str(n)
    return int(s[:: - 1])

def sum_digit(n):
    s = str(n)
    S = 0
    for i in s:
        if i == "2" or i == "3" or i == "5" or i == "7":
            S += int(i)
            continue
        return 0
    return S

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if nt(n) and nt(change(n)) and nt(sum_digit(n)):
            print ("Yes")
        else:
            print ("No")