if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if n[len(n) - 2] == '8' and n[len(n) - 1] == '6':
            print ("YES")
        else:
            print ("NO")