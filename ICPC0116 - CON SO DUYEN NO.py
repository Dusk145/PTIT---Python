if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if n[0] == n[- 1]:
            print ("YES")
        else:
            print ("NO")