def check():
    if len(a) != 4:
        return False
    for i in a:
        if not i.isdigit() or int(i) > 255:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = list(input().split("."))
        if check():
            print ("YES")
        else:
            print ("NO")