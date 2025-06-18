if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        first = n[0] + n[1]
        last = n[len(n) - 2] + n[len(n) - 1]
        if first == last:
            print ("YES")
        else:
            print ("NO")