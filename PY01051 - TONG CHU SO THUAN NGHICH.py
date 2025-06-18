def check(n):
    if n < 10:
        return False
    temp = str(n)
    for i in range(int(len(temp) / 2)):
        if temp[i] != temp[len(temp) - i - 1]:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = list(map(int, input()))
        if check(sum(a)):
            print ("YES")
        else:
            print ("NO")