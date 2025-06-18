def check(n):
    idx = 0
    while idx < len(n):
        if idx + 3 <= len(n) and n[idx: idx + 3] == "688":
            idx += 3
        elif idx + 2 <= len(n) and n[idx: idx + 2] == "68":
            idx += 2
        elif n[idx] == "6":
            idx += 1
        else:
            return False
    return True

if __name__ == "__main__":
    n = input()
    if check(n):
        print ("YES")
    else:
        print ("NO")