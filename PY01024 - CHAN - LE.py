def digit_sum(n):
    S = 0
    temp = str(n)
    for i in range(len(temp)):
        S += int(temp[i])
    return S

def check(n):
    temp = str(n)
    for i in range(1, len(temp) - 1):
        if abs(int(temp[i]) - int(temp[i - 1])) != 2 or abs(int(temp[i]) - int(temp[i + 1])) != 2:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if check(n) and digit_sum(n) % 10 == 0:
            print ("YES")
        else:
            print ("NO")