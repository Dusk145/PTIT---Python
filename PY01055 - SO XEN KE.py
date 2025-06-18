def check(n):
    for i in range(0, len(n) - 2, 2):
        if n[i] != n[i + 2]:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if len(n) % 2 == 1 and n[0] != n[1] and check(n):
            print ("YES")
        else:
            print ("NO")