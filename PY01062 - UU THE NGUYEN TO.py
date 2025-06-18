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
        ok = True
        if not nt(len(n)):
            ok = False
        cnt = 0
        for i in range(len(n)):
            if n[i] == "2" or n[i] == "3" or n[i] == "5" or n[i] == "7":
                cnt += 1
        if cnt <= len(n) - cnt:
            ok = False
        if ok:
            print ("YES")
        else:
            print ("NO")