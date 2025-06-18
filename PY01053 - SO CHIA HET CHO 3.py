if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = list(map(int, input()))
        if sum(a) % 3 == 0:
            print ("YES")
        else:
            print ("NO")